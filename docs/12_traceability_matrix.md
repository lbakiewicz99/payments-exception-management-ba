# Requirements Traceability Matrix

## 1. Purpose

This document provides end-to-end traceability across the payment exception management Business Analyst case study.

The traceability matrix links:

* business objectives;
* business requirements;
* functional and non-functional requirements;
* data and reporting requirements;
* user stories;
* business rules;
* risks and controls;
* UAT test cases.

The purpose is to confirm that each significant business need is supported by defined requirements and can be validated through testing or control evidence.

## 2. Traceability model

The projects uses the following traceability flow:

```text
Business objective
→ Business requirement
→ Functional/data/reporting requirement
→ User story
→ Business rule
→ Risk and control
→ UAT test case
```

This model supports:

* requirement completeness;
* impact analysis;
* UAT coverage;
* control coverage;
* scope management;
* change assessment;
* business sign-off.

## 3. Business objectives

| Objective ID | Business objective                                         |
|--------------|------------------------------------------------------------|
| BO-001       | Establish a single source of truth for payment exceptions  |
| BO-002       | Ensure clear ownership of all open payment exception cases |
| BO-003       | Standarize exception classification, status, and priority  |
| BO-004       | Improve SLA and aging visibility                           |
| BO-005       | Ensure high-risk and aged cases are escalated              |
| BO-006       | Strengthen investigation, closure, and audit evidence      |
| BO-007       | Improve operational and management reporting               |
| BO-008       | Reduce reliance on manual spreadsheets and email tracking  |
| BO-009       | Improve data quality and consistency                       |
| BO-010       | Support operational risk and control review                |

## 4. Core requirements traceability matrix

| Trace ID | Business objective | Business requirement | Functional/data requirement | User story                     | Business rule                      | Control/risk               | UAT test case                  |
|----------|--------------------|----------------------|-----------------------------|--------------------------------|------------------------------------|----------------------------|--------------------------------|
| RT-001   | BO-001             | BRQ-001              | FR-001, FR-002, DR-001      | US-001                         | BR-001, BR-002                     | R-001, C-001               | TC-001                         |
| RT-002   | BO-001             | BRQ-001              | FR-003, DR-002 to DR-008    | US-002                         | BR-003 to BR-006                   | R-002, C-002               | TC-002                         |
| RT-003   | BO-002             | BRQ-002              | FR-006, DR-011              | US-003                         | BR-039 to BR-043                   | R-003, C-003               | TC-006                         |
| RT-004   | BO-002             | BRQ-002              | FR-017, CR-006              | US-011                         | BR-040, BR-041                     | R-003, C-003               | TC-007                         |
| RT-005   | BO-003             | BRQ_003              | FR-004, DR-008              | US-002                         | BR-004, BR-075 to BR-078           | R-014, C-014               | TC-003                         |
| RT-006   | BO-003             | BRQ-003              | FR-005, DR-009              | US-004                         | BR-007 to BR-016                   | R-012, R-013, C-012, C-013 | TC-004, TC-005, TC-027         |
| RT-007   | BO-003             | BRQ-003              | FR-007, DR-010              | US-013                         | BR-017 to BR-024                   | R-004, C-004               | TC-008, TC-028                 |
| RT-008   | BO-004             | BRQ-004              | FR-008, DR-013              | US-006                         | BR-025, BR-026, BR-031, BR-032     | R-007, C-007               | TC-010                         |
| RT-009   | BO-004             | BRQ-004              | FR-009, DR-014              | US-007                         | BR-027 to BR-030                   | R-007, C-007               | TC-011                         |  
| RT-010   | BO-004             | BRQ-004              | FR-010, DR-015              | US-014                         | BR-033 to BR-038                   | R-008, C-008               | TC-012, TC-013                 | 
| RT-011   | BO-005             | BRQ-005              | FR-012, DR-016              | US-008                         | BR-045 to BR-051                   | R-009, R-016, C-009, C-016 | TC-014                         |
| RT-012   | BO-005             | BRQ-005              | FR-018, CR-003 to CR-005    | US-008, US-012                 | BR-045 to BR-050                   | R-005 to R-009             | TC-014, TC-023                 |
| RT-013   | BO-006             | BRQ-006              | FR-011, DR-017              | US-005                         | BR-043, BR-054, BR-062             | R-010, C-010               | TC-015, TC-016                 |
| RT-014   | BO-006             | BRQ-006              | FR-013, DR-018, DR-019      | US-009                         | BR-052 to BR-058                   | R-010, R-011, C-010, C-011 | TC-017, TC-018                 |
| RT-015   | BO-006             | BRQ-006              | FR-016, CR-007, CR-008      | US-005                         | BR-059 to BR-065                   | R-015, C-015               | TC-019                         |
| RT-016   | BO-007             | BRQ-007              | RR-001 to RR-004            | US-010, US-012                 | BR-066 to BR-069                   | R-017, C-017               | TC-021, TC-022, TC-025         | 
| RT-017   | BO-007             | BRQ-007              | RR-005, RR-006              | US-012                         | BR-070, BR-071                     | R-017, C-017               | TC-025                         |
| RT-018   | BO-007             | BRQ-007              | RR-007                      | US-003, US-011                 | BR-072                             | R-003, R-017               | TC-024                         |
| RT-019   | BO-007             | BRQ-007              | RR-008, DR-018, DR-020      | US-009, US-012                 | BR-057, BR-073                     | R-011, R-017               | TC-025                         |
| RT-020   | BO-007             | BRQ-007              | RR-009                      | US-012                         | BR-074                             | R-017, C-017               | TC-025                         | 
| RT-021   | BO-008             | BRQ-001, BRQ-007     | NFR-004, NFR-005            | US-010, US-012                 | BR-066 to BR-074                   | R-017, C-017               | TC-020, TC-030                 |
| RT-022   | BO-009             | BRQ-003              | DQ-001 to DQ-012            | US-001, US-002, US-009         | BR-001 to BR-006, BR-052 to BR-058 | R-002, R-019, C-002, C-019 | TC-002, TC-027, TC-028, TC-029 |
| RT-023   | BO-010             | BRQ-005, BRQ-006     | CR-001 to CR-008            | US-005, US-008, US-009, US-012 | BR-045 to BR-065                   | R-009 to R-019             | TC-014 to TC-019, TC-025       |

## 5. User story traceability

| User Story ID | User story summary                | Related requirements                   | Related business rules         | Related controls           | UAT coverage           |
|---------------|-----------------------------------|----------------------------------------|--------------------------------|----------------------------|------------------------|
| US-001        | Create payment exception case     | FR-001, FR-002, DR-001, DR-012         | BR-001, BR-002, BR-007         | C-001                      | TC-001                 |
| US-002        | Capture payment exception details | FR-003, FR-004, DR-002 to DR-008       | BR-003 to BR-006               | C-002, C-014               | TC-002, TC-003         |
| US-003        | Assign case owner                 | FR-006, DR-011, CR-006                 | BR-039 to BR-043               | C-003                      | TC-006                 |
| US-004        | Update case status                | FR-005, DR-009                         | BR-007 to BR-016               | C-012, C-013               | TC-004, TC-005, TC-027 |
| US-005        | Add investigation notes           | FR-011, DR-017, CR-002                 | BR-043, BR-054, BR-062         | C-010, C-015               | TC-015, TC-016, TC-019 | 
| US-006        | Calculate SLA due date            | FR-008, DR-013                         | BR-025, BR-026, BR-031, BR-032 | C-007                      | TC-010                 |
| US-007        | Flag SLA breaches                 | FR-009, DR-014, CR-004                 | BR-027 to BR-030               | C-007, C-009               | TC-011                 | 
| US-008        | Escalate high-risk or aged case   | FR-012, DR-016, CR-003 to CR-005       | BR-037, BR-045 to BR-051       | C-005, C-006, C-009, C-016 | TC-009, TC-014, TC-023 |
| US-009        |  Close case with closure reason   | FR-013, DR-018, DR-019, CR-001, CR-002 | BR-052 to BR-058               | C-010, C-011               | TC-016, TC-017, TC-018 |
| US-010        | Filter exception queue            | FR-015, RR-001 to RR-004               | BR-066 to BR-069               | C-007, C-008               | TC-020                 |
| US-011        | View unassigned cases             | FR-017, CR-006                         | BR-040, BR-041                 | C-003                      | TC-007                 |
| US-012        | View management reporting summary | RR-001 to RR-009                       | BR-066 to BR-074               | C-017, C-018               | TC-021 to TC-026       |
| US-013        | Update case priority              | FR-007, DR-010, CR-003, CR-008         | BR-017 to BR-024               | C-004, C-005               | TC-008, TC-028         |
| US-014        | Identify aged payment exception   | FR-010, DR-015, RR-003, CR-005         | BR-033 to BR-038               | C-008                      | TC-012, TC-013, TC-022 |

## 6. Control traceability

| Control ID | Control activity               | Related risk | Related requirements           | Business rule        | UAT evidence                             |
|------------|--------------------------------|--------------|--------------------------------|----------------------|------------------------------------------|
| C-001      | Unique case creation           | R-001        | FR-001, FR-002, DR-001         | BR-001, BR-002       | TC-001                                   | 
| C-002      | Mandatory field validation     | R-002        | FR-003, DR-002 to DR-008       | BR-003 to BR-006     | TC-002                                   |
| C-003      | Unassigned case monitoring     | R-003        | FR-006, FR-017, CR-006         | BR-039 to BR-042     | TC-006, TC-007                           |  
| C-004      | Priority required control      | R-004        | FR-007, DR-010                 | BR-017, BR-024       | TC-008, TC-028                           |
| C-005      | High-value case control        | R-005        | CR-003, DR-004                 | BR-019, BR-047       | TC-008                                   |
| C-006      | Duplicate risk escalation      | R-006        | CR-003, DR-016                 | BR-020, BR-047       | TC-009                                   |
| C-007      | SLA breach flag                | R-007        | FR-008, FR-009, DR-013, DR-014 | BR-025 to BR-032     | TC-010, TC-011, TC-021                   |
| C-008      | Aged exception flag            | R-008        | FR-010, DR-015, CR-005         | BR-033 to BR-038     | TC-012, TC-013, TC-022                   |
| C-009      | Escalation control             | R-009        | FR-012, FR-018                 | BR-045 to BR-051     | TC-014, TC-023                           | 
| C-010      | Investigation note requirement | R-010        | FR-011, DR-017, CR-002         | BR-054               | TC-015, TC-016                           | 
| C-011      | Closure reason requirement     | R-011        | FR-013, DR-018, CR-001         | BR-053, BR-056       | TC-017, TC-018                           |
| C-012      | Status transition validation   | R-012        | FR-005, FR-014                 | BR-007 to BR-016     | TC-004, TC-005                           |
| C-013      | Controlled status values       | R-013        | FR-005, DR-009, DQ-005         | BR-007 to BR-016     | TC-027                                   |
| C-014      | Controlled exception taxonomy  | R-014        | FR-004, DR-008, DQ-007         | BR-075 to BR-078     | TC-003                                   |
| C-015      | Case history retention         | R-015        | FR-016, CR-007, CR-008         | BR-059 to BR-065     | TC-019                                   | 
| C-016      | Escalation reason requirement  | R-016        | FR-012, DR-016                 | BR-049, BR-051       | TC-014, TC-023                           |
| C-017      | Management reporting           | R-017        | RR-001 to RR-009               | BR-066 to BR-074     | TC-025                                   |
| C-018      | Control evidence reporting     | R-018        | CR-001 to CR-008               | BR-066 to BR-074     | TC-026                                   |
| C-019      | Data quality checks            | R-019        | DQ-001 to DQ-012               | Relevant field rules | TC-002, TC-027 to TC-029                 |
| C-020      | Customer impact flag           | R-020        | customer_impact_flag, BR-021   | BR-021               | included in future detailed UAT coverage |

## 7. Reporting traceability

| Report ID | Report name             | Related requirements             | Related metrics    | Supporting business rules          | UAT coverage             |
|-----------|-------------------------|----------------------------------|--------------------|------------------------------------|--------------------------|
| RPT-001   | Exception Queue         | FR-015, RR-001 to RR-004         | M-001 to M-009     | BR-066 to BR-069                   | TC-020                   |
| RPT-002   | Team Lead Control View  | FR-017, FR-018, RR_001 to RR_007 | M-001 to M-013     | BR-039 to BR-051, BR-066 to BR-072 | TC-007, TC-021 to TC-024 |
| RPT-003   | Management Summary      | RR-001 to RR-009                 | M-001 to M-019     | BR-066 to BR-074                   | TC-025                   | 
| RPT-004   | SLA Breach Report       | FR-008, FR-009, RR-004           | M-006              | NR-025 to BR-032                   | TC-011, TC-021           |
| RPT-005   | Aged Exceptions Report  | FR-010, RR-003                   | M-004, M-005       | BR-033 to BR-038                   | TC-012, TC-013, TC-022   |
| RPT-006   | Escalation Report       | FR-012, FR-018                   | M-008              | BR-045 to BR-051                   | TC-014, TC-023           |  
| RPT-007   | Owner Workload Report   | FR-006, FR-017, RR-007           | M-009, M-013       | BR-039 to BR-044                   | TC-007, TC-024           | 
| RPT-008   | Exception Trend Report  | RR-005, RR-006, RR-009           | M-010 to M-012     | BR-070, BR-071, BR-074             | TC-025                   |
| RPT-009   | Closure Analysis Report | RR-008, DR-018 to DR-020         | M-014 to M-016     | BR-052 to BR-058, BR-073           | TC-018, TC-025           |
| RPT-010   | Control Evidence Report | CR-001 to CR-008                 | KCI-001 to KCI-012 | BR-045 to BR-065                   | TC-026                   |

## 8. UAT coverage summary 

| Requirement area     | UAT test cases         | Coverage status |
|----------------------|------------------------|-----------------|
| Case creation        | TC-001                 | Covered         |
| Mandatory data       | TC-002                 | Covered         |
| Exception taxonomy   | TC-003                 | Covered         |
| Status lifecycle     | TC-004, TC-005, TC-027 | Covered         |
| Ownership            | TC-006, TC-007         | Covered         |
| Priority             | TC-008, TC-028         | Covered         |
| Duplicate risk       | TC-009                 | Covered         |
| SLA calculation      | TC-010                 | Covered         |
| SLA breach logic     | TC-011, TC-21          | Covered         |
| Aging                | TC-012, TC-013, TC-022 | Covered         |
| Escalation           | TC-014, TC-023         | Covered         |
| Investigation notes  | TC-015, TC-016         | Covered         |
| Closure controls     | TC-016 to TC-018       | Covered         |
| Audit history        | TC-019                 | Covered         |
| Queue filtering      | TC-020                 | Covered         |
| Workload reporting   | TC-024                 | Covered         |
| Management reporting | TC-025                 | Covered         |
| Control reporting    | TC-026                 | Covered         |
| Data quality         | TC-027 to TC-029       | Covered         |
| CSV export           | TC-030                 | Covered         |    

## 9. Requirement coverage status

| Requirement category        | Requirement range  | Coverage status                                                  |
|-----------------------------|--------------------|------------------------------------------------------------------|
| Business requirements       | BRQ-001 to BRQ-007 | Covered                                                          |
| Functional requirements     | FR-001 to FR-018   | Covered                                                          |
| Non-functional requirements | NFR-001 to NFR-006 | Partially covered through design and UAT assumptions             |
| Data requirements           | DR-001 to DR-020   | Covered                                                          |
| Reporting requirements      | RR-001 to RR-009   | Covered                                                          |
| Control requirements        | CR-001  to CR-008  | Covered                                                          |
| Data quality rules          | DQ-001 to DQ-012   | Covered or planned for control reporting                         |
| Export requirements         | EXP-001 to EXP-004 | Partially covered                                                |
| Refresh requirements        | REF-001 to REF-005 | Defined; implementation validation remains environment-dependent | 

## 10. Identified coverage gaps 

| Gap ID  | Gap                                                                 | Impact                                                    | Proposed action                                          |
|---------|---------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------|
| GAP-001 | Public holiday handling is not fully defined for SLA calculation    | SLA dates may vary by jurisdiction                        | Resolve open question before implementation              |
| GAP-002 | Reopen workflow is not included in standard status lifecycle        | Closed case correction process remains undefined          | Define future-state reopen rules                         |
| GAP-003 | Customer-impacting case workflow has limited dedicated UAT coverage | Customer-risk handling may require additional validation  | Add detailed user story and test case if included in MVP |
| GAP-004 | Role-based access is out of implementation scope                    | Access control requirements are not tested                | Define future non-functional and security requirements   | 
| GAP-005 | External waiting time treatment is unresolved                       | SLA breach calculation may not reflect operational policy | Confirm whether SLA pauses during external dependency    |
| GAP-006 | High-value currency conversion logic is not fully defined           | High-value flag may be inconsistent across currencies     | Define FX source and conversion date                     |
| GAP-007 | Export testing currently focuses on exception queue                 | Other reporting exports are not fully covered             | Add export test cases if included in delivery scope      |

## 11. Change impact assessment guidance

When a requirement changes, the following linked artefacts should be reviewed

| Change type             | Artefacts requiring review                                                        |
|-------------------------|-----------------------------------------------------------------------------------|
| Status lifecycle change | Requirements catalog, user stories, business rules, diagrams, UAT cases, controls |
| Priority rule change    | Business rules, SLA logic, reporting, controls, UAT                               |
| SLA rule change         | Business rules, data dictionary, reporting requirements, control matrix, UAT      |
| New exception type      | Data dictionary, business rules, reporting requirements, test data                |
| Closure rule change     | User stories, business rules, control matrix, UAT                                 |
| New report requirement  | Reporting requirements, data dictionary, UAT, traceability                        |
| New mandatory field     | Requirements catalog, data dictionary, business rules, UAT                        |
| New control requirement | Risk and controls matrix, reporting requirements, UAT, traceability               |

## 12. Traceability maintenance approach

The traceability matrix should be updated when

* a new requirement is added;
* a requirement changes;
* a user story is added or removed;
* a business rule changes;
* a new control is introduced;
* a UAT test case is added or updated;
* a reporting requirement changes;
* project scope changes.

Recommended ownership:

| Activity                             | Owner                             |
|--------------------------------------|-----------------------------------|
| Maintain requirement link            | Business Analyst                  |
| Confirm business objective alingment | Operations Manager/Product Owner  |
| Confirm control mapping              | Risk/Operational Control          |
| Confirm UAT coverage                 | Business Analyst/QA               |
| Approve requirement changes          | Business Owner/Product Owner      |
| Confirm reporting coverage           | Operations Manager/Reporting Team |  

## 13. Summary

This traceability matrix demonstrates how the payment exception management case study connects business objectives to requirements, user stories, business rules, risks, controls, reports, and UAT test cases.

The matrix supports requirement completeness, control coverage, testing readiness, change impact analysis, and business sign-off.

It should be maintained alongside the requirements catalog, user stories, business rules, data dictionary, reporting requirements, risk and controls matrix, and UAT plan.