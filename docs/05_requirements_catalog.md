# Requirements Catalog

## 1. Purpose

This document defines the business, functional, non-functional, data, reporting, and control requirements for the payment exception management workflow.

Each requirement is assigned a unique ID to support traceability across user stories, business rules, UAT test cases, and controls.

## 2. Requirements categories

| Category                   | Description                                                             |
|----------------------------|-------------------------------------------------------------------------|
| Business Requirement       | High-level business need or objective                                   |
| Functional Requirement     | Specific system or workflow capability                                  |
| Non-Functional Requirement | Performance, usability, auditability, or reliability expectation        |
| Data Requirement           | Required data field, data quality rule, or data structure               |
| Reporting Requirement      | Required operational or management reporting output                     |
| Control Requirement        | Requirement designed to reduce operational risk or support auditability |

## 3. Business Requirements

| Requirement ID | Requirement                                                               | Priority    | Rationale                                                  |
|----------------|---------------------------------------------------------------------------|-------------|------------------------------------------------------------|
| BRQ-001        | The process must provide a single source of truth for payment exceptions. | Must Have   | Reduces fragmented tracking across emails and spreadsheets |
| BRQ-002        | The process must support clear ownership of each open payment exception.  | Must Have   | Prevents unassigned or duplicated investigation work       |
| BRQ-003        | The process must support consistent exception categorization.             | Must Have   | Enables reporting, prioritization, and root cause analysis |
| BRQ-004        | The process must provide SLA and aging visibility.                        | Must Have   | Supports timely resolution and escalation                  |
| BRQ-005        | The process must support escalation of high-priority and aged exceptions. | Must Have   | Reduces operational and customer-impact risk               |
| BRQ-006        | The process must provide an audit trail for investigation and closure.    | Must Have   | Supports operational control and review evidence           |
| BRQ-007        | The process must support management reporting.                            | Should Have | Reduces manual reporting effort and improves visibility    |

## 4. Functional requirements

| Requirement ID | Requirement                                                                                                                 | Priority    | Notes                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|-------------|-------------------------------------------------------|
| FR-001         | The workflow shall allow a user to create a new payment exception case.                                                     | Must Have   | Case creation may be manual in MVP                    |
| FR-002         | The workflow shall assign each exception a unique case ID.                                                                  | Must Have   | Required for tracking and audit trail                 |
| FR-003         | The workflow shall capture payment reference, payment date, amount, currency, payment channel, and exception source.        | Must Have   | Core payment identification fields                    |
| FR-004         | The workflow shall allow a user to select an exception type from a controlled list.                                         | Must Have   | Support standardization                               |
| FR-005         | The workflow shall support the following statuses: New, In Review, Pending External Response, Escalated,  Resolved, Closed. | Must Have   | Supports status lifecycle                             |
| FR-006         | The workflow shall allow a case owner to be assigned.                                                                       | Must Have   | Supports ownership                                    |
| FR-007         | The workflow shall allow users to update case priority.                                                                     | Must Have   | Priority may be system-suggested or manually adjusted |
| FR-008         | The workflow shgall calculate the SLA due date based on priority and created date.                                          | Must Have   | Supports SLA monitoring                               |
| FR-009         | The workflow shall identify cases that have breached SLA.                                                                   | Must Have   | Supports escalation and reporting                     |
| FR-010         | The workflow shall identify aged cases based on aging rules.                                                                | Must Have   | Supports operational controls                         |
| FR-011         | The workflow shll allow users to add investigation ntoes.                                                                   | Must Have   | Supports audit trail                                  |  
| FR-012         | The workflow shall allow a case to be escalated.                                                                            | Must Have   | Supports manager or control review                    |
| FR-013         | The workflow shall require a closure reason before a case can be closed.                                                    | Must Have   | Prevents unsupported closure                          |
| FR-014         | The workflow shall prevent a case from moving directly from New to Closed.                                                  | Should Have | Enforces status lifecycle discipline                  |
| FR-015         | The workflow shall allow filtering by status, priority, owner, exception type, payment channel, and SLA breach flag.        | Should Have | Supports analyst queue management                     |
| FR-016         | The workflow shall allow users to view a case history.                                                                      | Should Have | Supports audit trail and handover                     |
| FR-017         | The workflow shall allow team leads to view unassigned cases.                                                               | Should Have | Supports workload management                          |
| FR-018         | The workflow shall allow team leads to view escalated cases.                                                                | Should Have | Supports escalation oversight                         |

## 5. Non-functional requirements

| Requirement ID | Requirement                                                                                  | Priority    | Notes                                |
|----------------|----------------------------------------------------------------------------------------------|-------------|--------------------------------------|
| NFR-001        | The workflow should be simple enough for operations users to use without technical support.  | Must Have   | Usability is critical for adoption   |
| NFR-002        | The workflow should support clear and consistent field labels.                               | Must Have   | Reduces data entry errors            |
| NFR-003        | The workflow should retain case history for audit and review.                                | Must Have   | Supports control evidence            |
| NFR-004        | The workflow should allow daily operational review without manual spreadsheet consolidation. | Should Have | Reduces manual reporting             |
| NFR-005        | The workflow should support export of exception data for analysis.                           | Should Have | Supports reporting and ad hoc review |
| NFR-006        | The workflow should be designed so additional exception types can be added later.            | Could Have  | Supports future scalability          |

## 6. Data requirements

| Requirement ID | Field/Data Requirement | Priority    | Notes                                                           |
|----------------|----------------------- |-------------|-----------------------------------------------------------------|
| DR-001         | Case ID                | Must Have   | Unique identifier                                               |
| DR-002         | Payment Reference      | Must Have   | Internal or external payment reference                          |
| DR-003         | Payment Date           | Must Have   | Used for investigation and aging                                |
| DR-004         | Amount                 | Must Have   | Used for prioritization and risk review                         |
| DR-005         | Currenct               | Must Have   | Supports payment identification                                 |
| DR-006         | Payment Channel        | Must Have   | Examples: Bank Transfer, Card, Wallet, PSP                      |
| DR-007         | Exception Source       | Must Have   | Examples: Bank File, PSP Report, Reconciliation, Customer Query |
| DR-008         | Exception Type         | Must Have   | Controlled taxonomy                                             |
| DR-009         | Status                 | Must Have   | Controlled lifecycle                                            |
| DR-010         | Priority               | Must Have   | Low, Medium, High, Critical                                     | 
| DR-011         | Owner                  | Must Have   | Assigned analyst or team queue                                  |
| DR-012         | Created Date           | Must Have   | Used for SLA and aging                                          |
| DR-013         | SLA Due Date           | Must Have   | Calculated field                                                |
| DR-014         | SLA Breach Flag        | Must Have   | Calculated field                                                | 
| DR-015         | Aging Bucket           | Should Have | Used for reporting                                              |
| DR-016         | Escalation Flag        | Should Have | Used for escalation reporting                                   |
| DR-017         | Investigation Notes    | Must Have   | Required for audit trail                                        | 
| DR-018         | Closure Reason         | Must Have   | Required before closure                                         |
| DR-019         | Closed Date            | Should Have | Used for resolution reporting                                   | 
| DR-020         | Root Cause             | Should Have | Used for trend analysis                                         |

## 7. Reporting requirements 

| Requirement ID | Requirement                                                        | Priority    | Notes                                |
|----------------|--------------------------------------------------------------------|-------------|--------------------------------------|
| RR-001         | The workflow shall provide a count of open exceptions by status.   | Must Have   | Daily operations control             |
| RR-002         | The workflow shall provide a count of open exceptions by priority. | Must Have   | Workload prioritization              |
| RR-003         | The workflow shall provide aged exception reporting.               | Must Have   | SLA and control monitoring           |
| RR-004         | The workflow shall provide SLA breach reporting.                   | Must Have   | Escalation and management visibility |
| RR-005         | The workflow shall provide exception type breakdown.               | Should Have | Root cause visibility                |
| RR-006         | The workflow shall provide payment channel breakdown.              | Should Have | Channel performance visibility       |
| RR-007         | The workflow shall provide owner workload reporting.               | Should Have | Team lead workload management        |
| RR-008         | The workflow shall provide closure reason reporting.               | Could Have  | Helps identify recurring causes      | 
| RR-009         | The workflow shall provide weekly management summary metrics.      | Should Have | Senior stakeholder reporting         | 

## 8. Control requirements 

| Requirement ID | Requirement                                                        | Priority    | Risk addressed                     |
|----------------|--------------------------------------------------------------------|-------------|------------------------------------|
| CR-001         | A case cannot be closed without a closure reason.                  | Must Have   | Unsupported case closure           |
| CR-002         | A case cannot be closed without investigation notes.               | Must Have   | Weak audit trail                   |
| CR-003         | High-priority cases must be visible in a dedicated view or report. | Must Have   | Delayed escalation                 | 
| CR-004         | SLA-breached cases must be flagged                                 | Must Have   | Missed SLA breach                  |
| CR-005         | Aged cases must be reported.                                       | Must Have   | Long-running unresolved exceptions |
| CR-006         | Unassigned cases must be visible to team leads.                    | Should Have | Lack of ownership                  |
| CR-007         | Status changes should be retained in case history.                 | Should Have | Weak audit trail                   |
| CR-008         | Manual priority changes should be recorded.                        | Could Have  | Inconsistent prioritization        |