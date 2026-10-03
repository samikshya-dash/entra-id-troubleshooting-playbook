# Error code lookup

[← Back to the playbook](README.md)

Find the code, read what it means in plain words, and jump to the scenario that fixes it. Sign-in codes are shown in the logs as a number (`ResultType`) and on screen with the prefix `AADSTS`.

> **Not a failure:** `50140` (the "Stay signed in?" prompt) and `50199` (a confirmation prompt) are interrupts, not errors. Exclude them when you count failures.

## Sign-in codes (AADSTS)

| Code | Plain meaning | Go to |
|---|---|---|
| `16000` | The account isn't in this tenant, so it can't use the app | [22](scenarios/06-risk-guests-platform.md#22-guest-cant-sign-in-or-redeem-an-invitation) |
| `50008` | The SAML assertion from the federation server is missing or invalid | [13](scenarios/03-hybrid-sync.md#13-federated-sign-in-failure-ad-fs) · [8](scenarios/02-applications.md#8-saml-single-sign-on-failure) |
| `50011` | The reply URL the app sent isn't registered | [7](scenarios/02-applications.md#7-app-fails-to-authenticate) |
| `50020` | The account comes from another identity provider and isn't a guest here | [22](scenarios/06-risk-guests-platform.md#22-guest-cant-sign-in-or-redeem-an-invitation) |
| `50034` | User not found in this directory | [1](scenarios/01-sign-in.md#1-user-cant-sign-in) |
| `50053` | Account locked after too many bad attempts | [5](scenarios/01-sign-in.md#5-account-lockout-loop) |
| `50055` | Password expired | [1](scenarios/01-sign-in.md#1-user-cant-sign-in) |
| `50057` | Account disabled | [1](scenarios/01-sign-in.md#1-user-cant-sign-in) |
| `50058` | Silent sign-in couldn't find a session; the user must sign in interactively | [6](scenarios/01-sign-in.md#6-repeated-sign-in-prompts) |
| `50072` | The user must register a second factor | [2](scenarios/01-sign-in.md#2-mfa-problems) |
| `50074` | MFA was required and the user didn't pass it | [2](scenarios/01-sign-in.md#2-mfa-problems) |
| `50076` | MFA is now required because of a policy or location change | [2](scenarios/01-sign-in.md#2-mfa-problems) |
| `50079` | The user must register for MFA | [2](scenarios/01-sign-in.md#2-mfa-problems) |
| `50097` | Device authentication is required | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |
| `50105` | The user isn't assigned to the application | [9](scenarios/02-applications.md#9-user-not-assigned-or-consent-missing) |
| `50107` | The federation realm doesn't exist: domain federation is misconfigured | [13](scenarios/03-hybrid-sync.md#13-federated-sign-in-failure-ad-fs) |
| `50126` | Wrong username or password | [1](scenarios/01-sign-in.md#1-user-cant-sign-in) |
| `50129` | The device must be registered (workplace joined) | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `50133` | Session ended because the password changed or expired | [6](scenarios/01-sign-in.md#6-repeated-sign-in-prompts) |
| `50135` | Password change required because the account is at risk | [21](scenarios/06-risk-guests-platform.md#21-user-risk-detections-not-addressed) |
| `50144` | The on-premises Active Directory password has expired | [1](scenarios/01-sign-in.md#1-user-cant-sign-in) |
| `50155` | Device authentication failed | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |
| `50158` | An external security challenge (such as third-party MFA) wasn't satisfied | [2](scenarios/01-sign-in.md#2-mfa-problems) |
| `50173` | The token was revoked, usually after a password change or an admin action | [6](scenarios/01-sign-in.md#6-repeated-sign-in-prompts) |
| `50196` | A client is stuck in a sign-in loop | [23](scenarios/06-risk-guests-platform.md#23-slow-sign-ins-throttling-or-a-service-incident) |
| `53000` | Conditional Access needs a compliant device, and this one isn't | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |
| `53001` | Conditional Access needs a domain-joined device, and this one isn't | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |
| `53003` | Blocked by Conditional Access | [3](scenarios/01-sign-in.md#3-blocked-by-conditional-access) |
| `53004` | MFA registration is blocked because the sign-in is risky | [21](scenarios/06-risk-guests-platform.md#21-user-risk-detections-not-addressed) |
| `65001` | Nobody has consented to the permissions the app needs | [9](scenarios/02-applications.md#9-user-not-assigned-or-consent-missing) |
| `65004` | The user declined the consent prompt | [9](scenarios/02-applications.md#9-user-not-assigned-or-consent-missing) |
| `70043` | The refresh token expired because of a sign-in frequency policy | [6](scenarios/01-sign-in.md#6-repeated-sign-in-prompts) |
| `75005` | Entra doesn't support the SAML request the app sent | [8](scenarios/02-applications.md#8-saml-single-sign-on-failure) |
| `75011` | The app asked for an authentication method that doesn't match how the user signed in | [8](scenarios/02-applications.md#8-saml-single-sign-on-failure) |
| `80012` | Pass-through authentication: sign-in outside the user's allowed logon hours | [12](scenarios/03-hybrid-sync.md#12-password-sync-or-pass-through-authentication-failing) |
| `81010` | Seamless single sign-on failed: the Kerberos ticket is expired or invalid | [6](scenarios/01-sign-in.md#6-repeated-sign-in-prompts) |
| `90033` | The Microsoft directory service is temporarily unavailable | [23](scenarios/06-risk-guests-platform.md#23-slow-sign-ins-throttling-or-a-service-incident) |
| `90072` | The external account doesn't exist in the tenant it signed in to | [22](scenarios/06-risk-guests-platform.md#22-guest-cant-sign-in-or-redeem-an-invitation) |
| `90094` | An administrator must consent | [9](scenarios/02-applications.md#9-user-not-assigned-or-consent-missing) |
| `90095` | Admin consent is required; the user can send a request | [9](scenarios/02-applications.md#9-user-not-assigned-or-consent-missing) |
| `135011` | The device used for the sign-in is disabled | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |
| `500011` | The resource (API) the app asked for isn't in this tenant | [7](scenarios/02-applications.md#7-app-fails-to-authenticate) |
| `500121` | The MFA challenge failed | [2](scenarios/01-sign-in.md#2-mfa-problems) |
| `500213` | Your tenant's cross-tenant access policy doesn't allow this external user | [22](scenarios/06-risk-guests-platform.md#22-guest-cant-sign-in-or-redeem-an-invitation) |
| `530032` | Blocked by a tenant security policy | [3](scenarios/01-sign-in.md#3-blocked-by-conditional-access) |
| `700016` | The application isn't found in the tenant (wrong client ID or tenant) | [7](scenarios/02-applications.md#7-app-fails-to-authenticate) |
| `700082` | The refresh token expired after long inactivity | [6](scenarios/01-sign-in.md#6-repeated-sign-in-prompts) |
| `7000215` | Invalid client secret | [7](scenarios/02-applications.md#7-app-fails-to-authenticate) · [10](scenarios/02-applications.md#10-service-principal-or-workload-identity-failing) |
| `7000222` | The client secret has expired | [7](scenarios/02-applications.md#7-app-fails-to-authenticate) · [10](scenarios/02-applications.md#10-service-principal-or-workload-identity-failing) |

## Directory sync errors

| Error | Plain meaning | Go to |
|---|---|---|
| `AttributeValueMustBeUnique` | Two objects share a UPN, mail or proxy address | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |
| `InvalidSoftMatch` | Matched a cloud object that already belongs to another on-premises object | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |
| `InvalidHardMatch` | Match by source anchor was blocked, often an admin-role account | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |
| `ObjectTypeMismatch` | Objects of different types share an address | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |
| `DataValidationFailed` | UPN has unsupported characters or format | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |
| `LargeObject` | An attribute holds too many values | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |
| `DeletingCloudOnlyObjectNotAllowed` | Sync tried to delete a cloud-only object | [11](scenarios/03-hybrid-sync.md#11-directory-sync-errors) |

## Windows event IDs

| Log and source | Event | Plain meaning | Go to |
|---|---|---|---|
| Application · Directory Synchronization | `654` | Password sync heartbeat (every 30 minutes) | [12](scenarios/03-hybrid-sync.md#12-password-sync-or-pass-through-authentication-failing) |
| Application · Directory Synchronization | `611` · `655` | Password sync error | [12](scenarios/03-hybrid-sync.md#12-password-sync-or-pass-through-authentication-failing) |
| Application · PasswordResetService | `31002` · `31003` | Password writeback succeeded · failed | [20](scenarios/05-access-governance.md#20-self-service-password-reset-fails) |
| Application · PasswordResetService | `33004` · `33008` | Writeback: no permission · password policy not met | [20](scenarios/05-access-governance.md#20-self-service-password-reset-fails) |
| Application · PasswordResetService | `32002` | Writeback can't reach Service Bus | [20](scenarios/05-access-governance.md#20-self-service-password-reset-fails) |
| User Device Registration | `304` · `305` · `307` | Device join failed (phase, authentication, detail) | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| AAD · Operational | `1081` · `1088` | Primary Refresh Token errors | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |
| Security (domain controller) | `4740` · `4625` · `4771` | Account locked out · failed logon · Kerberos pre-authentication failed | [5](scenarios/01-sign-in.md#5-account-lockout-loop) |
| AD FS · Admin | `364` · `342` | Federation request error · token validation failed | [13](scenarios/03-hybrid-sync.md#13-federated-sign-in-failure-ad-fs) |

## Device join codes

| Code | Plain meaning | Go to |
|---|---|---|
| `0x801c001d` | Can't read the Service Connection Point | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `0x801c0021` · `0x801c001f` | Discovery failed or timed out | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `0x801c003a` | Tenant not found | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `0x801c03f2` | Directory error: the computer object hasn't synced | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `0x80072ee2` · `0x80072efd` · `0x80072ee7` | Network timeout · can't connect · name not resolved | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `0x80090016` · `0x80290407` | TPM errors | [14](scenarios/04-devices.md#14-device-registration-or-hybrid-join-fails) |
| `0xc000006d` · `0xc000006a` | Primary Refresh Token: sign-in failed · wrong password | [15](scenarios/04-devices.md#15-device-not-compliant-or-no-primary-refresh-token) |

Source for the meanings: Microsoft Learn's reference pages for authentication error codes, Entra Connect sync errors, hybrid join troubleshooting and password writeback. Microsoft adds and changes codes, so check the [official list](https://learn.microsoft.com/en-us/entra/identity-platform/reference-error-codes) for anything not shown here.

[← Back to the playbook](README.md)
