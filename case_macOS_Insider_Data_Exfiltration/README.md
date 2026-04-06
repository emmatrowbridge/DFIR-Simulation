# DFIR Simulation Platform
**By:** Emma Trowbridge and Cam Zabroski

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
├── case_brief.md
├── investigation_questions.md
│
├── evidence/
│   ├── artifacts/
│   │   ├── browser/
│   │   │   ├── chrome_history.csv
│   │   │   └── cookies.csv
│   │   │
│   │   └── filesystem/
│   │       ├── Desktop/
│   │       ├── Documents/
│   │       └── Projects/
│   │
│   └── disk_image/
│       └── (full disk image - optional)
│
├── workspace/
│   ├── answers_template.json
│   └── timeline_template.csv
│
├── validation/
│   └── check_answers.py
│
└── tools/
    └── (analysis environment and setup instructions)
```

---

## What You Are Given

### Artifacts (Primary Evidence)

You will primarily work with extracted artifacts, including:

* **Browser Data**

  * Chrome browsing history
  * Cookies

* **Filesystem Data**

  * Desktop files
  * Documents directory
  * Project directories

These artifacts contain the key evidence needed to complete the investigation.

---

### Disk Image (Optional)

A full disk image may also be included for advanced analysis.
However, this case is designed to be solved using the provided artifacts alone.

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
* DFIR tools (optional)

To successfully complete the case, you will need to:

* Analyze filesystem structure and file metadata
* Identify file access and staging behavior
* Examine browser history for external interactions
* Correlate activity across multiple data sources
* Reconstruct a logical sequence of events

---

## Workspace Files

You will record your findings using the provided workspace templates.

### Required

* `answers_template.json`

  * Contains structured answers to investigation questions
  * This file is used for validation

### Recommended

* `timeline_template.csv`

  * Used to organize events chronologically
  * Helps support your conclusions
  * Not automatically graded, but strongly recommended

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
3. Begin analyzing the artifacts in `evidence/artifacts/`
4. Record your findings in the workspace files

---

## Final Note

This case is designed to reflect how real investigations work:

Individual actions may appear normal in isolation.
Your task is to determine whether they form a meaningful pattern when viewed together.

---

Good luck.
