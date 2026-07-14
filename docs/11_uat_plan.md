# UAT Plan

## 1. Purpose

This documentation defines the User Acceptance Testing (UAT) plan for the payment exception management workflow.

The purpose of UAT is to confirm that the proposed workflow meets business requirements, supports operational users, enforces key business rules, provides required reporting, and supports risk and control objectives.

UAT should validate that business users can create, manage, escalate, resolve, close, and report payment exception cases using the target workflow.

## 2. UAT objectives

The main objectives of UAT are to confirm that:

* payment exception cases can be created with required data;
* status lifecycle rules work as expected;
* priority, SLA, aging, and escalation rules are correctly applied;
* case ownership can be assigned and monitored;
* investigation notes and closure reasons are captured;
* cases cannot be closed without required evidence;
* operational and management reports provide expected information;
* risk and control requirements are supported;
* users can perform daily exception management activities without relying on manual spreadsheets.

## 3. UAT scope

### In scope

The following areas are in scope for UAT:

* case creation;
* mandatory field validation;
* exception classification;
* status updates;
* owner assignment;
* priority assignment;
* SLA due date calculation;
* SLA breach flagging;
* aging bucket calculation;
* aged exception identification;
* escalation workflow;
* investigation ntoes;
* closure reason validation;
* case closure;
* exception queue filters;
* unassigned case reporting;
* aged exception reporting;
* SLA breach reporting;
* escalation reporting;
* management summary reporting;
* control evidence reporting;
* audit trail/case history review.

### Out of scope

The following areas are out of scope for UAT:

* real bank or PSP integrations;
* production payment processing;
* authentication and authorization implementation;
* real client or customer data;
* automated file ingestion from external parties;
* cloud deployment;
* performance testing under production volumes;
* disaster recovery testing.

## 4. UAT participants

| Role                              | Responsibility                                                                                      |
|-----------------------------------|-----------------------------------------------------------------------------------------------------|
| Payments Operations Analyst       | Execute operational test cases for case creation, investigation, status updates, notes, and closure |
| Payments Operations Team Lead     | Execute workload, ownership, escalation, SLA, and aged case test cases                              |
| Payments Operations Manager       | Review management reporting and sign-off readiness                                                  |
| Risk/Operational Control          | Review control evidence, closure rules, audit trail, and escalation controls                        |
| Product/Technology Representative | Support UAT execution, clarify solution behavior, and review defects                                |
| QA/Test Support                   | Support test coordination, defect logging, and retesting                                            |
| Business Analyst                  | Prepare UAT scenarios, map test cases to requirements, support execution, and track sign-off        |

## 5. UAT entry criteria

UAT should begin only when the following conditions are met:

| Entry criterion              | Description                                                                         |
|------------------------------|-------------------------------------------------------------------------------------|
| Requirement baseline agreed  | Requirements catalog, business rules, and reporting requirements have been reviewed |
| Test cases prepared          | UAT test cases have been documented and mapped to requirements                      |
| Test data available          | Sample payment exception cases are available for UAT                                |
| Test environment available   | UAT environment or prototype is accessible to users                                 |
| User access confirmed        | UAT participants have appropriate access                                            |
| Known limitations documented | Any known gaps or constraints are documented before testing begins                  |
| Defet process agreed         | Defect logging, prioritization, and retesting process is agreed                     |
| UAT schedule agreed          | Testing timeline and participant availability are confirmed                         |

## 6. UAT exit criteria 

UAT can be considered complete when:

| Exit criterion             | Description                                                                |
|----------------------------|----------------------------------------------------------------------------|
| Critical test cases passed | All Must Have requirements have passed UAT or have approved workaround     |
| Critical defects resolved  | No open Critical or High severity defects remain without business approval |
| Reporting validated        | Required operational, management, and control reports have been reviewed   |
| Controls validated         | Key control requirements have been tested                                  |
| Defects documented         | All defects are logged with status and resolution plan                     |
| Business sign-ff obtained  | Payment Operations Manager or delegated owner signs off UAT                |
| Traceability completed     | Test cases are mapped to requirements and controls                         |

## 7. Defect severity 

| Severity    | Description                                                             | Example                                                             |
|-------------|-------------------------------------------------------------------------|---------------------------------------------------------------------|
| Critical    | Prevents core workflow from being used or creates major control failure | Cases cannot be created, cases can close without closure reason     |
| High        | Major business function fails or key control does not work              | SLA breaches are not flagged, High priority cases are not escalated |
| Medium      | Function works partially but has business impact                        | Filter does not work for one field, report total is incorrect       |
| Low         | Minor issue with limited business impact                                | Label typo, minor formatting issue                                  |
| Enhancement | Improvement request outside agreed UAT scope                            | Additional dashboard chart requested                                |

## 8. Test data requirements 

UAT should include test cases covering different payment exception scenarios.

| Test data scenario                 | Purpose                                              |
|------------------------------------|------------------------------------------------------|
| Standard Medium priority exception | Validate standard case creation and investigation    |
| High-value payment exception       | Validate high-value flag and priority rules          |
| Duplicate payment risk case        | Validate escalation and control reporting            |
| Bank rejection case                | Validate exception type and closure reason           |
| PSP rejection case                 | Validate Payment Service Provider exception handling |
| Returned payment case              | Validate payment status and investigation fields     |
| SLA-breached case                  | Validate SLA breach reporting                        |
| Aged exception case                | Validate aging bucket and aged exception reporting   |
| Unassigned case                    | Validate team lead control view                      |
| Escalated case                     | Validate escalation report and escalation reason     |
| Closed case with notes and reason  | Vlaidate closure requirements                        |
| Invalid closure attempt            | Validate preventive controls                         |

## 9. UAT test cases 

| Test Case ID | Test Case                                          | Objective                                 | Related requirements             | Expected result                                                           |
|--------------|----------------------------------------------------|-------------------------------------------|----------------------------------|---------------------------------------------------------------------------|
| TC-001       | Create new payment exception case                  | Validate case creation and unique case ID | FR-001, FR-002, DR-001           | Case is created with unique case ID and status New                        |
| TC-002       | Validate mandatory payment fields                  | Confirm required fields are enforce       | FR-003, DR-002 to DR-008         | Case cannot progress without mandatory fields                             |
| TC-003       | Select exception type from controlled list         | Validate exception taxonomy               | FR-004, DR-008, BR-075           | User can only select valid exception type                                 |
| TC-004       | Move case from New to In Review                    | Validate valid status transition          | FR-005, BR-008                   | Status updates to In Review                                               |
| TC-005       | Prevent direct transition from New to Closed       | Validate status lifecycle control         | FR-014, BR-015, C-012            | System prevents direct closure                                            |
| TC-006       | Assign case owner                                  | Validate ownership assignment             | FR-006, DR-011                   | Owner is saved and visible in queue                                       |
| TC-007       | View unassigned cases                              | Validate team lead monitoring             | FR-017, CR-006                   | Unassigned open cases appear in report                                    |
| TC-008       | Assign High priority to high-value case            | Validate high-value priority rule         | BR-019, CR-003                   | Case is flagged High priority or above                                    | 
| TC-009       | Flag duplicate payment risk                        | Validate duplicate risk control           | BR-020. C-006                    | Case is flagged and visible for escalation review                         | 
| TC-010       | Calculate SLA due date                             | Validate SLA calculation                  | FR-008, DR-013, BR-025           | SLA due date is calculated based on priority                              |
| TC-011       | Flag SLA breach                                    | Validate SLA breach logic                 | FR-009, DR-014, CR-004           | Case is flagged when current date exceeds SLA due date                    | 
| TC-012       | Calculate aging bucket                             | Validate aging logic                      | FR-010, DR-015, BR-033 to BR-038 | Case appears in correct aging bucket                                      |
| TC-013       | Identify aged exception                            | Validate aged exception rule              | FR-010, CR-045, BR-035           | Case open over 5 business days is flagged aged                            |
| TC-014       | Escalate High priority SLA-breached case           | Validate escalationm rule                 | FR-012, CR-003, CR-004           | Case status or flag shows escalation                                      | 
| TC-015       | Add investigation notes                            | Validate investigation audit trail        | FR-011, DR-017, CR-002           | Notes are saved and visible in case history                               |
| TC-016       | Prevent closure without notes                      | Validate closure evidence control         | CR-002, BR-054                   | Case cannot close without investigation notes                             |  
| TC-017       | Prevent closure without closure reason             | Validate closure reason control           | FR-013, DR-018, DR-019           | Case cannot close without closure reason                                  | 
| TC-018       | Close resolved case                                | Validate closure process                  | FR-013, DR-018, DR-019           | Case moves from Resolved to Closed and closed date is recorded            |
| TC-019       | Review case history                                | Validate audit trail                      | FR-016, CR-007                   | Status, owner, priority, and note history is visible                      | 
| TC-020       | Filter exception queue                             | Validate queue filtering                  | FR-015                           | Queue filters by status, priority, owner, type, channel, and SLA flag     |
| TC-021       | Review SLA breach report                           | Validate operational reporting            | RR-004                           | SLA-breached open cases are displayed                                     |
| TC-022       | Review aged exceptions report                      | Validate aged reporting                   | RR-003                           | Aged open cases are dusokayed by aging bucket                             | 
| TC-023       | Review escalation report                           | Validate escalation reporting             | FR-018, RR-009                   | Escalated cases and reasons are displayed                                 |
| TC-024       | Review owner workload report                       | Validate workload reporting               | RR-007                           | Open cases are grouped by owner or queue                                  |
| TC-025       | Review management summary                          | Validate management reporting             | RR-001 to RR-009                 | Summary shows open, aged, SLA-breached, escalated, and closed cases       | 
| TC-026       | Review control evidence report                     | Validate control reporting                | CR-001 to CR-008, RPT-010        | Report shows closure, SLA, aging, escalation, and data quality indicators | 
| TC-027       | Validate invalid status values are not allowed     | Validate controlled status values         | DR-009, DQ-005                   | User cannot select invalid status                                         |  
| TC-028       | Validate invalid priority values are not allowed   | Validate controlled priority values       | DR-010, DQ-006                   | User cannot select invalid priority                                       |
| TC-029       | Validate closed date cannot be before created date | Validate data quality rule                | DQ-010                           | Invalid data sequence is prevented or flagged                             |
| TC-030       | Export exception queue data                        | Validate export requirement               | EXP-001                          | User can export exception queue data to CSV                               |

## 10. Sample detailed test case format

### TC-001: Create new payment exception case

| Field                | Detail                                                                                                  |
|----------------------|---------------------------------------------------------------------------------------------------------|
| Test Case ID         | TC-001                                                                                                  |
| Test case name       | Create new payment exception case                                                                       |
| Objective            | Confirm that an analyst can create a new payment exception case                                         |
| Preconditions        | User has access to the exception workflow                                                               |
| Test data            | Standard Medium priority payment exception                                                              |
| Related requirements | FR-001, FR-002, DR-001, DR-012                                                                          |
| Steps                | 1. Open exception workflow. 2. Select create new case. 3. Enter required payment details. 4. Save case. |
| Expected result      | Case is created successfully, unique case ID is assigned, status is New, created date is recorded       |
| Actual result        | To be completed during UAT                                                                              |
| Status               | Not Run                                                                                                 |
| Defect ID            | To be completed if failed                                                                               |

### TC-017: Prevent closure without closure reason 

| Field                | Detail                                                                                                  |
|----------------------|---------------------------------------------------------------------------------------------------------|
| Test case ID         | TC-017                                                                                                  |
| Test case name       | Prevent closure without closure reason                                                                  |
| Objective            | Confirm that a case cannot be closed without selecting closure reason                                   |
| Preconditions        | Case exists and is in Resolved status                                                                   |
| Test data            | Resolved payment exception case                                                                         |
| Related requirements | FR-013, DR-018, CR-001, BR-053                                                                          |
| Steps                | 1. Open resolved case. 2. Attempt to close case without selecting closure reason. 3. Save case.         |
| Expected result      | System prevents closure and displays validation message                                                 |
| Actual result        | To be completed during UAT                                                                              |
| Status               | Not Run                                                                                                 |
| Defect ID            | To be completed if failed                                                                               |

## 11. UAT execution tracking

| Field          | Description                           |
|----------------|---------------------------------------|
| Test Case ID   | Unique test case identifier           |
| Test case name | Short test description                |
| Tester         | User executing the test               |
| Execution date | Date when test was executed           |
| Status         | Not Run, Passed, Failed, Blocked      |
| Actual result  | Result observed by tester             |
| Defect ID      | Linked defect if failed               |
| Retest status  | Not Required, Pending, Passed, Failed |  
| Sign-off notes | Business notes or comments            |

## 12. Defect management process

Defects identified during UAT should be logged and reviewed.

Recommended defect workflow:

1. Tested identifies issue during UAT execution.
2. Tester records actual result and evidence.
3. Defect is logged with severity and related test case.
4. Business Analyst reviews whether the issue is a defect, requirement gap, or enhancement.
5. Product/Technology team reviews and provides resolution plan.
6. Defect is fixed or accepted with workaround.
7. Tester retest the scenario.
8. UAT status is updated.

## 13. UAT reporting

During UAT, the following summary should be maintained:

| Metric                    | Description                                      |
|---------------------------|--------------------------------------------------|
| Total test cases          | Number of planned UAT test cases                 |
| Passed test cases         | Number of test cases passed                      |
| Failed test cases         | Number of test cases failed                      |
| Blocked test cases        | Number of test cases blocked                     |
| Not run test cases        | Number of test cases not yet executed            |
| Open Critical defects     | Count of unresolved Critical defects             |
| Open High defects         | Count of unresolved High defects                 |
| Retest pending            | Count of defects awaiting retest                 |
| UAT completion percentage | Completed test cases divided by total test cases |

## 14. UAT sign-off

UAT sign-off should confirm that:

* agreed UAT scope was tested;
* Must Have requirements were validated;
* key business rules were tested;
* key controls were testes;
* reporting outputs were reviewed;
* open defects are acceptable or resolved;
* business users agree that the workflow is fit for purpose.

Sign-off onwer:

| Role                              | Sign-off responsibility                                 |
|-----------------------------------|---------------------------------------------------------|
| Payments Operations Manager       | Final business sign-off                                 |
| Payments Operations Team Lead     | Operational workflow sign-off                           |
| Risk/Operational Control          | Control evidence sign-off                               |
| Product/Technology Representative | Delivery readiness acknowledgement                      |
| Business Analyst                  | Traceability and documentation completness confirmation |

## 15. Open questions

| Question ID | Question                                                                                          | Owner                   |
|-------------|---------------------------------------------------------------------------------------------------|-------------------------|
| OQ-001      | Should UAT include public holiday scenarios for SLA calculation?                                  | Operations/Product      |
| OQ-002      | Should UAT include reopened case scenarios?                                                       | Operations/Risk         |
| OQ-003      | Should UAT validate role-based access even if implementation is out of scope for this case study? | Product/Technology      |
| OQ-004      | Should export functionality be tested for all reports or only exception queue?                    | Operations/Reporting    |
| OQ-005      | Should test evidence be stored as screenshots, exported files, or test execution notes?           | QA/Business Analyst     |
| OQ-006      | Should Risk/Control sign-off be mandatory for go-live?                                            | Operations Manager/Risk |

## 16. Summary

This UAT plan defines how the payment exception management workflow should be validated by business users.

It link UAT execution to business requirements, functional requirements, business rules, reporting requirements, and control objectives.

Successful UAT should demonstrate that the workflow supports controlled payment exception handling, operational visibility, escalation discipline, closure evidence, and management reporting.