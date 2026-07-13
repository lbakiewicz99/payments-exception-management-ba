# Risk and Controls Matrix

## 1. Purpose

This document defines the key operational risks and related controls for the payment exception management workflow.

The matrix links risks to control objectives, control activities, related requirements, reporting needs, and UAT eveidence.

The purpose is to show how the target workflow reduces operational risk, improves control visibility, and supports auditability.

## 2. Control objectives

| Control Objective ID | Control Objective                                                                          |
|----------------------|--------------------------------------------------------------------------------------------|
| CO-001               | Ensure all payment exceptions are captured and tracked in a single workflow                |
| CO-002               | Ensure each open exception has clear ownership                                             |
| CO-003               | Ensure payment exceptions are prioritized consistently                                     |
| CO-004               | Ensure SLA breachesz and aged cases are visible and escalated                              |
| CO-005               | Ensure high-risk, high-value, and duplicate-risk cases receive appropriate review          |
| CO-006               | Ensure cases cannot be closed without sufficient investigation evidence                    |
| CO-007               | Ensure status, priority, ownership, escalation, and closure history is retained            |
| CO-008               | Ensure management and control reporting is available for review                            |
| CO-009               | ENsure controlled values are used for status, priority, exception type, and closure reason |
| CO-010               | ENsure data quality issues are identified and monitored                                    | 

## 3. Risk categories

| Risk category       | Description                                                                |
|---------------------|----------------------------------------------------------------------------|
| Case capture risk   | Payments exceptions may not be recorded or tracked                         |
| Ownership risk      | Cases may remain unassigned or unclear                                     |
| Prioritization risk | High-rik cases may not be prioritized correctly                            | 
| SLA and aging risk  | Cases may remain unresolved beyond expected timelines                      |
| Escalation risk     | Cases requiring management or control review may not be escalated          |
| Closure risk        | Cases may be closed without proper investigation evidence                  |
| Audit trail risk    | Investigation, ownership, status, or closure history mau not be retained   |
| Reporting risk      | Management may not have reliable visibility of exception volumes and risks |
| Data quality risk   | Required case data may be incomplete, invalid, or inconsistent             |

## 4. Risk and controls matrix 

| Risk ID | Risk                                                       | Impact                                                                      | Control ID | Control activity                                                                               | Related requirements                      | Reporting/evidence                                     |
|---------|------------------------------------------------------------|-----------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------|-------------------------------------------|--------------------------------------------------------|
| R-001   | Payment exceptions are not captured in a central workflow  | Open issues may be missed, duplicated, or handled inconsistently            | C-001      | Each exception requiring investigation must be created as a case with unique case ID           | BRQ-001, FR-001, FR-002, DR-001           | Exception queue, case ID uniqueness check              |
| R-002   | Cases are created without required payment details         | Analysts may not have enough information to investigate or report cases     | C-002      | Mandatory fields must be completed before a case can move from New to In Review                | FR-003, DR-002 to DR-008, BR-003          | Data quality report, incomplete case report            |
| R-003   | Cases remain unassigned                                    | Cases may nnot be investigated or resolved on time                          | C-003      | Open cases without owner or team queue must be visible to team leads                           | FR-006, FR-017, DR-011, CR-006            | Unassigned cases report                                |
| R-004   | Priority is not assigned or is assigned inconsistently     | High-risk cases may not receive timely attention                            | C-004      | Every open case must have priority selected from controlled values                             | FR-007, DR-010, BR-017, BR-024            | Open cases by priority, missing priority control check |
| R-005   | High-value payment exception are not identified            | Material financial risk may not be reviewed appropriately                   | C-005      | Cases aboce the high-value threshold must be flagged and assigned at least High priority       | BR-019, CR-003, DR-004                    | High-value cases report, management review flag        |
| R-006   | Duplicate payment risk is not escalated                    | Duplicate payments may cause financial loss or recovery effort              | C-006      | Duplicate payment risk cases must be flagged and assigned at least High priority               | BR-020, CR-003                            | Duplicate risk report, escalation report               |
| R-007   | SLA breaches are not visible                               | Cases may remain unresolved beyond operational exceptions                   | C-007      | SLA due date and SLA breach flag must be calculated and shown in the queue                     | FR-008, FR-009, DR-013, DR-014, CR-004    | SLA breach report                                      |
| R-008   | Aged exceptions are not monitored                          | Long-running issues may remain unresolved without management attention      | C-008      | Cases open for more than 5 business days must be classified as aged exceptions                 | FR-010, DR-015, CR-005, BR-035            | Aged exceptions report                                 | 
| R-009   | High-priority aged or SLA-breached cases are not escalated | Material issues may not receive team lead or manager attention              | C-009      | High/Critical SLA-breached or aged cases must be escalated                                     | FR-012, FR-018, CR-003, CR-004, CR-005    | Escalation report, management summary                  |
| R-010   | Cases are closed without investigation notes               | Closure evidence may be insufficient for audit or control review            | C-010      | Investigation notes must be required before case closure                                       | FR-011, DR-017, CR-002, BR-054            | Control evidence report                                |
| R-011   | Cases are closed without closure reason                    | Closure outcomes may be unclear and trend analysis may be unreliable        | C-011      | Closure reason must be mandatory and selected from controlled values                           | FR-013, DR-018, CR-001, BR-053, BR-056    | Closure analysis report, control evidence report       | 
| R-012   | Cases are moved directly from New to Closed                | Cases may bypass investigation workflow                                     | C-012      | Status lifecycle must prevent direct transition from New to Closed                             | FR-014, BR-015                            | Status transition validation, UAT evidence             |
| R-013   | Status values are inconsistent                             | Reporting and workflow logic may become unreliable                          | C-013      | Status must be selected from controlled status values                                          | FR-005, DR-009, DQ-005                    | Invalid status report                                  |
| R-014   | Exception types are entered as free text                   | Root cause analysis and reporting may be inconsistent                       | C-014      | Exception type must be selected from a controlled taxonomy                                     | FR-004, DR-008, BR-075, BR-076            | Exception type breakdown, data quality check           |
| R-015   | Ownership, priority, or status changes are not retained    | Audit trail may be incomplete                                               | C-015      | Case history must retain status, owner, and priority changes                                   | FR-016, CR-007, CR-008, BR-059, to BR-061 | Case history review                                    |
| R-016   | Escalation reason is not recorded                          | Escalation evidence may be unclear                                          | C-016      | Escalated cases must include escalation reason and escalation date                             | FR-012, DR-016, BR-049, BR-051            | Escalation report                                      |
| R-017   | Management reporting is manually prepared and inconsistent | Management may not have reliable view of operational risk                   | C-017      | Management summary must use defined metrics and controlled reporting logic                     | RR-001 to RR-009, BR-074                  | Management summary report                              |
| R-018   | Control evidence is unavailable during review              | Risk or audit teams may not be able to verify control operation             | C-018      | Control evidence report must show closure, SLA, aging, escalation, and data quality indicators | CR-001 to CR-008, RPT-010                 | Control evidence report                                |
| R-019   | Invalid or incomplete data enters reporting                | Metrics may be inaccurate or misleading                                     | C-019      | Data quality rules must identify missing, invalid, or inconsistent required fields             | DQ-001 to DQ-012                          | Data quality exception report                          |
| R-020   | Customer-impacting cases are not identified                | Customer support and operations may not prioritize impacted cases correctly | C-020      | Customer impact flag should be captured and available for reporting                            | customer_impact_flag, BR-021              | Customer-impacting cases report                        |

## 5. Control design summary 

| Control ID | Control type                   | Preventive/Detective | Manual/Automated                  | Frequency          | Owner                         |
|------------|--------------------------------|----------------------|-----------------------------------|--------------------|-------------------------------|
| C-001      | Case creation control          | Preventive           | Automated/workflow                | Per case           | Payment Operation             |
| C-002      | Mandatory field validation     | Preventive           | Automated                         | Per case           | Payment Operations/Product    |
| C-003      | UNassigned case monitoring     | Detective            | Automated report/team lead review | Daily              | Team Lead                     |
| C-004      | Priority required control      | Preventive           | Automated                         | Per case           | Payments Operations           |
| C-005      | High-value flag control        | Preventive/Detective | Automated/calculated              | Per case/Daily     | Team Lead                     |
| C-006      | Duplicate risk escalation      | Preventive/Detective | Manual + workflow flag            | Per case           | Payments Operations/Team Lead |
| C-007      | SLA breach flag                | Detective            | Automated/calculated              | Daily              | Team Lead                     |
| C-008      | Aged exception flag            | Detective            | Automated/calculated              | Daily              | Team Lead                     | 
| C-009      | Escalation control             | Detective/Corrective | workflow + team lead review       | Daily              | Team Lead                     |
| C-010      | Investigation note requirement | Preventive           | Automated                         | Per closure        | Payments Operations           |
| C-011      | Closure reason requirement     | Preventive           | Automated                         | Per closure        | Payment Operations            |
| C-012      | Status transition validation   | Preventive           | Automated                         | Per status change  | Product/Workflow              |
| C-013      | Controlled status values       | Preventive           | Automated                         | Per update         | Product/Workflow              |
| C-014      | Controlled exception taxonomy  | Preventive           | Automated                         | Per case           | Product/Operations            |
| C-015      | Case history retention         | Detective            | Automated                         | Per update         | Product/Workflow              |
| C-016      | Escalation reason requirement  | Preventive           | Automated/Manual                  | Per escalation     | Payments Operations           |
| C-017      | Management reporting           | Detective            | Automated report                  | Weekly             | Operations Manager            |
| C-018      | Control evidence reporting     | Detective            | Automated report                  | Monthly/On request | Risk/Operational Control      |
| C-019      | Data quality checks            | Detective            | Automated report                  | Daily/Weekly       | Operations/Data Team          |
| C-020      | Customer impact flag           | Preventive/Detective | Manual + workflow flag            | Per case           | Payments Operations           |

## 6. Control evidence requirements

| Evidence ID | Evidence                                                  | Used by                   | Related controls |
|-------------|-----------------------------------------------------------|---------------------------|------------------|
| E-001       | Exception queue with case IDs and current statuses        | Operations, Team Lead     | C-001, C-013     |
| E-002       | Data quality report shwoing missing mandatory fields      | Operations, Data Team     | C-002, C-019     |
| E-003       | Unassigned cases report                                   | Team Lead                 | C-003            |
| E-004       | Open cases by priority report                             | Team Lead, Manager        | C-004            |
| E-005       | High-value cases report                                   | Team Lead, Manager, Risk  | C-005            |
| E-006       | Duplicate risk cases report                               | Team Lead, Risk           | C-006            | 
| E-007       | SLA breach report                                         | Team Lead, Manager, Risk  | C-007            |
| E-008       | Aged exceptions report                                    | Team Lead, Manager, Risk  | C-008            | 
| E-009       | Escalation report                                         | Team Lead, Manager        | C-009, C-016     | 
| E-010       | Closed cases with investigation notes and closure reasons | Risk/Control              | C-010, C-011     |
| E-011       | Status transition audit history                           | Risk/Control, Product     | C-012, C-015     |
| E-012       | Exception type breakdown using controlled taxonomy        | Manager, Reporting Team   | C-014            |
| E-013       | Weekly management summary                                 | Operations Manager        | C-017            |
| E-014       | Control evidence report                                   | Risk/Operational Control  | C-018            | 
| E-015       | Customer-impacting cases report                           | Customer Support, Manager | C-020            |

## 7. Key control indicators 

| Indicator ID | Indicator                                      | Expected result | Review owner       | Frequency      |
|--------------|------------------------------------------------|-----------------|--------------------|----------------|
| KCI-001      | Cases without case ID                          | 0               | Operations/Product | Daily          |
| KCI-002      | Open cases without owner or team queue         | 0 or reviewed   | Team Lead          | Daily          |
| KCI-003      | Open cases without priority                    | 0               | Team Lead          | Daily          |
| KCI-004      | Open cases without SLA due date                | 0               | Team Lead          | Daily          |
| KCI-005      | SLA-breached High/Critical cases not escalated | 0               | Team Lead/Manager  | Daily          |
| KCI-006      | Aged High/Critical cases not escalated         | 0               | Team Lead/Manager  | Daily          |
| KCI-007      | Closed cases without investigation notes       | 0               | Risk/Control       | Weekly/Monthly |
| KCI-008      | Closed cases without closure reason            | 0               | Risk/Control       | Weekly/Monthly |
| KCI-009      | Cases with invalid status                      | 0               | Product/Operations | Daily          |
| KCI-010      | Cases with invalid exception type              | 0               | Product/Operations | Daily          |
| KCI-011      | High-value cases not flagged for review        | 0               | Team Lead/Risk     | Daily          |
| KCI-012      | Duplicate risk cases not escalated             | 0               | Team Lead/Risk     | Daily          |

## 8. UAT coverage expectations 

| UAT area                                                | Control objective covered |
|---------------------------------------------------------|---------------------------|
| Create case with required fields                        | CO-001, CO-010            |
| Prevent case progress when mandatory fields are missing | CO-001, CO-010            |
| Assign owner and identify unassigned cases              | CO-002                    |
| Assign and update priority                              | CO-003                    |
| Calculate SLA due date                                  | CO-004                    |
| Flag SLA breach                                         | CO-004                    |
| Flag aged exception                                     | CO-004                    |
| Escalate High/Critical cases                            | CO-005                    |
| Prevent closure without notes                           | CO-006                    |
| Prevent closure without closure reason                  | CO-006                    |
| Enforce valid status transitions                        | CO-009                    |
| Retain case history                                     | CO-007                    |
| Produce management reporting                            | CO-008                    |
| Produce control evidence report                         | CO-008                    |
| Validate controlled values                              | CO-009                    |
| Validate data quality checks                            | CO-010                    |

## 9. Open questions 

| Question ID | Question                                                                        | Owner                       |
|-------------|---------------------------------------------------------------------------------|-----------------------------|
| OQ-001      | Should control evidence reports be generated automatically or on request?       | Risk/Control                |
| OQ-002      | Should high-value threshold vary by currency or be converted to EUR equivalent? | Finance/Product             |
| OQ-003      | Should external waiting time pause SLA breach calculation?                      | Operations/Risk             |
| OQ-004      | Should customer-impacting cases require separate controls?                      | Customer Support/Operations |
| OQ-005      | Should reopened cases be included in control reporting?                         | Risk/Operations             |
| OQ-006      | Who should approve new exception types in the controlled taxonomy?              | Operations Manager/Product  |
| OQ-007      | Should management review flags be fully automated or manually adjustable?       | Operations/Product          |
| OQ-008      | Should some controls be tested daily, weekly, or monthly?                       | Risk/Control                |

## 10. Summary

The risk and controls matrix links payment exception management risk to control activities, requirements, reporting outputs, and evidence.

The controls support centralized case tracking, onwership, prioritization, SLA monitoring, escalation, closure discipline, audit trail retention, reporting, and data quality monitoring.

This document should be reviewed alongside the requirements catalog, business rules, data dictionary, reporting requirements, UAT plan, and traceability matrix.