# Case Brief: Windows Phishing Compromise

---
## Background
Applied Logic Platforms (ALP) is a SaaS company that develops internal developer tooling and customer workflow automation software.

As part of the onboarding process, new employees receive multiple emails from internal departments such as Human Resources, IT, and Customer Operations. These communications often include attached documents, onboarding guides, and access instructions.

Because onboarding involves frequent email communication and document downloads, new employees may be more vulnerable to phishing attempts that imitate legitimate internal messaging.

---
## Situation
A newly onboarded employee, Asa Bohnson, was issued a corporate Windows workstation as part of the standard onboarding process.

Shortly after beginning orientation activities, security monitoring systems identified unusual process activity on the device.

This activity occurred soon after Asa opened an email attachment received during onboarding.

Observed activity includes:
* Document execution from a downloaded email attachment
* Unexpected process creation shortly after opening the file
* Malicious activity on the workstation
* Additional application activity following execution

Due to the timing and context, this activity has been flagged for review.

---
## System Information
* **Hostname:** alp-win11-aBohnson
* **Operating System:** Windows 11
* **Timezone:** America/New_York
* **User:** aBohnson

This system is Asa’s newly provisioned corporate workstation. It contains early-stage onboarding activity including email access, downloaded onboarding files, and standard user interaction.

### Account Context
Asa is a newly hired Product Analyst in the Customer Operations department.

As part of the onboarding process, Asa has been actively reviewing:
* onboarding documentation
* HR communications
* company resource guides
* external emails

This activity creates a realistic environment in which malicious communication may appear similar to legitimate onboarding materials.

---
## Investigation Scope
You have been provided with forensic artifacts extracted from Asa’s system.

Your task is to determine:
* What email or file initiated the activity
* What process execution occurred on the system
* Whether PowerShell was executed
* What user action enabled execution
* What sequence of events led to the observed activity
* Whether the behavior is consistent with a phishing-based compromise

Some activity may need to be inferred through correlation of multiple artifacts rather than directly observed.

---
## Important Notes
* The user has legitimate access to the system
* No assumptions should be made beyond observable evidence
* All conclusions must be based on artifact correlation

This investigation focuses on reconstructing what happened, not assigning intent.

---
## Objective
Analyze the provided artifacts and reconstruct a clear, evidence-supported sequence of events.

No conclusions have been made. The purpose of the investigation is to determine what occurred and whether the system was compromised through phishing-based document execution.

