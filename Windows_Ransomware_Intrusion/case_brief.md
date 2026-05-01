# Case Brief: Windows Ransomware Intrusion

---
## Background
Stark Engineering is a mid-sized infrastructure consulting firm that manages transportation and public works projects across multiple municipalities.

Employees regularly work with project documentation, vendor records, financial data, and site materials stored locally on their workstations.

The organization maintains standard enterprise logging and monitoring capabilities. However, employee systems are not tightly restricted and are frequently used for a mix of operational, administrative, and project-related tasks.

---
## Situation
On April 25, Madison Tanner reported that a number of files on her workstation were no longer accessible.

She also noted that her system had recently installed an update and had been behaving unusually, including reduced performance and intermittent system issues.

Shortly after, additional users reported similar problems on their systems.

The IT team collected Madison’s workstation for analysis. During initial review, they observed that many files on the system had been modified and were no longer accessible. Many of these files exhibited a `.locked` extension.

Further examination identified the presence of an unfamiliar message left on the system, indicating that access to files had been restricted.

Based on these findings, the incident is believed to involve ransomware.

Madison has stated that she did not intentionally install or execute any unfamiliar software.

Due to these findings, the DFIR team has been tasked with determining how the ransomware was introduced onto the system and assessing the extent of its impact.

---
## System Information
* **Hostname:** SE-PC-MTANNER
* **Operating System:** Windows 11 Pro
* **Timezone:** America/New_York
* **User:** mtann

This system is a standard employee workstation used for project coordination, documentation, and communication.

### Account Context
Madison is responsible for managing project documentation, coordinating with vendors, and maintaining internal records.

Her daily activity includes accessing shared files, reviewing documents, and communicating with internal and external stakeholders.

This system reflects typical business usage and contains a mix of routine and project-related activity.

---
## Investigation Scope
You have been provided with forensic artifacts extracted from Madison's system.

Your task is to determine:
* How the ransomware was introduced onto the system
* What actions occurred following initial access
* Which activity is directly related to the incident
* How widespread the impact is across the system

Some activity may need to be inferred through the correlation of multiple artifacts rather than directly observed.

---
## Important Notes
* The user has legitimate access to the files on this system
* No assumptions should be made about intent
* Not all activity is malicious; some may be unrelated to the incident
* All conclusions must be based on observable evidence
* Some actions may not be directly logged and must be inferred from available artifacts

This investigation focuses on what happened, not why.

---
## Objective
Analyze the provided artifacts and reconstruct a clear, evidence-supported sequence of events.

No conclusions have been made. The purpose of the investigation is to determine what occurred and identify the source and scope of the incident.
