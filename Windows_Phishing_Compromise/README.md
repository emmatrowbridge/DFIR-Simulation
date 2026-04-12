**Developers:** Emma Trowbridge and Cam Zabroski

---

## Overview

This case simulates a digital forensics and incident response (DFIR) investigation involving a phishing-based compromise on a Windows corporate workstation.

You are provided with a curated set of forensic artifacts extracted from a newly provisioned employee device. Your objective is to analyze the evidence, reconstruct what occurred, and produce evidence-based conclusions.

This is an **introductory-to-intermediate level (medium)** case. The scenario is intentionally designed to require correlation across multiple sources of evidence, helping you strengthen core DFIR skills such as artifact analysis, process correlation, timeline reconstruction, user activity analysis, and attack narrative development.

---

## Getting Started

Begin by cloning the repository and navigating into it:

```bash
git clone https://github.com/emmatrowbridge/DFIR-Simulation-Platform.git
cd DFIR-Simulation-Platform/windows_phishing_compromise

Start by reading:

Required Reading
case_brief.md — background and context
investigation_questions.md — required questions to answer
Investigation Approach

All evidence is located in the evidence/ directory.

You should download and analyze these files locally on your machine, not directly in GitHub.

Suggested Workflow
Explore the directory structure in your terminal
Open files using appropriate tools
Identify relevant artifacts
Begin correlating activity across sources

This case does not require specialized forensic tools.

Basic artifact inspection and careful reasoning are sufficient.

Focus Areas

Pay close attention to:

Email activity and suspicious attachments
Browser access to email platforms
Downloaded files and document locations
Microsoft Word document execution
PowerShell process creation
Parent-child process relationships
User interaction evidence
Files created or modified after execution

Do not treat artifacts in isolation.

The key objective is correlating:

Email activity
Browser usage
Filesystem evidence
Process execution logs
PowerShell artifacts
Recording Your Answers

All answers should be completed in the workspace/ directory.

Create your working file by copying the template:

cp workspace/answers_template.json workspace/answers.json

Then open answers.json in a text editor and complete your responses.

Important Requirements

Make sure:

Exact file names and paths are used where applicable
All answers are supported by evidence
The file remains valid JSON

Do not remove quotes, commas, or brackets.

Optional Timeline Tracking

You may also use timeline_template.csv to organize events during your investigation.

This is optional but highly recommended.

Checking Your Work

Once you have completed your answers, run:

python validation/check_answers.py

The script will evaluate each answer and report whether it is correct or incorrect, along with a final summary.

About the Validation System

The validation system is included to support self-guided learning and immediate feedback.

The file validation/answer_key.json contains the expected answers used by the script.

You should not rely on it during the investigation.

The purpose of this case is to develop your ability to:

Interpret forensic artifacts
Correlate evidence across sources
Identify phishing-based execution chains
Reconstruct attacker activity
Build defensible conclusions
Final Notes

A strong investigation is not about finding a single suspicious file.

It is about connecting multiple artifacts into a coherent explanation of what occurred.

Individual actions may appear normal on their own.

Your task is to determine whether they form a meaningful pattern when viewed together.

This case specifically focuses on identifying how a phishing email, user interaction, document execution, and PowerShell activity combine into a complete compromise narrative.

Good luck.
