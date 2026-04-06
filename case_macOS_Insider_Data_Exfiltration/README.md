# DFIR Simulation Platform
**Developers:** Emma Trowbridge and Cam Zabroski

## macOS Insider Data Exfiltration

---
## Overview

This case simulates a digital forensics and incident response (DFIR) investigation involving potential insider data exfiltration on a macOS system.

You are provided with a curated set of forensic artifacts extracted from a company-issued device. Your objective is to analyze the evidence, reconstruct what occurred, and produce evidence-based conclusions.

This is an **introductory-level (easy)** case. The scenario is intentionally structured to be clear and focused, allowing you to develop core DFIR skills such as artifact analysis, timeline reconstruction, and correlation of events.

---
## Scenario Summary

A company employee’s system has been flagged for unusual activity shortly after submitting their resignation. The behavior involves access to internal files and interaction with external services.

No conclusions have been made.

Your role is to investigate what happened using the available evidence.

---
## Repository Structure

```
case_macOS_insider_data_exfiltration/
│
├── README.md (you are here!)
├── case_brief.md
├── investigation_questions.md
│
├── evidence/
│   ├── BrowserArtifacts/
│   │   ├── chrome_history.csv
│   │   └── cookies.csv
│   │
│   └── FileSystem/
│       ├── Desktop/
│       │   ├── meeting_notes.txt
│       │   └── todo.md
│       │
│       ├── Documents/
│       │   ├── Notes/
│       │   │   └── ideas.txt
│       │   │
│       │   ├── Personal/
│       │   │   └── journal.txt
│       │   │
│       │   └── archive/
│       │       ├── api_keys.txt
│       │       ├── customer_data.csv
│       │       └── internal_roadmap.pdf
│       │
│       └── Projects/
│           ├── alp-app/
│           │   ├── app.py
│           │   └── test.sh
│           │
│           └── internal-tools/
│               ├── api_keys.txt
│               ├── customer_data.csv
│               └── internal_roadmap.pdf
│
├── workspace/
│   ├── answers_template.json
│   ├── timeline_template.csv
│   └── timeline_template_notes.txt
│
└── validation/
    └── check_answers.py
```

---
## What You Are Given

### Browser Artifacts

Located in:

```
evidence/BrowserArtifacts/
```

Includes:

* Chrome browsing history
* Cookies

These artifacts help identify:

* External services accessed
* Timing of browser activity

---
### Filesystem Artifacts

Located in:

```
evidence/FileSystem/
```

These artifacts represent a reconstructed view of the user’s filesystem based on files extracted from the disk image.

They include:

* Desktop files
* Documents (including user-created directories)
* Project directories and internal files

These are files recovered from the system and organized to reflect the original directory structure.

---
### Important Note on Filesystem Data

These files are **not full forensic exports** and may not include complete metadata such as:

* Precise access timestamps
* Full MAC time history
* Low-level filesystem artifacts

Instead, the filesystem evidence in this case is intended to help you:

* Identify which files exist and where
* Understand relationships between directories
* Recognize staging or duplication of files
* Provide context for user activity

You will need to rely on **combining filesystem structure with browser activity** to reconstruct events.

---
## Your Objective

You are acting as a forensic analyst.

Your task is to:

1. Examine the provided artifacts
2. Identify relevant activity
3. Reconstruct a timeline of events
4. Answer all investigation questions
5. Ensure every conclusion is supported by evidence

You should expect to combine multiple artifacts to answer most questions rather than relying on a single source.

---
## Investigation Approach

This case is **artifact-driven**, not tool-driven.

You may use any approach you prefer, including:

* Manual inspection
* Spreadsheet analysis
* Scripting (e.g., Python)

To successfully complete the case, you will need to:

* Analyze filesystem structure and file relationships
* Identify duplicated or staged files across directories
* Examine browser history for external activity
* Correlate filesystem state with browser events
* Reconstruct a logical sequence of actions

Note: Because filesystem metadata is intentionally limited, **timeline reconstruction will depend heavily on browser artifacts and logical inference based on file placement and duplication**. In this case, timestamps are primarily derived from browser artifacts rather than filesystem metadata.

---
## Workspace Files

The `workspace/` directory contains templates you will use to record your findings.

### Required

* `answers_template.json`
  This file contains the structured format for answering the investigation questions.
  You must complete this file before running validation.

---
### Strongly Recommended

* `timeline_template.csv`
  Use this file to build a timeline of events.
  This will help you organize findings and support your answers.

* `timeline_template_notes.txt`
  Provides guidance on how to construct a timeline, including:

  * What types of events to include
  * How to correlate artifacts
  * How to document supporting evidence

---
### Important

* Only `answers_template.json` is checked by the validation script
* The timeline files are for your analysis process
* A well-constructed timeline will make this case significantly easier

---
## Answer Requirements

All answers must:

* Be directly supported by evidence
* Match artifact data exactly (file names, paths, and values present in the artifacts)
* Avoid assumptions not backed by observable data

If an answer cannot be supported by the provided artifacts, it should not be included.

---
## Validation

After completing your answers, run:

```bash
python validation/check_answers.py
```

The validation system will:

* Check each answer for correctness
* Indicate correct vs incorrect responses

The validation system will NOT:

* Provide hints
* Reveal correct answers
* Partially credit responses

---
## Important Guidelines

* Not all artifacts are relevant
* Background activity is intentionally included
* Some conclusions require correlating multiple artifacts
* The absence of expected activity can be meaningful
* Do not assume malicious intent without evidence

This investigation focuses on **what happened**, not speculation.

---
## Learning Goals

By completing this case, you will:

* Identify and interpret common forensic artifacts
* Correlate filesystem and browser activity
* Reconstruct a clear investigative timeline
* Produce defensible, evidence-based conclusions

---
## Getting Started

1. Read `case_brief.md`
2. Review `investigation_questions.md`
3. Begin analyzing the artifacts in `evidence/`
4. Record your findings in the workspace files

---
## Final Note

This case reflects how real investigations work:

Individual actions may appear normal in isolation.
Your task is to determine whether they form a meaningful pattern when correlated together.

---

Good luck.
