# DFIR Simulation Platform

**Developers:** Emma Trowbridge and Cam Zabroski

This repository contains a collection of digital forensics and incident response (DFIR) cases designed to provide practical, hands-on investigation experience.

The project was built around a simple idea: it should be possible to practice real forensic analysis without needing a specialized lab environment or access to formal coursework. Many existing DFIR exercises rely on full disk images, platform-specific tooling, or tightly guided walkthroughs. This platform takes a different approach by providing curated artifacts that can be analyzed on any system, while still preserving the structure and ambiguity of a real investigation.

Each case presents a scenario supported by forensic artifacts extracted from a system. Your task is to examine those artifacts, determine what is relevant to the investigation, and reconstruct what happened using evidence. The focus is not on following instructions, but on developing the ability to interpret data and connect findings across multiple sources.

## Available Cases
The platform currently includes the following cases, ordered by increasing difficulty:

| Case | Platform | Scenario | Difficulty |
|------|--------|---------|------------|
| macOS Insider Data Exfiltration | macOS | Following a resignation notice, an engineer’s system shows unusual after-hours activity involving internal files and external services | Easy |
| Windows Phishing Compromise | Windows | A newly onboarded employee’s workstation exhibits unexpected activity shortly after opening an email attachment | Easy |
| macOS Infostealer Malware | macOS | Further analysis of a developer system reveals external downloads, script execution, and file activity inconsistent with prior findings | Medium |
| Windows Ransomware Intrusion | Windows | A workstation displays signs of system compromise and abnormal file behavior consistent with a potential ransomware event, requiring full incident reconstruction | Hard |

Each case is self-contained and includes its own background, investigation questions, and answer validation. The cases are intended to be completed in order, with each introducing additional complexity in both artifacts and analysis.

**Note:** The platform labels (macOS, Windows) refer to the system the artifacts were extracted from. All cases can be completed on macOS, Windows, or Linux.

## Investigation Process

Start by opening a case directory and reading the provided materials. From there, you will work directly with the artifacts in the `evidence/` folder.

A typical investigation involves:
- Exploring the available files and understanding their structure  
- Identifying which artifacts are relevant  
- Looking for patterns across multiple sources  
- Reconstructing a sequence of events  
- Supporting your conclusions with evidence
- Validating your results using the provided script

The emphasis is on producing conclusions that are clearly supported by evidence.

## What This Project Emphasizes

These cases are designed to build core DFIR skills:
- Thinking critically about what data matters  
- Correlating activity across different artifacts  
- Recognizing when individual actions form a larger pattern  
- Producing conclusions that are clearly supported by evidence  

The goal is not just to find answers, but to understand how those answers are derived.

## Purpose

This platform is intended for anyone who wants to practice forensic investigation in a structured but self-guided way. It is especially useful for students and self-learners who may not have access to dedicated DFIR coursework, as well as for anyone looking to strengthen their analytical approach to security incidents.
