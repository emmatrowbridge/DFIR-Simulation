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
├── README.md
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
│   └── (your working files go here)
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

Includes:

* Desktop files
* Documents (including user-created directories)
* Project directories and internal files

These artifacts help identify:

* File access behavior
* File staging or copying
* Contextual user activity

---

## Your Objective

You are acting as a forensic analyst.

Your task is to:

1. Examine the provided artifacts
2. Identify relevant activity
3. Reconstruct a timeline of events
4. Answer all investigation questions
5. Ensure every conclusion is supported by evidence

---

## Investigation Approach

This case is **artifact-driven**, not tool-driven.

You may use any approach you prefer, including:

* Manual inspection
* Spreadsheet analysis
* Scripting (e.g., Python)

To successfully complete the case, you will need to:

* Analyze filesystem structure and file relationships
* Identify file access and staging behavior
* Examine browser history for external activity
* Correlate events across filesystem and browser artifacts
* Reconstruct a logical sequence of actions

---

## Answer Requirements

All answers must:

* Be directly supported by evidence
* Match artifact data exactly (file names, paths, timestamps)
* Avoid assumptions not backed by observable data

If an answer cannot be supported by the provided artifacts, it should not be included.

---

## Validation

After completing your answers, run:

```
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

---

## Final Note

This case reflects how real investigations work:

Individual actions may appear normal in isolation.
Your task is to determine whether they form a meaningful pattern when viewed together.

---

Good luck.
