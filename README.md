<p align="center">
  <img src="assets/header.svg" alt="Samikshya Dash, Identity Security Architect" width="100%">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/samikshya-dash-cybersecurity"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:smkshy@hotmail.com"><img src="https://img.shields.io/badge/Email-smkshy%40hotmail.com-0b1b33?style=for-the-badge&logo=microsoftoutlook&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Based_in-Bengaluru-4fd1c5?style=for-the-badge" alt="Bengaluru">
</p>

I'm an identity security architect at Accenture with 9+ years in tech. I lead security delivery for 15+ enterprise clients and own the roadmap for a consumer identity platform used by 100M+ people across 9 markets. When the same problem shows up in the ticket queue twice, I write code so it doesn't show up a third time.

<p align="center">
  <img src="assets/impact.svg" alt="Impact: 100M+ users, 9 markets, $50M+ deals, 85%+ less manual work, 92% fewer SSO outages, 62% AI adoption" width="100%">
</p>

## 🛡️ What I work on

| Area | Stack |
|---|---|
| **Identity & Zero Trust** | ![Entra ID](https://img.shields.io/badge/Entra_ID-0078D4?style=flat-square&logo=microsoft&logoColor=white) ![Azure AD B2C](https://img.shields.io/badge/Azure_AD_B2C-0078D4?style=flat-square&logo=microsoftazure&logoColor=white) ![PIM](https://img.shields.io/badge/PIM-0078D4?style=flat-square) ![Conditional Access](https://img.shields.io/badge/Conditional_Access-0078D4?style=flat-square) ![SailPoint](https://img.shields.io/badge/SailPoint-0033A1?style=flat-square) ![CISA ZTMM](https://img.shields.io/badge/CISA_Zero_Trust-1f3a5f?style=flat-square) |
| **Cloud security** | ![Azure](https://img.shields.io/badge/Azure_WAF_%26_Front_Door-0078D4?style=flat-square&logo=microsoftazure&logoColor=white) ![AWS](https://img.shields.io/badge/AWS_IAM_%7C_KMS_%7C_Secrets_Manager-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white) ![Prisma Cloud](https://img.shields.io/badge/Prisma_Cloud_CSPM-00C0E8?style=flat-square&logo=paloaltonetworks&logoColor=white) |
| **Detection & response** | ![Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0078D4?style=flat-square&logo=microsoft&logoColor=white) ![KQL](https://img.shields.io/badge/KQL-1f3a5f?style=flat-square) ![Defender XDR](https://img.shields.io/badge/Defender_XDR-0078D4?style=flat-square&logo=microsoft&logoColor=white) |
| **AI security** | ![Security Copilot](https://img.shields.io/badge/Security_Copilot_(RAG)-6B46C1?style=flat-square&logo=microsoft&logoColor=white) ![Copilot Studio](https://img.shields.io/badge/Copilot_Studio-6B46C1?style=flat-square) ![AI red teaming](https://img.shields.io/badge/AI_agent_red_teaming-C53030?style=flat-square) |
| **Automation** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white) ![n8n](https://img.shields.io/badge/n8n_agentic_AI-EA4B71?style=flat-square&logo=n8n&logoColor=white) ![Bitbucket](https://img.shields.io/badge/Bitbucket_CI%2FCD-0052CC?style=flat-square&logo=bitbucket&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Azure DevOps](https://img.shields.io/badge/Azure_DevOps-0078D7?style=flat-square&logo=azuredevops&logoColor=white) |

## 🔧 Things I've built at work

Client code stays with clients, so I rebuilt five of them as public, runnable versions with synthetic data, flow diagrams and the design decisions behind each one. **[See the full repository →](https://github.com/samikshya-dash/identity-security-automation)**

| | Project | What changed in production |
|---|---|---|
| 📜 | [**SAML certificate lifecycle**](https://github.com/samikshya-dash/identity-security-automation/tree/main/saml-cert-lifecycle) · Graph API, Python, Bitbucket CI/CD, ServiceNow | Priority SSO outages **−92%** |
| 🔑 | [**Secrets scanner**](https://github.com/samikshya-dash/identity-security-automation/tree/main/secrets-scanner) · regex + entropy, pre-commit, CI gate | **77** leaked secrets caught in **37** repos before production |
| 🤖 | [**Self-healing operations**](https://github.com/samikshya-dash/identity-security-automation/tree/main/self-healing-ops) · n8n agentic AI with guardrails | **−67%** effort, about **60 h/month** saved |
| 📨 | [**GDPR request automation**](https://github.com/samikshya-dash/identity-security-automation/tree/main/gdpr-dsr-automation) · OneTrust, Event Hub, Python | **4,000–6,000** requests/month, **2–3 h/day** freed |
| ⚡ | [**Session revocation**](https://github.com/samikshya-dash/identity-security-automation/tree/main/session-revocation) · Sentinel KQL, Logic Apps, Graph | Compromised sessions killed in **under 2 s** |
| 📖 | [**Entra ID troubleshooting playbook**](https://github.com/samikshya-dash/entra-id-troubleshooting-playbook) · 24 scenarios, real error codes, KQL | From the error on screen to the cause and the fix |

### How the SAML lifecycle works

```mermaid
flowchart LR
    A([Daily pipeline]) --> B[Graph API:<br/>scan every SAML app]
    B --> C{Expiring?}
    C -- no --> Z([Healthy])
    C -- yes --> D{Owner?}
    D -- yes --> E[Alert at 90 · 60 · 30 · 7 days]
    D -- no --> F[ServiceNow ticket]
    E --> G[Safe rollover<br/>24 h before expiry]
    F --> G
    classDef step fill:#14325c,stroke:#63b3ed,color:#fff;
    classDef ok fill:#0f4032,stroke:#199e70,color:#fff;
    class A,B,E,F,G step;
    class Z ok;
```

## 📚 Learning right now

Executive Diploma in Machine Learning & AI at **IIIT Bengaluru** (finishing 2027), with a focus on securing AI agents.

## 🏅 Certifications

![SC-100](https://img.shields.io/badge/SC--100-Cybersecurity_Architect_Expert-0078D4?style=flat-square&logo=microsoft)
![AZ-305](https://img.shields.io/badge/AZ--305-Azure_Solutions_Architect_Expert-0078D4?style=flat-square&logo=microsoft)
![SC-300](https://img.shields.io/badge/SC--300-Identity_%26_Access_Admin-0078D4?style=flat-square&logo=microsoft)
![AZ-500](https://img.shields.io/badge/AZ--500-Azure_Security_Engineer-0078D4?style=flat-square&logo=microsoft)
![AZ-104](https://img.shields.io/badge/AZ--104-Azure_Administrator-0078D4?style=flat-square&logo=microsoft)
![MS-102](https://img.shields.io/badge/MS--102-Microsoft_365_Admin-0078D4?style=flat-square&logo=microsoft)
