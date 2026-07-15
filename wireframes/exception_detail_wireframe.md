# Payment Exception Detail Wireframe

## 1. Purpose

This document presents a conceptual wireframe for the payment exception detail view.

The detail view is used by Payments Operations Analysts and Team Leads to investigate, update, escalate, resolve, and close an individual payment exception case.

The wireframe is not a production user interface design. It ilustrates how documented requirements, business rules, data fields, controls, and audit evidence could be represented in a business-facing screen.

## 2. Primary users

* Payments Operations Analyst
* Payments Operations Team Lead
* Payments Operations Manager
* Risk/Operational Control reviewer

## 3. Main user objectives

The exception detail view should allow users to:

* review payment and exception details;
* update status, priority, ownership, and classification;
* review SLA and aging information;
* add investigation notes;
* record external follow-up;
* escalate the case;
* review case history;
* resolve and close the case;
* capture closure reason and resolution outcome.

## 4. Conceptual layout

```text
+--------------------------------------------------------------------------+
| PAYMENT EXCEPTION CASE                                                   |  
+--------------------------------------------------------------------------+
| CASE-000145                                                              |
| Bank Rejection | Critical | Escalated | SLA BREACHED                     |
+--------------------------------------------------------------------------+
| CASE SUMMARY                                                             |
| Owner: Analyst A                  Team Queue: Bank Transfers             |
| Created: 2025-01-15               Days open: 8                           |
| SLA Due: 2025-01-16               Escalation Owner: Team Lead            |
| Customer Impact: Yes              High Value: Yes                        |
+--------------------------------------------------------------------------+
| PAYMENT DETAILS                                                          |
| Payment Reference: PAY-98452                                             |
| Internal Payment ID: INT-PMT-98765                                       |
| External Payment ID: BNK-456781                                          |
| Payment Date: 2025-01-14          Value Date: 2025-01-15                 |
| Amount: 125,000.00                Currency: EUR                          |
| Payment Channel: Bank Transfer    Counterparty: ABC Supplier Ltd         |
+--------------------------------------------------------------------------+
| EXCEPTION DETAILS                                                        |
| Exception Type: Bank Rejection                                           |
| Exception Source: Bank File                                              |
| Rejection Reason: Invalid beneficiary account                            |
| Root Cause: [Not Confirmed ▾]                                            |
| Status: [Escalated ▾]             Priority: [Critical ▾]                 |                 
+--------------------------------------------------------------------------+
| SLA AND ESCALATION                                                       |
| SLA Status: BREACHED              Aging Bucket: 6-10 days                |
| Escalation Reason: High-value SLA breach                                 |
| Escalation Date: 2025-01-17       Escalation Owner: Team Lead            |
|                                                                          |
| [Escalate Case] [Update Escalation]                                      |
+--------------------------------------------------------------------------+
| INVESTIGATION NOTES                                                      |
| 2025-01-15 11:30 | Analyst A                                             |
| Bank rejection file confirmed invalid beneficiary account.               |
|                                                                          |
| 2025-01-16 14:10 | Analyst A                                             |
| Correct beneficiary details requested from internal payment team.        |
|                                                                          |
| [Add Investigation Note]                                                 |
+--------------------------------------------------------------------------+
| RESOLUTION AND CLOSURE                                                   |
| Resolution Outcome: [Select ▾]                                           |
| Closure Reason: [Select ▾]                                               |
| Closure Notes:                                                           |
| [                                                                      ] |
|                                                                          |
| [Mark Resolved] [Close Case]                                             |
+--------------------------------------------------------------------------+
| CASE HISTORY                                                             |
| 2025-01-15 09:10 | Case created                   | System               |
| 2025-01-15 09:25 | Statis: New -> In Review       | Analyst A            |
| 2025-01-15 09:30 | Priority: High -> Critical     | Analyst A            |
| 2025-01-17 10:15 | Status: In Review -> Escalated | Team Lead            |
+--------------------------------------------------------------------------+
| [Back to Queue]  [Save Changes]  [Export Case History]                   |
+--------------------------------------------------------------------------+
```

## 5. Header and case summary

The top section should provide an immediate summary of the case.

| Field            | Description                                        | Related requirement  |
|------------------|----------------------------------------------------|----------------------|
| Case ID          | Unique payment exception identifier                | FR-002, DR-001       |
| Exception Type   | Current exception classification                   | FR-004, DR-008       |
| Priority         | Current operational priority                       | FR-007, DR-010       |
| Status           | Current lifecycle status                           | FR-005, DR-009       |
| SLA Status       | Shows whether SLA is active, due, or breached      | FR-009, DR-014       |
| Owner            | Analyst responsible for the case                   | FR-006, DR-011       |
| Team Queue       | Operational queue responsible for the case         | FR-006               |
| Days Open        | Number of business days the case has remained open | DR_015               |
| Escalation Owner | Person or team responsible for escalation review   | FR-018               |
| Customer Impact  | Indicates customer or client impact                | customer_flag_impact |
| High Value       | Indicates whether the high-value threshold is met  | high_value_flag      |

## 6. Payment details section

The payment details section should provide enough information to identify the payment and support investigation.

| Field               | Description                                 | Editable?   |
|---------------------|---------------------------------------------|-------------|
| Payment Reference   | Internal or external payment reference      | Conditional |
| Internal Payment ID | Identifier from the internal payment system | Conditional |
| External Payment ID | Identifier from bank or PSP                 | Conditional |
| Payment Date        | Date when payment was initiated             | Conditional |
| Value Date          | Expected or actual settlement date          | Conditional |
| Amount              | Payment amount                              | Restricted  |
| Currency            | ISO payment currency                        | Restricted  |
| Payment Channel     | Payment processing channel                  | Conditional |
| Debtor Account      | Sending account                             | Restricted  |
| Creditor Account    | Receiving account                           | Restricted  |
| Counterparty Name   |Payment counterparty                         | Conditional |

Sensitive payment data should be displayed onle where required and according to access rules defined during implementation.

## 7. Exception details section

| Field                | Description                                | Related requirement |
|----------------------|--------------------------------------------|---------------------|
| Exception Type       | Controlled exception classification        | FR-004              |
| Exception Source     | Source where exception was identified      | DR-007              |
| Rejection Reason     | Bank, PSP, or system rejection information | FR-003              |
| Root Cause           | Confirmed cause after investigation        | DR-020              |
| Status               | Current case lifecycle status              | FR-005              |
| Priority             | Current operational priority               | FR-007              |
| Customer Impact Flag | Indicates customer impact                  | BR-021              |
| Duplicate Risk Flag  | Indicates potential duplicate payment      | BR-020              |
| High Value Flag      | Indicates material payment value           | BR-019              |

Controlled values should be used for exception type, status, priority, and root cause wherever possible.

## 8. Status controls

The detail screen should enforce the documented status lifecycle.

| Current status            | Available sctions                                         |
|---------------------------|-----------------------------------------------------------|
| New                       | Move to In Review                                         |
| In Review                 | Move to Pending External Response, Escalated, or Resolved |
| Pending External Response | Move to In Review or Escalated                            |
| Escalated                 | Move to In Review or Resolved                             |
| Resolved                  | Close case                                                |
| Closed                    | View only, unless controlled reopen process is introduced |

The screen should prevent:

* movenet directly from ```New``` to ```Closed```;
* closure without investigation notes;
* closure without closure reason;
* invalid status transitions;
* standard editing after cause closure.

## 9. SLA and aging section

| Field                   | Description                                          |
|-------------------------|------------------------------------------------------|
| Initial Review Due Date | Deadline for first review                            |
| SLA Due Date            | Target resolution date                               |
| SLA Breach Flag         | Indicates whether SLA has been breached              |
| Days Open               | Business days since case creation                    |
| Aging Bucket            | Current aging category                               |
| Aged Exception Flag     | Indicates whether case is older than 5 business days |

Suggested SLA indicators:

| SLA condition         | Display          |
|-----------------------|------------------|
| Within SLA            | ```WITHIN SLA``` |
| Due today             | ```DUE TODAY```  |
| Due next business day | ```DUE SOON```   |
| Breached              | ```BREACHED```   |
| Closed                | ```COMPLETED```  |

Color should not be the only indicator. Text labels should be included for accessibility and clarity.

## 10. Escalation section

The escalation section should support both initiation and review of escalated cases.

Required fields:

| Field                       | Requirement                                 |
|-----------------------------|---------------------------------------------|
| Escalation Flag             | Must identify whether the case is escalated |
| Escalation Reason           | Required when case is escalated             |
| Escalation Date             | Recorded automatically                      |
| Escalation Owner            | Person or team responsible for review       |
| Escalation Resolution Notes | Required before escalation is cleared       |

Example escalation reasons:

* Critical priority;
* High-value payment;
* SLA breach;
* aged High or Critical case;
* duplicate payment risk;
* customer impact;
* regulatory or compliance concern;
* external aprty delay;
* manager review requested.

## 11. Investigation notes

The investigation notes section should provide a chronological record of analyst activity.

Each note should include:

| Field                | Description                            |     
|----------------------|----------------------------------------|
| Note Date            | Date and time when note was added      |
| Note Author          | User who added the note                |
| Note Type            | Optional controlled category           |
| Note Content         | Investigation detail                   |
| Attachment Reference | Optional link or reference to evidence |

Suggested note types:

* Investigation update;
* External follow-up;
* Bank response;
* PSP response;
* Customer communication;
* Internal escalation;
* Resolution update;
* Control review.

Existing notes should not normally be editable after submission. Corrections should be addes as a new note to preserve the audit trail.

## 12. Resolution and closure

The resolution section should becoma available when the investigation outcome is known.

Required closure information:

| Field               | Required?               |
|---------------------|-------------------------|
| Status = Resolved   | Yes                     |
| Investigation Notes | Yes                     |
| Resolution Outcome  | Yes                     |
| Closure Reason      | Yes                     |
| Closure Notes       | Should Have             | 
| Closed Date         | Generated automatically |
| Closing User        | Generated automatically |

Suggested resolution outcomes:

* Payment settled;
* Payment reprocessed;
* Payment cancelled;
* Bank rejection resolved;
* PSP issue resolved;
* duplicate risk resolved;
* no action required;
* incorrect exception;
* external issue confirmed;
* internal process correction completed.

The ```Close Case``` action should remain disabled untill all mandatory closure conditions are met.

## 13. Case history

The case history should provide a chronological audit trail.

History should include:

* case creation;
* status changes;
* priority changes;
* owner changes;
* team queue changes;
* escalation actions;
* investigation notes;
* resolution updates;
* closure;
* reopen activity, if introduced.

Each history entry should include:

| Field          | Description                              |
|----------------|------------------------------------------|
| Timestamp      | Date and time of change                  |
| User           | User or system process making the change |
| Field/Action   | Item changed                             |
| Previous Value | Previous value where applicable          |
| New Value      | New value where applicable               |
| Reason         | Reason for change where required         |

## 14. Available actions

### Analyst actions

* Save changes;
* update status;
* update priority;
* assign or change owner;
* add investigation note;
* move case to Pending External Response;
* escalate case;
* mark case as Resolved;
* close case when requirements are met;
* return to exception queue.

### Team Lead actions

* assign or reassing case;
* change priority;
* review escalation;
* update escalation owner;
* request further investigaiton;
* confirm resolution;
* export case history.

### Restricted actions

The following actions should require additional permission or approval:

* reopena closed case;
* delete a case;
* edit historical notes;
* remove audit history;
* override SLA calculation;
* remove Critical priority without reason.

## 15. Validation messages

| Scenario                         | Suggested message                                                              | 
|----------------------------------|--------------------------------------------------------------------------------|
| Missing required payment details | ```Complete all mandatory payment fields before starting the investigation.``` |
| Invalid status transition        | ``` This status transition is not allowed.```                                  |
| Missing investigation notes      | ```Add investigation notes before resolving or closing the case.```            |
| Missing escalation reason        | ```Select an escalation reason before escalating the case.```                  |
| Missing owner                    | ```Assign an owner or team queue before continuing.```                         |
| Closed case editing attempt      | ```Closed cases cannot be edited without an approved reopen process.```        |

## 16. Empty and error states

| Scenario                       | Expected behavior                                              |
|--------------------------------|----------------------------------------------------------------|
| Case ID not found              | Display clear case-not-found message                           |
| Payment data unavailable       | Display warning and allow data quality escalation              |
| Case history unabailable       | Display audit history warning                                  |
| Save fails                     | Preserve entered data and display error                        |
| External reference unavailable | Allow case to continue with internal reference where permitted |
| Report export fails            | Display error without changing case data                       |

## 17. Related requirements

The wireframe supports:

* FR-003: Capture payment details
* FR-004: Select controlled exception type
* FR-005: Manage status lifecycle
* FR-006: Assign case owner
* FR-007: Update priority
* FR-008: Calculate SLA due date
* FR-009: Identify SLA breaches
* FR-010: Identify aged cases
* FR-011: Add investigation notes
* FR-012: Escalate case
* FR-013: Require closure reason
* FR-014: Prevent invalid direct closure
* FR-016: View case history
* CR-001: Closure reason control
* CR-002: Investigation note control
* CR-007: Audit history retention
* CR-008: Priority change history

## 18. Minimum Viable Product scope

The Minimum Viable Product version should includ:

* case summary;
* payment details;
* exception classification;
* status and priority updates;
* owner assignment;
* SLA and aging information;
* investigation notes;
* escalation fields;
* resolution and closure controls;
* basic case history.

Future enhancements may include:

* file attachments;
* comments and mentions;
* automated bank or PSP status updates;
* external communication templates;
* configurable workflow rules;
* case reopen process;
* linked reconciliation breaks;
* linked customer support cases;
* automatic duplicate detection.

## 19. Summary

The Payment Exception Detail wireframe translates case management requirement into a structured investigation and control view.

It supports payment identification, exception classification, ownership, SLA monitoring, escalation,m investigation history, resolution, closure controls, and audit evidence.