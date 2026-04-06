# Case Brief: macOS Insider Data Exfiltration

---
## Background

Applied Logic Platforms (ALP) is a SaaS company that develops internal developer tooling and customer workflow automation software. 

Engineers have access to internal documentation, API credentials, and limited customer data for testing purposes.

ALP maintains centralized monitoring and alerting capabilities, but developer systems—particularly travel laptops—are not fully locked down. These systems allow flexibility for development workflows, including browser access and cloud services, even if not all services are strictly restricted.

---
## Situation

An employee, **Jason Wang**, recently submitted his two-week resignation notice.

Shortly after, the security team observed **unusual activity** associated with his account over the weekend.

This activity included:

* Access patterns outside normal working hours
* Interaction with external, cloud-based services
* A login to a Google account from an unfamiliar IP address

Due to the timing and context, this activity has been flagged for review.

---
## System Information

* Hostname: alp-macbook-jwang
* Operating System: macOS
* User: jwang

This system is a company-issued developer laptop used for both work-related and limited personal activity.

---
## Account Context

The user operates with multiple accounts accessible from the same system:

* A **work-related account** used for development activity
* A **personal account** accessible within the same browser

This configuration allows multiple accounts to be active within a single browser session.

---
## Investigation Scope

You have been provided with forensic artifacts extracted from Jason’s system.

Your task is to determine:

* What activity occurred on the system
* Whether any internal data was accessed or moved
* Whether the observed behavior is consistent with normal usage or something more concerning

---
## Important Notes

* The user has legitimate access to the files on this system
* No assumptions should be made about intent
* All conclusions must be based on observable evidence

This investigation focuses on **what happened**, not why.

---
## Objective

Analyze the provided artifacts and reconstruct a **clear, evidence-supported sequence of events**.
