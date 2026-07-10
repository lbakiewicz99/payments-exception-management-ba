# Data Dictionary

## 1. Purpose

This document defines the key data fields required for the payment exception management workflow.

The data dictionary supports consistent case creation, investigation, prioritization, SLA tracking, escalation, closure, reporting, and audit review.

It is intended to help business stakeholders, product teams, technology teams, QA, reporting teams, and UAT users udnerstand what each means and how it should be used. 

## 2. Data dictionary conventions

| Attribute            | Description                             |
|----------------------|-----------------------------------------|
| Field name           | Proposed system or reporting field name |
| Business name        | Business-friendly field label           |
| Description          | Explanation of the field                |
| Data type            | Expected data format                    |
| Required?            | Wheter the field is mandatory           |
| Source               | Where the value comes from              |
| Example              | Example value                           |
| Related requirements | Requirement IDs linked to the field     |

## 3. Core case fields

| Field name        | Business name     | Description                                                                   | Data type      | Required?          | Source                           | Example                   | Related requirement |
|-------------------|-------------------|-------------------------------------------------------------------------------|----------------|--------------------|----------------------------------|---------------------------|---------------------|
| case_id           | Case ID           | Unique identifier assigned to each payment exception case                     | Text/ID        | Yes                | Workflow generated               | CASE-2025-000001          | DR-001, FR-002      |
| case_title        | Case Title        | Short description of the payment exception                                    | Text           | Should Have        | User entered/system suggested    | High-value bank rejection | FR-001              |
| created_date      | Created Date      | Date when the case was created                                                | Date           | Yes                | Workflow generated               | 15-01-2025                | DR-012              |
| created_by        | Created BY        | User or process that created the case                                         | Text           | Should Have        | Workflow generated               | analyst01                 | NFR-003             |
| last_updated_date | Last Updated Date | Date when the case was last updated                                           | Date/Timestamp | Should Have        | Workflow generated               | 16-01-2025 14:30          | FR-016              |
| last_updated_by   | Last Updated By   | User or process that last updated the case                                    | Text           | Should Have        | Workflow generated               | analyst02                 | FR-016              |
| owner             | Owner             | Analyst or team queue responsible for the case                                | Text           | Yes for open cases | User selected/team lead assigned | Payments Analyst A        | DR-011, FR-006      |
| team_queue        | Team Queue        | Operational queue responsible for the case if no individual owner is assigned | Text           | Conditional        | User selected/workflow assigned  | Card Payments Queue       | FR-006, CR-006      |

## 4. Payment identification fields

| Field name          | Business name       | Description                                                                   | Data type      | Required?          | Source                           | Example                     | Related requirement |
|---------------------|---------------------|-------------------------------------------------------------------------------|----------------|--------------------|----------------------------------|-----------------------------|---------------------|
| payment_reference   | Payment Reference   | Internal or external reference used to identify the payment                   | Text           | Yes                | Payment system/bank/PSP          | PAY-2025-000456             | DR-002              |
| internal_payment_id | Internal Payment ID | Internal system identifier for the payment                                    | Text           | Should Have        | Internal payment system          | INT-PMT-98765               | DR-002              |
| external_payment_id | External Payment ID | External bank or PSP identifier for the payment                               | Text           | Should Have        | Bank/PSP                         | PSP-ABC-123456              | DR-002              |
| payment_date        | Payment Date        | Date when the payment was initiated or expected                               | Date           | Yes                | Payment system/bank/PSP          | 14-01-2025                  | DR-003              |
| value_date          | Value Date          | Date when funds are expected to settle or become available                    | Date           | Conditional        | Bank/payment system              | 15-01-2025                  | RR-006              |
| amount              | Amount              | Payment amount                                                                | Decimal        | Yes                | Payment system/bank/PSP          | 125000.00                   | DR-004              |
| currency            | Currency            | Payment currency using ISO currency code                                      | Text           | Yes                | Payment system/bank/PSP          | EUR                         | DR-005              |
| debtor_account      | Debtor Account      | Account from which the payment is sent                                        | Text           | Could Have         | Payment system/bank              | DE89370400440532013000      | DR-002              |
| creditor_account    | Creditor Account    | Account to which the paymenty is sent                                         | Text           | Could Have         | Payment system/bank              | FR7630006000011234567890189 | DR-002              |
| counterparty_name   | Counterparty Name   | Name of the payment counterparty                                              | Text           | Could Have         | Payment system/bank/PSP          | ABC Supplier Ltd            | DR-002              |

## 5. Exception classification fields

| Field name           | Business name        | Description                                                                    | Data type             | Required?          | Source                           | Example                       | Related requirement |
|----------------------|----------------------|--------------------------------------------------------------------------------|-----------------------|--------------------|----------------------------------|-------------------------------|---------------------|
| exception_type       | Exception Type       | Controlled category describing the payment exception                           | Text/Controlled value | Yes                | User selected/workflow suggested | Bank Rejection                | DR-008, FR-004      |
| exception_source     | Exception Source     | Source from which the exception was identified                                 | Text/Controlled value | Yes                | User selected/source file        | PSP report                    | DR-007              |
| payment_channel      | Payment Channel      | Channel or method used for the payment                                         | Text/Controlled value | Yes                | Payment system/user selected     | Bank Transfer                 | DR-006              |
| rejection_reason     | Rejection Reason     | Reason provided by bank, PSP, or payment system for failed or rejected payment | Text                  | Conditional        | Bank/PSP/payment system          | insufficient funds            | FR-003              |
| root_cause           | Root Cause           | Final known cause of the exception after investigation                         | Text/Controlled value | Should Have        | User selected                    | Incorrect beneficiary details | DR-020              |
| customer_impact_flag | Customer Impact Flag | Indicates whether the exception impacts a customer, client, or end user        | Boolean               | Should Have        | User selected/workflow suggested | Yes                           | BR-021              |
| high_value_flag      | High Value Flag      | Indicates whether the payment meets the high-value threshold                   | Boolean               | Should Have        | Calculated                       | Yes                           | BR-019              |
| duplicate_risk_flag  | Duplicate Risk Flag  | Indicates wheteh the case has potential duplicate payment risk                 | Boolean               | Should Have        | User selected/workflow suggested | No                            | BR-020              |

## 6. Status and priority fields

| Field name             | Business name          | Description                                                                    | Data type             | Required?          | Source                           | Example                       | Related requirement |
|------------------------|------------------------|--------------------------------------------------------------------------------|-----------------------|--------------------|----------------------------------|-------------------------------|---------------------|
| status                 | Status                 | Current lifecycle status of the case                                           | Text/Controlled value | Yes                | User selected/workflow default   | In Review                     | DR-009, FR-005      |
| priority               | Priority               | Operational priority assigned to the case                                      | Text/Controlled value | Yes                | User selected/workflow suggested | High                          | DR-010, FR-007      |
| previous_status        | Previous Status        | Prior case status before the most recent status update                         | Text                  | Could Have         | Workflow generated               | New                           | FR-016              |
| status_updated_date    | Status Updated Date    | Date when the current status was assigned                                      | Date/Timestamp        | Should Have        | Workflow generated               | 15-01-2025 11:45              | FR-016              |
| priority_updated_date  | Priority Updated Date  | Date when priority was last updated                                            | Date/Timestamp        | Could Have         | Workflow generated               | 15-01-2025 12:00              | CR-008              |
| priority_change_reason | Priority Change Reason | Reason for manual priority change                                              | Text                  | Conditional        | User entered                     | High-value case identified    | CR-008              |

## 7. SLA and aging fields

| Field name              | Business name           | Description                                                                    | Data type             | Required?          | Source                           | Example                       | Related requirement |
|-------------------------|-------------------------|--------------------------------------------------------------------------------|-----------------------|--------------------|----------------------------------|-------------------------------|---------------------|
| sla_due_date            | SLA Due Date            | Date by which the case should be resolved based on priority rules              | Date                  | Yes for open cases | Calculated                       | 18-01-2025                    | DR-013, FR-006      |
| initial_review_due_date | Initial Review Due Date | Date by which the case should receive first review                             | Date                  | Should Have        | Calculated                       | 16-01-2025                    | BR-025              |
| sla_breach_flag         | SLA Breach Flag         | Indicates whether the case has breached SLA                                    | Boolean               | Yes                | Calculated                       | No                            | DR-014, FR-009      |
| days_open               | Days Open               | Number of business days the case has been open                                 | Integer               | Should Have        | Calculated                       | 4                             | DR-015              |
| aging_bucket            | Aging Bucket            | Grouping of open cases by age                                                  | Text/Controlled value | Should Have        | Calculated                       | 3-5 days                      | DR-015              |
| aged_exception_flag     | Aged Exception Flag     | Indicates whether the case is classified as aged                               | Boolean               | Should Have        | Calculated                       | No                            | FR-010, CR-005      |
| closed_date             | Closed Date             | Date when the case was closed                                                  | Date                  | Conditional        | Workflow generated               | 20-01-2025                    | DR-019              |              
| final_age_at_closure    | Final Age at Closure    | Number of business days between created date and closed date                   | Integer               | Conditional        | Calculated                       | 5                             | BR-034              |

## 8. Escalation fields

| Field name                  | Business name               | Description                                                                            | Data type             | Required?   | Source                   | Example                                                  | Related requir |
|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------|-----------------------|------------ |------------------------- |----------------------------------------------------------|----------------|
| escalation_flag             | Escalation Flag             | Indicates whether the case is escalated                                                | Boolean               | Should Have | User selected/calculated | Yes                                                      | DR-016, FR-012 |
| escalation_reason           | Escalation Reason           | Reason why the case was escalated                                                      | Text/Controlled value | Conditional | User selected            | SLA breach                                               | BR-049         |
| escalation_date             | Escalation Date             | Date when the case was escalated                                                       | Date/Timestamp        | Conditional | Workflow generated       | 17-01-2025 10:15                                         | BR-051         |
| escalation_owner            | Escalation Owner            | Team lead, manager, risk, compliance, or specialist owner reviewing the escalated case | Text                  | Conditional | User selected            | Payments Team Lead                                       | FR-018         |
| escalation_resolution_notes | Escalation Resolution Notes | Notes explaining the outcome of escalation review                                      | Text                  | Conditional | User entered             | Bank confirmed delay; payment expected next business day | FR-016         |

## 9. Investigation and closure fields 

| Field name                     | Business name                  | Description                                        | Data type             | Required?          | Source             | Example                                                                | Related require|
|--------------------------------|--------------------------------|----------------------------------------------------|-----------------------|--------------------|--------------------|------------------------------------------------------------------------|----------------|
| investigation-notes            | Investigation Notes            | Notes added by analyst during case investigation   | Long text             | Yes before closure | User entered       | PSP confirmed rejection due to invalid beneficiart details             | DR-017, FR-011 |
| latest_investigation_note_date | Latest Investigation Note Date | Date of the most recent investigation note         | Date/Timestamp        | Should Have        | Workflow generated | 16-01-2025 15:20                                                       | FR-016         |
| closure_reason                 | Closure Reason                 | Controlled reason selected when closing the case   | Text/Controlled value | Yes before closure | User selected      | Payment reprocessed                                                    | DR-018, FR-013 |
| closure_notes                  | Closure Notes                  | Additional explanation added when closing the case | Long text             | Should Have        | User entered       | Corrected beneficiary details and payment was reprocessed successfully | DR-020         |
| resolution_outcome             | Resolution Outcome             | Summary of final outcome                           | Text/Controlled value | Should Have        | User selected      | Resolved by reprocessing                                               | DR-020         |
| reopened_flag                  | Reopened Flag                  | Indicates whether a closed case was reopened       | Boolean               | Could Have         | Workflow generated | No                                                                     | OQ-004         |
| reopen_reason                  | Reopen Reason                  | Reason for reopening a closed case                 | Text                  | Conditional        | User entered       | Bank confirmed payment was not settled                                 | OQ-004         |    

## 10. Reporting and control fields

| Field name                   | Business name                | Description                                                                    | Data type             | Required?          | Source                           | Example                       | Related requirement |
|------------------------------|------------------------------|--------------------------------------------------------------------------------|-----------------------|--------------------|----------------------------------|-------------------------------|---------------------|
| reportable_status            | Reportable Status            | Simplified status grouping for reports                                         | Text                  | Could Have         | Calculated                       | Open                          | RR-001              |
| open_case_flag               | Open Case Flag               | Indicates whether the case is currently open                                   | Boolean               | Should Have        | Calculated                       | Yes                           | RR-001              |
| unassigned case_flag         | Unassigned Case Flag         | Indicates whether the case has no assigned owner                               | Boolean               | Should Have        | Calculated                       | No                            | CR-006              |
| management_review_flag       | Management Review Flag       | Indicates whether the case should appear in management review                  | Boolean               | Should Have        | Calculated                       | Yes                           | CR-003              |
| control_exception_flag       | Control Exception Flag       | Indicates whether the case represents a control-relevant exception             | Boolean               | Could Have         | User selected/calculated         | Yes                           | CR-007              |
| audit_history_available_flag | Audit History Available Flag | Indicates whether status, owner, priority, and notes history is retained       | Boolean               | Should Have        | Workflow generated               | Yes                           | NFR-003             |

## 11. Controlled values

### 11.1 Status values 

| Value                     | Description                                                             |
|---------------------------|-------------------------------------------------------------------------|
| New                       | Case has been created but investigation has not started                 |
| In Review                 | Analyst is actively investigating the case                              |
| Pending External Response | Waiting for input from bank, PSP, client, or other external party       |
| Escalated                 | Case requires team lead, manager, risk, compliane, or specialist review |
| Resolved                  | Investigation outcome is confirmed but the case is not formally closed  |
| Closed                    | Case is completed with closure reason and required notes                |

### 11.2 Priority values

| Value    | Description                                                         |
|----------|---------------------------------------------------------------------|
| Low      | Low operational impact, no urgent action required                   |
| Medium   | Standard investigation priority                                     |
| High     | Time-sensitive or material issue requiring prompt review            |
| Critical | Severe business, financial, customer, regulatory, or control impact |

### 11.3 Payment channel values

| Value             | Description                                         |
|-------------------|-----------------------------------------------------|
| Bank Transfer     | Standard bank transfer                              |
| Card              | Card payment processed through card network or PSP  |
| Wallet            | Digital wallet payment                              |
| PSP               | Payment processed through Payment Service Provider  |
| Internal Transfer | Internal book transfer or internal payment movement |
| Other             | Payment channel not covered by standard categories  |

### 11.4 Exception source values 

| Value          | Description                                               |
|----------------|-----------------------------------------------------------|
| Bank File      | Exception identified from bank firle or bank response     |
| PSP Report     | Exception identified from Payment Service Provider report |
| Payment System | Exception identified from internal payment system         |
| Reconciliation | Exception identified through reconciliation process       |
| Customer Query | Exception raised through customer or client support query |
| Manual Review  | Exception identified during manual operational review     |

### 11.5 Exception type values 

| Value                  | Description                                               |
|------------------------|-----------------------------------------------------------|
| Bank rejection         | Payment rejected by bank                                  |
| PSP Rejection          | Payment rejected or failed at PSP level                   |
| Returned Payment       | Payment returned after initiaiotn                         |
| Failed Payment         | Payment failed before completion                          |
| Delayed Payment        | Payment or settlement confirmation delayed                |
| Duplicate Payment Risk | Potential duplicate payment identified                    |
| Unmatched Payment      | Payment cannot be matched to expected record              |
| Incorrect Amount       | Amount mismatch identified                                |
| Incorrect Currency     | Currency mismatch identified                              |
| Missing Reference      | Required payment reference is missing                     |
| Customer Query         | Exception raised through customer support or client query |
| Manual Review Required | Case requires manual review but does not fit another type |

### 11.6 Closure reason values

| Value                   | Description                                             |
|-------------------------|---------------------------------------------------------|
| Payment settled         | Payment was completed or confirmed as settled           |
| Payment reprocessed     | Payment was corrected and reprocessed                   |
| Payment cancelled       | Payment was cancelled and no further action is required |
| Duplicate resolved      | Duplicate payment risk was reviewed and resolved        |
| Bank rejection resolved | Bank rejection reason was addressed                     |
| PSP issue resolved      | PSP-related issue was resolved                          |
| Customer query resolved | Customer-impacting issue was resolved                   |
| No action required      | Investigation confirmed no operational action is needed |
| Incorrect exception     | Case was created in error                               |

### 11.7 Aging bucket values

| Value        | Description                                       |
|--------------|---------------------------------------------------|
| 0-2 days     | Case has been open for 0 to 2 business days       |
| 3-5 days     | Case has been open for 3 to 5 business days       |
| 6-10 days    | Case has been open for 6 to 10 business days      |
| 11-30 days   | Case has been open for 11 to 30 business days     |
| Over 30 days | Case has been open for more than 30 business days |

## 12. Derived and calculated fields

| Field name              | Calculation logic                                                                                   | Notes                               |
|-------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------|
| sla_due_date            | Created Date + resolution target based on Priority                                                  | Uses business days                  |
| initial_review_due_date | Created Date + initial review SLA based on Priority                                                 | Uses business days                  |
| sla_breach_flag         | Current Date > SLA Due Date and Status is not Closed                                                | Boolean output                      |
| days_open               | Current Date - Created Date for open cases                                                          | Uses business days                  |
| final_age_at_closure    | Closed Date - Created Date                                                                          | Stored for closed cases             |
| aging_bucket            | Derived from Days Open                                                                              | Used for reporting                  |
| aged_exception_flag     | Days Open > 5 business days and Status is not Closed                                                | Based on business rules             |
| high_value_flag         | Amount >= 100,000 EUR equivalent                                                                    | Threshold may require FX conversion |
| open_case_flag          | Status is not Closed                                                                                | Used for reporting                  |
| unassigned_case_flag    | Owner is blank and Status is not Closed                                                             | Used by team leads                  |
| management_review_flag  | Critical priority, High priority SLA breach, aged High/Critical, duplicate risk, or high-calue case | Used for escalation reporting       |

## 13. Data quality rules

| Rule ID | Data quality rule                                                      | Related field       |
|---------|------------------------------------------------------------------------|---------------------|
| DQ-001  | Case ID must be unique.                                                | case_id             |
| DQ-002  | Payment Reference must not be blank for active cases.                  | payment_reference   |
| DQ-003  | Amount must be greater than zero.                                      | amount              |
| DQ-004  | Currency must be a valid ISO currency code.                            | currency            |
| DQ-005  | Status must be selected from controlled status values.                 | status              |
| DQ-006  | Priority must be selected from controlled priority values.             | priority            |
| DQ-007  | Exception Type must be selected from controlled exception type values. | exception_type      |
| DQ-008  | Closure Reason must not be blank when Status is Closed.                | closure_reason      |
| DQ-009  | Investigation Notes must not be blank when Status is Closed.           | investigation_notes |
| DQ-010  | Closed Date must not be earlier than Created Date.                     | closed_date         |
| DQ-011  | SLA Due Date must not be blank for open cases.                         | sla_due_date        |
| DQ-012  | Owner or Team Queue should not be blank for open cases.                | owner, team_queue   |

## 14. Reporting usage

| Reporting need              | Required fields                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| Open exceptions by status   | status, open_case_flag                                                                            |
| Open exceptions by priority | priority, open_case_flag                                                                          |
| Aged exceptions report      | created_date, days_open, aging_bucket, aged_exception_flag, status                                |
| SLA breach report           | sla_due_date, sla_breach_flag, priority, owner, status                                            |
| High-priority case report   | priority, amount, high_value_flag, exception_type, owner                                          |
| Escalation report           | escalation_flag, escalation_reason, escalation_date, escalation_owner                             |
| Owner workload report       | owner, team_queue, status, priority, sla_breach_flag                                              |
| Exception type breakdown    | exception_type, status, created_date                                                              |
| Payment channel breakdown   | payment_channel, status, exception_type                                                           |
| Closure reason analysis     | closure_reaosn, closed_date, root_cause                                                           |
| Management summary          | status, priority, aging_bucket, sla_breach_flag, escalation_flag, exception_type, payment_channel |

## 15. Open questions

| Question ID | Question                                                                                     | Owner                       |
|-------------|----------------------------------------------------------------------------------------------|-----------------------------|
| OQ-001      | Should high-value thresholds be stored in original currency, EUR equivalent, or both?        | Finance/Product             |
| OQ-002      | Should public holidays be included in business day calculations?                             | Operations/Product          |
| OQ-003      | Should bank and PSP rejection codes be stored separately from business exception type?       | Operations/Technology       |
| OQ-004      | Should investigation notes be free text only, or should structured note categories be added? | Operations                  |
| OQ-005      | Should customer-impacting cases require additional mandatory fields?                         | Customer Support/Operations |
| OQ-006      | Should reopened cases retain previous closure reason or require a new closure cycle?         | Risk/Operations             |
| OQ-007      | Should root cause be mandatory for all closed cases or only selected exception types?        | Operations Manager          |

## 16. Summary

This data dictionary defines the core fields required to support the payment exception management workflow.

The fields support case tracking, investigation, prioritization, SLA monitoring, escalation, closure, audit trail, reporting, and operational controls.

The dictionary should be reviewed alongside the requirements catalog, business rules, reporting requirement, risk and controls matrix, UAT plan, and traceability matrix.
