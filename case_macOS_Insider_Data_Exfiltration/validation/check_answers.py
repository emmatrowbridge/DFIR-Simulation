#!/usr/bin/env python3
"""
DFIR Simulation Platform - Answer Validation Script
Case: macOS Insider Data Exfiltration

Expected student workflow:
1. Copy workspace/answers_template.json to workspace/answers.json
2. Fill in workspace/answers.json
3. Run this script from the case root:
       python validation/check_answers.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterable


ANSWERS_PATH = Path("workspace/answers.json")

EXPECTED_FIELDS = [
    "q1_internal_tools_files",
    "q2_staging_directory",
    "q3_duplicated_files",
    "q4_application_used",
    "q5_external_service",
    "q6_multiple_accounts_evidence",
    "q7_sequence_of_actions",
    "q8_incident_type",
]

EXPECTED_Q1_FILES = {
    "api_keys.txt",
    "customer_data.csv",
    "internal_roadmap.pdf",
}

EXPECTED_Q2_STAGING_DIR = "/Users/jwang/Documents/archive"

EXPECTED_Q3_DUPLICATED_FILES = {
    "api_keys.txt",
    "customer_data.csv",
    "internal_roadmap.pdf",
}

EXPECTED_Q4_APP = "google chrome"
EXPECTED_Q5_SERVICE = "google drive"
EXPECTED_Q8_INCIDENT = "insider data exfiltration"


def load_answers(path: Path) -> dict[str, Any]:
    if not path.exists():
        print(f"[ERROR] Could not find answers file: {path}")
        print("Copy workspace/answers_template.json to workspace/answers.json,")
        print("complete it, then run this script again.")
        sys.exit(1)

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {path}: {e}")
        sys.exit(1)

    if not isinstance(data, dict):
        print("[ERROR] answers.json must contain a top-level JSON object.")
        sys.exit(1)

    return data


def normalize_string(value: Any) -> str:
    if value is None:
        return ""
    return " ".join(str(value).strip().split()).lower()


def normalize_path(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip().replace("\\", "/")
    while "//" in text:
        text = text.replace("//", "/")
    return text.rstrip("/") if text != "/" else text


def normalize_list_of_strings(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    result = []
    for item in value:
        if isinstance(item, str):
            cleaned = item.strip()
            if cleaned:
                result.append(cleaned)
    return result


def normalize_filename_set(value: Any) -> set[str]:
    return {item.strip() for item in normalize_list_of_strings(value)}


def check_required_fields(data: dict[str, Any]) -> list[str]:
    return [field for field in EXPECTED_FIELDS if field not in data]


def validate_q1(value: Any) -> tuple[bool, str]:
    actual = normalize_filename_set(value)
    if actual == EXPECTED_Q1_FILES:
        return True, "Correct."
    return False, "Expected the exact set of files present in internal-tools."


def validate_q2(value: Any) -> tuple[bool, str]:
    actual = normalize_path(value)
    expected = normalize_path(EXPECTED_Q2_STAGING_DIR)
    if actual == expected:
        return True, "Correct."
    return False, "Expected the full staging directory path."


def validate_q3(value: Any) -> tuple[bool, str]:
    actual = normalize_filename_set(value)
    if actual == EXPECTED_Q3_DUPLICATED_FILES:
        return True, "Correct."
    return False, "Expected the exact set of duplicated files."


def validate_q4(value: Any) -> tuple[bool, str]:
    actual = normalize_string(value)
    if actual == EXPECTED_Q4_APP:
        return True, "Correct."
    return False, "Expected the application used to access the external service."


def validate_q5(value: Any) -> tuple[bool, str]:
    actual = normalize_string(value)
    if actual == EXPECTED_Q5_SERVICE:
        return True, "Correct."
    return False, "Expected the external service accessed."


def contains_any(text: str, keywords: Iterable[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def validate_q6(value: Any) -> tuple[bool, str]:
    if isinstance(value, list):
        text = " ".join(str(v) for v in value)
    else:
        text = str(value)

    norm = normalize_string(text)

    has_multiple = (
        "multiple account" in norm
        or "two account" in norm
        or "more than one account" in norm
        or ("account" in norm and ("accounts" in norm or "multiple" in norm or "two" in norm))
    )

    has_context = contains_any(
        norm,
        [
            "google",
            "chrome",
            "browser",
            "drive",
            "history",
            "cookie",
            "cookies",
            "account",
        ],
    )

    if has_multiple and has_context:
        return True, "Correct."

    return False, "Answer should explain that the browser artifacts suggest multiple accounts were in use."


def validate_q7(value: Any) -> tuple[bool, str]:
    if isinstance(value, list):
        items = [str(v).strip() for v in value if str(v).strip()]
        combined = " ".join(items)
        has_multiple_steps = len(items) >= 3
    else:
        combined = str(value)
        has_multiple_steps = False

    norm = normalize_string(combined)

    local_activity = contains_any(
        norm,
        [
            "internal file",
            "internal-tools",
            "local file",
            "sensitive file",
            "accessed files",
            "files",
        ],
    )

    staging_activity = contains_any(
        norm,
        [
            "stage",
            "staging",
            "archive",
            "copied",
            "copy",
            "duplicate",
            "duplicated",
        ],
    )

    external_activity = contains_any(
        norm,
        [
            "google drive",
            "drive",
            "cloud",
            "external service",
            "browser",
            "chrome",
            "uploaded",
            "transfer",
            "interaction",
        ],
    )

    sequence_language = contains_any(
        norm,
        [
            "then",
            "next",
            "after",
            "followed by",
            "sequence",
            "first",
            "finally",
            "before",
        ],
    ) or has_multiple_steps

    if local_activity and staging_activity and external_activity and sequence_language:
        return True, "Correct."

    return False, (
        "Answer should reconstruct a sequence from local/internal file activity, "
        "to staging/copying, to browser-based external interaction."
    )


def validate_q8(value: Any) -> tuple[bool, str]:
    actual = normalize_string(value)
    if actual == EXPECTED_Q8_INCIDENT:
        return True, "Correct."
    return False, "Expected the incident type best supported by the evidence."


VALIDATORS = {
    "q1_internal_tools_files": validate_q1,
    "q2_staging_directory": validate_q2,
    "q3_duplicated_files": validate_q3,
    "q4_application_used": validate_q4,
    "q5_external_service": validate_q5,
    "q6_multiple_accounts_evidence": validate_q6,
    "q7_sequence_of_actions": validate_q7,
    "q8_incident_type": validate_q8,
}


def main() -> None:
    answers = load_answers(ANSWERS_PATH)

    missing_fields = check_required_fields(answers)
    if missing_fields:
        print("[ERROR] answers.json is missing required field(s):")
        for field in missing_fields:
            print(f"  - {field}")
        sys.exit(1)

    total = len(EXPECTED_FIELDS)
    correct = 0

    print("DFIR Simulation Platform - Validation Results")
    print("Case: macOS Insider Data Exfiltration")
    print("-" * 55)

    for field in EXPECTED_FIELDS:
        validator = VALIDATORS[field]
        is_correct, message = validator(answers.get(field))
        status = "CORRECT" if is_correct else "INCORRECT"
        print(f"{field}: {status}")
        print(f"  {message}")
        if is_correct:
            correct += 1

    print("-" * 55)
    print(f"Score: {correct}/{total} correct")

    if correct == total:
        print("All answers are correct.")
    else:
        print("Some answers are incorrect. Review the evidence and try again.")


if __name__ == "__main__":
    main()
