macOS Insider Data Exfiltration — Investigation Guide

Overview
This case provides a structured set of forensic artifacts for analyzing a potential insider data exfiltration scenario on a macOS system.
The case is artifact-driven. You will work with extracted evidence rather than a full disk image.
Getting Started
Read the Case Brief to understand the scenario
Review the investigation questions
Begin analysis using the provided artifacts
Evidence Overview
Filesystem Artifacts
Location: evidence/filesystem
These artifacts include project directories, user files, and potential staging locations. They provide insight into file access and modification activity.
Browser Artifacts
Location: evidence/browser
These artifacts include Chrome data such as browsing history, cookies, login data, and preferences. They provide insight into web activity and account usage.

Parsed Artifacts
Location: evidence/parsed
These artifacts include extracted and preprocessed data such as CSV files. They are provided to support faster analysis and alternative workflows.

Investigation Approach
You are expected to:
• Identify relevant artifacts
 • Distinguish meaningful activity from background noise
 • Correlate events across multiple data sources
 • Reconstruct a timeline of activity
The key to this case is correlation, not any single artifact.

Workspace
Use the workspace directory to organize your findings.

Answers Template
The answers template should be used to record structured responses to the investigation questions.
Timeline Template
The timeline template should be used to document key events, their order, and the evidence supporting them.
Tools
You may use any tools you prefer, including:
• Spreadsheet software
 • SQLite database viewers
 • Text editors
 • Timeline tools
No specific tool is required.
Important Notes
• Not all actions are directly observable
 • Some conclusions require inference
 • Focus on evidence, not assumptions
Objective
Your goal is to reconstruct what occurred on the system and determine whether the observed activity is consistent with normal behavior or indicative of inappropriate data handling.
Final Output
At the end of the investigation, you should produce:
• Completed answers to all investigation questions
 • A structured timeline of events
 • A defensible explanation of the observed activity
Optional Use of Full Disk Image and Tools
A full disk image and supporting analysis tools are provided as part of this case for users who wish to perform a complete forensic workflow.
You may choose to use these tools to independently parse the image and extract artifacts. This approach more closely reflects real-world DFIR investigations and allows for deeper exploration of the system.
However, use of the disk image and tools is not required to complete this investigation.
All necessary artifacts have already been extracted and are available within the provided evidence directories. These artifacts contain sufficient information to answer all investigation questions and reconstruct the timeline of events.
Students are encouraged to focus on analyzing the provided artifacts and developing a defensible narrative based on the available evidence.
