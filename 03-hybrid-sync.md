# Hybrid identity: sync, passwords and federation

[← Back to the playbook](../README.md)

| # | Scenario | Typical signals |
|---|---|---|
| 11 | [Directory sync errors](#11-directory-sync-errors) | AttributeValueMustBeUnique · InvalidSoftMatch · ObjectTypeMismatch |
| 12 | [Password sync or pass-through authentication failing](#12-password-sync-or-pass-through-authentication-failing) | Event 611 · 655 · agent inactive |
| 13 | [Federated sign-in failure (AD FS)](#13-federated-sign-in-failure-ad-fs) | 50107 · 50008 · AD FS event 364 |

```mermaid
flowchart LR
    AD[(On-premises<br/>Active Directory)] -->|import| CS[Connector space]
    CS -->|sync rules| MV[Metaverse]
    MV -->|export| EN[(Microsoft Entra ID)]
    AD -. password hashes .-> EN
    classDef a fill:#14325c,stroke:#63b3ed,color:#fff;
    classDef b fill:#0f4032,stroke:#199e70,color:#fff;
    class CS,MV a; class AD,EN b;
```

A sync problem is always at one of three steps: **import** (reading from Active Directory), **sync** (applying rules) or **export** (writing to Entra ID). Find the step that shows the error and you have halved the search.

---

## 11. Directory sync errors

**What you see:** a new user, group or attribute change made on-premises never appears in the cloud, or a "directory synchronization error" email arrives.

| Error | What it means | Fix |
|---|---|---|
| **AttributeValueMustBeUnique** | Two objects have the same `userPrincipalName`, `mail` or `proxyAddresses` value | Find the duplicate, decide which object keeps the value, remove it from the other, sync again |
| **InvalidSoftMatch** | The object matched an existing cloud object by address, but the cloud object is already tied to a different on-premises object | Remove the duplicate address from the object that shouldn't have it |
| **ObjectTypeMismatch** | A user, group or contact shares an address with an object of a different type | Remove the shared value from one of them |
| **InvalidHardMatch** | A match by source anchor was blocked, often because the cloud account holds an admin role | Temporarily remove the role, sync, then restore the role |
| **DataValidationFailed** | The UPN has unsupported characters or a wrong format | Correct the UPN on-premises |
| **LargeObject** | Too many values in one attribute (for example more than 15 certificates, or hundreds of proxy addresses) | Remove expired certificates or old addresses |
| **DeletingCloudOnlyObjectNotAllowed** | Sync is trying to delete an object that is now cloud-only | Check whether the user was moved out of sync scope by mistake |

| Other cause | How to confirm | Fix |
|---|---|---|
| Sync scheduler is off or stuck | `Get-ADSyncScheduler` shows `SyncCycleEnabled : False`, or the last run is hours old | `Set-ADSyncScheduler -SyncCycleEnabled $true`, then `Start-ADSyncSyncCycle -PolicyType Delta` |
| Object is out of scope | The OU isn't selected, or a filtering rule excludes it | Add the OU or adjust the filter, then run a full import |
| Server is in staging mode | `StagingModeEnabled : True` on the server you think is active | Confirm which server is active. Only one should export |
| Connector account lost permissions | Export shows `permission-issue` | Restore the account's permissions on the affected OU |
| Server can't reach Microsoft | Export shows `no-start-connection` or `stopped-server-down` | Check proxy, firewall and TLS 1.2 |

**Where to look:** Entra admin center → Microsoft Entra Connect → Connect Sync errors (Connect Health) · on the server: **Synchronization Service Manager** → Operations tab · Application event log, source `ADSync`.

```powershell
Get-ADSyncScheduler                                  # is the scheduler on, and when is the next run
Start-ADSyncSyncCycle -PolicyType Delta              # run a sync now
Invoke-ADSyncDiagnostics                             # guided checks for objects and passwords
```

```kusto
// Directory sync changes that failed, from the audit log
AuditLogs
| where TimeGenerated > ago(24h)
| where tostring(InitiatedBy) has "Sync_" and Result != "success"
| project TimeGenerated, OperationName, Result, ResultReason, Target = tostring(TargetResources[0].userPrincipalName)
| order by TimeGenerated desc
```

**Prevent it:** run IdFix before onboarding new domains or OUs · a second server in staging mode for failover · alert on sync being more than two hours old.

---

## 12. Password sync or pass-through authentication failing

**What the user sees:** the new on-premises password doesn't work in the cloud (password hash sync), or cloud sign-ins fail while on-premises sign-ins work (pass-through authentication).

**Password hash sync**

| Cause | How to confirm | Fix |
|---|---|---|
| Sync isn't running | No event `654` (heartbeat, every 30 minutes) or `656`/`657` (request and response) in the Application log | Restart the sync service; run `Invoke-ADSyncDiagnostics -PasswordSync` |
| Error for a domain | Event `611` or `655` | Check connectivity to a domain controller and the connector account's replication permissions |
| "User must change password at next logon" is set | Per-object status `FilteredByTarget` | The user changes the password on-premises first; temporary passwords aren't synced by default |
| Object isn't synced at all | Status `NoTargetConnection` or `SourceConnectorNotPresent` | Fix the object's sync first (scenario 11) |
| Full sync hasn't finished | Event `613` | Wait for the directory full sync to complete |

**Pass-through authentication**

| Cause | How to confirm | Fix |
|---|---|---|
| Agent offline | Entra admin center → Microsoft Entra Connect → Pass-through authentication shows the agent **Inactive** | Start the agent service; install at least three agents for resilience |
| Agent can't reach a domain controller | Sign-in logs show an `8000x` on-premises validation error, for example `80012` (outside allowed logon hours) | Check the agent server's network path to the domain controllers |
| On-premises account state | Account locked, disabled or expired in Active Directory | Fix the account on-premises |

**Password writeback (self-service reset)** is covered in [scenario 20](05-access-governance.md#20-self-service-password-reset-fails).

**Where to look:** Application event log, source `Directory Synchronization` · `Invoke-ADSyncDiagnostics -PasswordSync` · Connect Health.

**Prevent it:** monitor for the 30-minute heartbeat event · keep password hash sync enabled as a backup even when using pass-through or federation.

---

## 13. Federated sign-in failure (AD FS)

**What the user sees:** redirected to the organisation's own sign-in page, which shows an error, or returns to Microsoft with an error.

| Cause | How to confirm | Fix |
|---|---|---|
| Token-signing certificate rolled over, Entra not updated | `50008` after AD FS sign-in succeeds; certificate dates differ between AD FS and the domain's federation settings | Update the federation settings with the new certificate |
| AD FS or the proxy is down | The sign-in page doesn't load; **no** Entra sign-in log entry | Restore the AD FS farm or Web Application Proxy |
| Extranet lockout | AD FS security audit shows the lockout for that user | Unlock in AD FS; find the source of bad passwords (scenario 5) |
| Claim rule broken | AD FS Admin log event `364`; `ImmutableID` or UPN claim missing | Repair the issuance rules for the Microsoft 365 relying party |
| Domain misconfigured | `50107` (federation realm doesn't exist) | Check the domain's federation configuration and issuer URI |
| Bad credentials at AD FS | AD FS event `342` or `411` (token validation failed) | User corrects the password, or resets it |

**Where to look:** on the AD FS server: **AD FS/Admin** event log and the Security log · Entra admin center → Connect Health for AD FS · Sign-in logs (only if the request reached Entra).

**Prevent it:** alert on token-signing certificate expiry · plan a move to cloud authentication (password hash sync with seamless single sign-on) to remove the dependency on the AD FS farm.

---

[← Applications](02-applications.md) · [Back to the playbook](../README.md) · [Next: Devices →](04-devices.md)
