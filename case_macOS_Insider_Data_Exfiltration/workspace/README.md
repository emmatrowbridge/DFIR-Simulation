# Workspace Guide

This directory contains the files you will use to record your findings during the investigation.

---
## Workflow

### Step 1 — Analyze the Evidence

Begin by examining the artifacts in the `evidence/` directory.

Focus on:

* Filesystem structure
* Browser activity
* Relationships between artifacts

Not all artifacts are relevant. Your goal is to identify meaningful patterns.

---
### Step 2 — Build a Timeline (Recommended)

Use:
```
timeline_template.csv
```
to organize events into a sequence.


The timeline is not graded, but it is the most effective way to:
* Understand what happened
* Correlate multiple artifacts
* Answer the investigation questions

---
## How to Build the Timeline

Each row should represent a meaningful event.

Include:
* What happened
* Which artifact supports it
* Why the artifact supports your conclusion

### Important Notes

* Filesystem artifacts do **not include full timestamp metadata**
* Most timestamps come from **browser artifacts**
* Some steps must be **inferred through correlation**

You are expected to:
* Combine multiple artifacts
* Use logical reasoning
* Support conclusions with evidence

---
### What to Look For

Examples of relevant events:
* Presence of sensitive files
* Files appearing in multiple directories
* Creation or presence of a staging directory
* Browser access to external services
* Activity that connects local files to external interaction

---
### Tips

* Focus on **important events**, not everything
* Look for **relationships between files and directories**
* Correlate filesystem activity with browser activity
* Avoid assumptions not supported by evidence

---
### Common Mistakes

* Treating all files as equally important
* Ignoring duplicated files across directories
* Relying on only one artifact
* Assuming intent without evidence

---
### Step 3 — Complete Your Answers

Use:
```
answers_template.json
```

Steps:
1. Copy this file to `answers.json`
2. Fill in all required fields
3. Use exact values from the artifacts where applicable

---
### Answer Guidelines

* All answers must be supported by evidence
* Use exact file names, paths, and values
* Some questions require combining multiple sources

---
### Step 4 — Run Validation

Run:
```
python validation/check_answers.py
```

This will check your answers for correctness.

---
## Final Goal

By the end of this process, you should be able to:
* Reconstruct a clear sequence of events
* Explain how artifacts relate to each other
* Support your conclusions with evidence
* Answer all investigation questions confidently

---

A strong investigation is not about finding a single clue—it is about connecting multiple pieces of evidence into a coherent explanation.
