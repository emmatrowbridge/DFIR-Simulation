Case Brief — macOS Insider Data Exfiltration

Overview
Case Title: macOS Insider Data Exfiltration
Scenario Category: Insider Threat / Data Exfiltration
Difficulty: Easy
This case introduces insider threat investigations in a controlled, realistic environment. The sequence of activity is intentionally clear and tightly grouped in time. The goal is to ensure that investigators can reconstruct a complete and defensible narrative using a limited set of artifacts.
The case reflects a common real-world situation in which a legitimate employee, using authorized access, engages in potentially suspicious behavior shortly before departing an organization.

Organization Context
Company Name: Applied Logic Platforms (ALP)
Industry: SaaS / Developer Tooling
Environment: macOS developer workstation
Applied Logic Platforms develops internal developer tooling and customer workflow automation software. Engineers have access to internal documentation, API credentials, and limited customer data for testing purposes.
Developer systems are not fully locked down and allow flexibility for development workflows, including browser access and cloud services. This reflects a realistic balance between security and productivity.
This investigation begins after internal monitoring flagged unusual activity associated with an employee who recently submitted their resignation.

User Profile
Name: Jason Wang
Role: Software Engineer
Department: Internal Tools Engineering
ALP Email (managed): jwang.dev@gmail.com
Local Username: jwang
Jason is a legitimate employee with authorized access to the files involved in the investigation. The concern is not unauthorized access, but whether legitimate access was used inappropriately.

Account Configuration
Jason uses two Google accounts on this device:
• ALP-managed account (primary): jwang.dev@gmail.com
• Personal account (unmanaged): jasonwang@gmail.com
Jason is signed into Google Chrome using his ALP-managed account and has also accessed his personal account within the browser.
This dual-account setup is common and may enable movement of data between managed and unmanaged environments.

System Environment
Operating System: macOS
File System: APFS
Hostname: alp-macbook-jwang
Timezone: America/New_York
The system contains a mix of work-related and personal activity and reflects a typical developer workstation.

Incident Trigger
Jason submitted his two-week notice earlier in the week.
Over the weekend, monitoring identified unusual activity associated with his account, including:
• Access to internal files
• Cloud-related activity outside normal hours
• A login from an unfamiliar location
This combination of events prompted a forensic review of the system.
No conclusions have been made.

Pre-Scenario System State
The system reflects normal usage and is not artificially clean.
The filesystem contains project directories, personal files, and application-generated data. The internal-tools directory contains sensitive internal files relevant to the investigation.
Standard user directories such as Desktop, Documents, and Downloads contain typical working files. No staging directory existed prior to the incident.
The system also includes normal background activity such as browser history, application usage, and file access events.

Investigation Objective
Your task is to determine:
• What actions occurred
• When they occurred
• How they relate to one another
You must rely only on the provided artifacts.

Investigation Questions
Which files were accessed from the internal-tools directory?
What directory was created to stage files?
When was the staging directory created?
Which files were copied into the staging directory?
When were the staged files created?
What application was used to access an external service?
What external service was accessed?
Which Google account(s) were involved in the activity?
What sequence of observable actions suggests data movement between accounts?
What type of incident best explains the observed activity?

Investigation Framing
This case is not presented as a confirmed security incident.
The user has legitimate access to the data, and all actions are performed using valid credentials. The investigation focuses on interpreting behavior and determining whether it is consistent with normal usage.
All conclusions must be supported by observable evidence. Avoid assumptions that are not directly supported by artifacts.

Summary
This case simulates a realistic insider threat scenario involving potential data movement using cloud services.
The investigation emphasizes:
• Artifact correlation
• Timeline reconstruction
• Evidence-based reasoning
Your goal is to reconstruct a coherent and defensible narrative based on the provided artifacts.
