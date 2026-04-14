# DFIR Simulation Platform

This repository contains a collection of hands-on digital forensics and incident response (DFIR) cases designed to simulate real investigative work. Each scenario provides a curated set of forensic artifacts and asks a simple but demanding question: what actually happened, and how can you prove it?

Rather than guiding you step-by-step, these cases are built around the idea that forensic analysis is a process of interpretation. You are given evidence, not instructions. Your task is to examine that evidence, identify what is meaningful, and construct a coherent, evidence-based explanation of events.

## Available Cases

The platform currently includes several scenarios, ordered by increasing difficulty:

| Case | Platform | Scenario | Difficulty |
|------|--------|---------|------------|
| macOS Insider Data Exfiltration | macOS | An employee accesses and stages internal company data prior to departure | Easy |
| Windows Phishing Compromise | Windows | Credential theft and subsequent account misuse following a phishing attack | Easy |
| macOS Infostealer Malware | macOS | Malware infection resulting in the collection and staging of sensitive data | Medium |
| Windows Ransomware Intrusion | Windows | System compromise leading to ransomware execution and file encryption | Hard |

Each case is self-contained and includes its own background context, investigation questions, and validation system.

## How the Platform Works

To get started, clone the repository and select a case:

git clone https://github.com/emmatrowbridge/DFIR-Simulation-Platform.git  
cd DFIR-Simulation-Platform  
cd <case_name>  

From there, the case README will guide you through the setup and investigation process. In general, you will analyze artifacts located in the evidence/ directory, reconstruct a sequence of events, and record your conclusions in a structured answer file. A validation script is included in each case to provide immediate feedback on your results.

## What You Will Practice

These cases are designed to develop the core skills required in DFIR work. This includes identifying relevant activity within a large set of artifacts, recognizing patterns across different data sources, and connecting individual observations into a defensible narrative. Many questions cannot be answered by looking at a single file in isolation; instead, they require correlating multiple pieces of evidence.

The emphasis throughout is on reasoning. The goal is not simply to locate artifacts, but to understand their significance and use them to support clear conclusions.

## Who This Is For

This platform is intended for students, self-learners, and instructors who want practical experience with forensic investigation. It is especially useful for those preparing for cybersecurity roles, where the ability to analyze and interpret evidence is critical.

## Repository Structure

DFIR-Simulation-Platform/  
├── macOS_Insider_Data_Exfiltration/  
├── Windows_Phishing_Compromise/  
├── macOS_Infostealer_Malware/  
├── Windows_Ransomware_Intrusion/  

Within each directory, you will find the artifacts, investigation materials, and validation scripts needed to complete the case.

## Final Note

These cases are intentionally designed without step-by-step guidance. While the answer key is included for validation purposes, the value of the platform comes from working through the investigation independently and developing your own understanding of the evidence.

## Contributors

Emma Trowbridge  
Cam Zabroski 
