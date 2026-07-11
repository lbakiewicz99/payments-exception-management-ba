# Reporting Requirements 

## 1. Purpose 

This document defines the reporting requirements for the payment exception management workflow.

The reporting layer should provide operational users, team leads, managers, and control stakeholders with visibility into open exceptions, aged items, SLA breaches, workload, escalation, exception trends, and closure outcomes.

Reporting requirements support daily operations, workload management, escalation control, management oversight, root cause analysis, and audit evidence.

## 2. Reporting objectives

The reporting solution should allow stakeholders to:

* monitor open payment exceptions;
* identify high-priority and aged cases;
* track SLA breaches;
* review workload by owner or team queue;
* understand exception volumes by type, source, and payment channel;
* monitor escalated cases;
* review closure reasons and root causes;
* support daily and weekly management reporting;
* provide evidence for operational control review.

## 3. Reporting stakeholders

| Stakeholder                   | Reporting needed                                                                    |
|-------------------------------|-------------------------------------------------------------------------------------|
| Payments Operations Analyst   | Needs a filtered queue of cases requiring action                                    |
| Payments Operations Team Lead | Needs workload, SLA breach, aged case, escalation, and unassigned case reporting    |
| Payments Operations Manager   | Needs management summary, trend analysis, control indicators, and exception drivers |
| Finance Operations            | Needs visibility of payment exceptions with financial impact                        |
| Reconciliation Team           | Needs visibility of payment exceptions linked to reconciliation breaks              |
| Risk/Operational Control      | Needs SLA, aging, escalation, closure, and audit trail indicators                   |
| Customer Support              | Needs status visibility for customer-impacting payment issues                       |
| Product/Technology            | Needs reporting definitions to support workflow design and implementation           |
| Data/Reporting Team           | Needs field definitions, metric, logic, and report layout requirements              |

## 4. Reporting principles

| Principle                | Description                                                                                 |
|--------------------------|---------------------------------------------------------------------------------------------|
| Clear metric definitions | Each metric should have a documented business definition.                                   |
| Operational usefulness   | Reoirts should support actual daily decisions, not just look decorative.                    |
| Drill-down capability    | Summary reports should allow users to identify underlying cases.                            |
| Controlled values        | Reports should use standardized statuses, priorities, exception types, and closure reasons. |
| Timeliness               | Operational reports should reflect current case data.                                       |
| Auditability             | Reporting should support evidence of control review and escalation.                         |
| Consistency              | Metrics should be calculated consistently across all reports.                               |

## 5. Key metrics

| Metric ID | Metric                          | Definition                                                        | Primary users                | Related requirements |
|-----------|---------------------------------|-------------------------------------------------------------------|------------------------------|----------------------|
| M-001     | Open Exceptions                 | Count of cases where status is not Closed                         | Analysts, Team Lead, Manager | RR-001               |
| M-002     | Open Exceptions by Status       | Count of open cases grouped by current status                     | Analysts, Team Lead          | RR-001               |
| M-003     | Open Exceptions by Priority     | Count of open cases grouped by priority                           | Analysts, Team Lead, Manager | RR-002               |
| M-004     | Aged Exceptions                 | Count of open cases older than 5 business days                    | Team Lead, Manager, Risk     | RR-003               |
| M-005     | Aged Exceptions by aging bucket | Count of open cases grouped by aging bucket                       | Team Lead, Manager, Risk     | RR-003               |
| M-006     | SLA breaches                    | Count of open cases where current date is later than SLA due date | Team Lead, Manager, Risk     | RR-004               |
| M-007     | High-Priority Cases             | Count of open cases with priority High or Critical                | Team Lead, Manager           | CR-003               |
| M-008     | Escalated Cases                 | Count of cases with status Escalated or escalation flag = Yes     | Team Lead, Manager           | FR-018               |
| M-009     | Unassigned Cases                | Count of open cases without owner or team queue                   | Team Lead                    | FR-017, CR-006       | 
| M-010     | Exceptions by Type              | Count of cases grouped by exception type                          | Team Lead, Manager           | RR-005               |
| M-011     | Exceptions by Payment Channel   | Count of cases grouped by payment channel                         | Manager, Reporting Team      | RR-006               |
| M-012     | Exceptions by source            | Count of cases grouped by exception source                        | Manager, Reporting Team      | DR-007               |
| M-013     | Owner Workload                  | Count of open cases grouped by owner or team queue                | Team Lead                    | RR-007               |
| M-014     | Closed Cases                    | Count of cases closed within selected period                      | Team Lead, Manager           | RR-009               |
| M-015     | Closure Reasons                 | Count of closed cases grouped by closure reason                   | Manager, Risk                | RR-008               |
| M-016     | Root causes                     | Count of closed cases grouped by root cause                       | Manager, Product, Operations | DR-020               |
| M-017     | Customer-Impacting Cases        | Count of cases where customer impact flag = Yes                   | Customer Support, Manager    | BR-021               |
| M-018     | High-Value Cases                | Count of cases where high value flag = Yes                        | Team Lead, Manager, Risk     | BR-019               |
| M-019     | Duplicate Risk Cases            | Count of cases where duplicate risk flag = Yes                    | Team Lead, Manager, Risk     | BR-020               |

## 6. Report catalog 
| Report ID | Report name             | Purpose                                                               | Primary users                    | Frequency          |
|-----------|-------------------------|-----------------------------------------------------------------------|----------------------------------|--------------------|
| RPT-001   | Exception Queue         | Operational working list of open payment exceptions                   | Analysts                         | Real-time/Daily    |
| RPT-002   | Team Lead Control View  | Workload, unassigned cases, SLA breaches, aged items, and escalations | Team Lead                        | Daily              |
| RPT-003   | Management Summary      | High-level view of volumes, risk indicators, trends, and closures     | Operations Manager               | Weekly             |
| RPT-004   | SLA Breach Report       | Cases breaching SLA or close to breach                                | Team Lead, Manager, Risk         | Daily              |
| RPT-005   | Aged Exceptions Report  | Cases open beyond aging threshold                                     | Team Lead, Manager, Risk         | Daily/Weekly       | 
| RPT-006   | Escalation Report       | Escalated cases and escalation reasons                                | Team Lead, Manager               | Daily              |
| RPT-007   | Owner Workload Report   | Case allocation by owner or queue                                     | Team Lead                        | Daily              |
| RPT-008   | Exception Trend Report  | Exception volumes by type, channel, source, and period                | Manager, Product, Reporting Team | Weekly/Monthly     |
| RPT-009   | Closure Analysis Reprot | Closure reasons and root casues for resolved cases                    | Manager, Risk, Product           | Weekly/Monthly     |
| RPT-010   | Control Evidence Report | SLA, aging, escalation, closure, and audit indicators                 | Risk/Operational Control         | Monthly/On Request |

## 7. RPT-001: Exception Queue

### Purpose

The exception queue is the main operational view used by analysts to review and work payment exception cases.

### Required fields

| Field             | Description                            |
|-------------------|----------------------------------------|
| Case ID           | Unique case identifier                 |
| Payment Reference | Internal or external payment reference |
| Exception Type    | Controlled exception category          |
| Payment Channel   | Payment channel                        |
| Exception Source  | Source of the exception                |
| Amount            | Payment amount                         |
| Currency          | Payment currency                       | 
| Status            | Current case status                    |
| Priority          | Current priority                       |
| Owner             | Assigned analyst or team queue         |
| Created Date      | Case creation date                     |
| SLA Due Date      | Resolution due date                    |
| SLA Breach Flag   | Indicates SLA breach                   |
| Aging Bucket      | Case aging category                    |
| Escalation Flag   | Indicates escalated case               |

### Required filters

* status;
* priority;
* onwer;
* team queue;
* exception type;
* payment channel;
* exception source;
* SLA breach flag;
* aging bucket;
* escalation flag;
* created date range.

### Sorting requirements

Default sorting:

1. Critical priority first;
2. SLA-breached cases first;
3. oldest created date first.

### Related requirements

* RR-001
* RR-002
* RR-003
* RR-004
* FR-015

## 8. RPT-002: Team Lead Control view

### Purpose

The Team Lead control View supports daily workload management and operational control.

It should help team leads identify cases requiring assignment, escalation, or urgent review.

### Required sections

| Section                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| KPI summary              | Open cases, aged cases, SLA breaches, high-priority cases, unassigned cases |
| Unassigned cases         | Open cases without owner or team queue                                      |
| SLA breaches             | Cases where SLA breach flag = Yes                                           |
| Aged exceptions          | Cases open for more than 5 business days                                    |
| Escalated cases          | Cases requiring team lead or management attention                           |
| Owner workload           | Open case count by owner                                                    |
| Exception type breakdown | Open cases grouped by exception type                                        |

### Related requirements 

* FR-017
* FR-018
* RR-001
* RR-002
* RR-003
* RR-004
* RR-007
* CR-003
* CR-004
* CR-005
* CR-006

## 9. RPT-003: Management Summary

### Purpose

The Management Summary provides a high-level view of payment exception volumes, risk indicators, operationsl performance, and recurring drivers.

### Required KPIs

| KPI                           | Description                                     |
|-------------------------------|-------------------------------------------------|
| Total open exceptions         | Count of all cases not Closed                   |
| New exceptions this period    | Count of cases created in selected period       |
| Closed exceptions this period | Count of cases closed in selected period        |
| Aged exceptions               | Count of open cases older than aging threshold  |
| SLA breaches                  | Count of open cases braching SLA                |
| High-priority cases           | Count of High and Critical cases                |
| Escalated cases               | Count of escalated cases                        |
| Unassigned cases              | Count of open cases without owner or queue      |
| Top exception type            | Most frequent exception type in selected period |
| Top payment channel           | Payment channel with highest exception volume   |    

### Required brakdowns 

* open exceptions by status;
* open exceptions by priority;
* exceptions by type;
* exceptions by payment channel;
* exceptions by source;
* aged exceptions by aging bucket;
* closure reasons;
* root causes.

### Related requirements

* RR-001
* RR-002
* RR-003
* RR-004
* RR-005
* RR-006
* RR-008
* RR-009

## 10. RPT-004: SLA Breach Report

### Purpose

The SLA Breach Report identifies cases that have brached SLA or are appraoching SLA breach.

### Required fields

| Field           | Description                        |
|-----------------|------------------------------------|
| Case ID         | Unique case identifier             |
| Priority        | Case priority                      |
| Status          | Current case status                |
| Owner           | Assigned owner                     |
| Created Date    | Case creation date                 |
| SLA Due Date    | Resolution due date                |
| Days Open       | Business days open                 |
| Exception Type  | Exception category                 |
| Payment Channel | Payment channel                    |
| Escalation Flag | Indicates wheter case is escalated |

### Logic

A case should appear in this report if:

* status is not closed; and
* SLA breach flag = Yes.

Optional enhancement:

* include cases due within the next business day.

### Related requirements

* FR-008
* FR-009
* RR-004
* CR-004

## 11. RPT-005: Aged Exceptions Report

### Purpose

The Aged Exceptions Report identifies cases that have remained open beyond the aging threshold.

### Logic

A case should appear in this report if:

* status is not closed; and
* day open > 5 business days.

### Required fields

| Field           | Description                  |
|-----------------|------------------------------|
| Case ID         | Unique case identifier       |
| Exception Type  | Exception category           |
| Priority        | Case priority                |
| Status          | Current status               |
| Owner           | Assigned owner               |
| Created Date    | Case creation date           |
| Days Open       | Number of business days open |
| Aging Bucket    | Aging category               |
| SLA Breach Flag | Indicate SLA breach          |
| Escalation Flag | Indicates escalation         |

### Related requirements

* FR-010
* RR-003
* CR-005

## 12. RPT-006: Escalation Report

### Purpose

The Escalation Report shows cases requiring team lead, manager, risk, compliance, or specialist review.

### Logic

A case should appear in this report if:

* status = Escalated; or 
* escalation flag = Yes.

### Required fields

| Field             | Description                             |
|-------------------|-----------------------------------------|
| Case ID           | Unique identifier                       |
| Priority          | Case priority                           |
| Escalation Reason | Reason for escalation                   |
| Escalation Date   | Date of escalation                      |
| Escalation Owner  | Owner responsible for escalation review |
| Status            | Current status                          |
| SLA Breach Flag   | Indicates SLA breach                    |
| Aging Bucket      | Aging category                          |
| Exception Type    | Exception category                      |
| Amount            | Payment amount                          |
| Currency          | Payment currency                        |

### Related requirements

* FR-012
* FR-018
* CR-003
* CR-004
* CR-005

## 13. RPT-007: Owner Workload Report

### Purpose 

The Owner Workload Report helps team leads monitor case distribution across analysts and queues.

### Required metrics

| Metric                       | Description                                    |
|------------------------------|------------------------------------------------|
| Open cases by owner          | Count of open cases assigned to each analyst   |
| High-priority cases by owner | Count of High and Critical open cases by owner |
| SLA breaches by owner        | Count of SLA-breached cases by owner           |
| Aged cases by owner          | Count of aged cases by owner                   |
| Unassigned cases             | Count of open cases without owner or queue     |

### Related requirements

* FR-006
* FR-017
* RR-007
* CR-006

## 14. RPT-008: Exception Trend Report

### Purpose

The Exception Trend Report supports root cause analysis and management review.

It should show how exception volumes change over time by type, payment, and source.

### Required breakdowns

| Breakdown                          | Description                         |
|------------------------------------|-------------------------------------|
| Exceptions by month                | Monthly exception volume            |
| Exceptions by type                 | Exception volume by exception type  |
| Exceptions by payment channel      | Exception volume by payment channel |
| Exceptions by source               | Exception volume by source          |
| High-priority exceptions over time | Trend of High and Critical cases    |
| SLA breaches over time             | Trend of SLA breaches               |
| Aged exceptions over time          | Trend of aged cases                 |

### Related requirements

* RR-005
* RR-006
* RR-009

## 15. RPT-009: Closure Analysis Report

### Purpose

The Closure Analysis Report shows how cases are resolved and supports process improvement.

### Required metrics

| Metric                     | Description                                                |
|----------------------------|------------------------------------------------------------|
| Closed cases by period     | Count of closed cases by week or month                     |
| Closure reasons            | Count of cases by closure reason                           |
| Root causes                | Count of cases by root cause                               |
| Average days to close      | Average business days between created date and closed date |
| Closure by exception type  | Closed cases grouped by exception type                     |
| Closure by payment channel | Closed cases grouped by payment channel                    |

### Related requirements

* RR-008
* DR-018
* DR-019
* DR-020

## 16. RPT-010: Control Evidence Report

### Purpose

The Control Evidence Report supports risk, audit, and operational control review.

It should provide evidence that key controls are operating as expected.

### Required control indicators

| Indicator                                | Description                                     |
|------------------------------------------|-------------------------------------------------|
| Cases closed without closure reason      | Should be zero                                  |
| Cases closed without investigation notes | Should be zero                                  |
| Open cases without owner or queue        | Should be reviewed by team lead                 |
| SLA-breached cases                       | Should be reviewed and escalatef where required | 
| Aged High or Critical cases              | Should be escalated                             |
| Cases with missing priority              | Should be zero                                  |
| Cases with invalid status                | Should be zero                                  |
| High-value cases not escalated           | Should be reviewed                              |
| Duplicate risk cases not escalated       | Should be reviewed                              |

### Related requirements 

* CR-001 
* CR-002
* CR-003
* CR-004
* CR-005
* CR-006
* CR-007
* CR-008

## 17. Filter requirements

Reports should support the following common filters where applicable:

| Filter               | Applies to                                            |
|----------------------|-------------------------------------------------------|
| Date range           | All reports                                           |
| Status               | Exception queue, management summary, workload reports |
| Priority             | Excpetion queue, SLA, aged, management summary        |
| Owner                | Exception queue, workload reports                     |
| Team queue           | Exception queue, workload reports                     |
| Exception type       | Exception queue, trend reports, management summary    |
| SLA breach flag      | Exception queue, SLA report, management summary       |
| Aging bucket         | Exception queue, aged reports                         |
| Escalation flag      | Exception queue, escalation report                    |
| Customer impact flag | Exception queue, management summary                   |
| High value flag      | Exception queue, ,amage,emt summary                   |
| Duplicate risk flag  | Exception queue, escalation report                    |

## 18. Export requirements 

| Requirement ID | Requirement                                                                 |
|----------------|-----------------------------------------------------------------------------|
| EXP-001        | Users should be able to export exception queue data to CSV.                 |
| EXP-002        | Team leads should be able to export aged exceptions and SLA breach reports. |
| EXP-003        | Managers should be able to export weekly management summary data.           |
| EXP-004        | Risk/Control users should be able to export control evidence reports.       |

## 19. Data refresh requirements  

| Requirement ID | Requirement                                                                           |
|----------------|---------------------------------------------------------------------------------------|
| REF-001        | Operational queue data should reflect the latest available case data.                 |
| REF-002        | SLA breach and aging indicators should be recalculated at least daily.                |
| REF-003        | Management summary reporting should support weekly review.                            |
| REF-004        | Closed case metrics should include cases closed during the selected reporting period. |
| REF-005        | Reporting logic should use controlled values defined in the data dictionary.          |

## 20. Reporting assumptions 


| Assumption ID | Requirement                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| AS-001        | Case data is available in structured form.                                                   |
| AS-002        | Status, priority, exception type, payment channel, and closure reason use controlled values. |
| AS-003        | Created date and closed date are available for aging and resolution metrics.                 |
| AS-004        | SLA due date and SLA breach flag are calculated by the workflow or reporting layer.          |
| AS-005        | Users can access reports according to their operational role.                                |
| AS-006        | Reports are based on fictional sample data for this portfolio case study.                    |

## 21. Open questions

| Question ID | Question                                                                    | Owner                       |
|-------------|-----------------------------------------------------------------------------|-----------------------------|
| OQ-001      | Should reports use calendar days or business days for aging display?        | Operations/Product          |
| OQ-002      | Should external waiting time pause SLA reporting?                           | Operations/Risk             |
| OQ-003      | Should management reports show both current open cases and period movement? | Operations Manager          |
| OQ-004      | Should customer-impacting cases have a separate report?                     | Customer Support/Operations |
| OQ-005      | Should high-value threshold be configurable by currency?                    | Finance/Product             |
| OQ-006      | Should control evidence reports be generated automatically or on request?   | Risk/Control                |
| OQ-007      | Should reporting include reopened cases as a separate metric?               | Operations/Risk             |

## 22. Summary

The reporting requirements define how payment exception data should be translated into operational, management, and control views.

The reports support daily case handling, workload management, SLA monitoring, escalation oversight, trend analysis, and audit evidence.

These requirements should be reviewed alongside the requirements catalog, business rules, data dictionary, risk and controls matrix, UAT plan, and traceability matrix.