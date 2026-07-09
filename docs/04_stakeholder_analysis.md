# Stakeholder Analysis

## 1. Purpose

This document identifies the key stakeholders involved in the payment exception management process improvement project.

The purpose of stakeholder analysis is to clarify who is impacted by the process, who provides requirements, who approves the target workflow, and who consumes the reporting outputs.

## 2. Stakeholder overview

| Stakeholder                   | Role in process                                                                                    | Interest / concern                                                             | Involvement level |
|-------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------|
| Payments Operations Analyst   | Investigates and resolves payment exceptions                                                       | Needs clear queue, ownership, status, notes, SLA, and closure process          | High              |
| Payments Operations Team Lead | Oversees daily workload and escalations                                                            | Needs visibility of aged, high-priority, and unassigned cases                  | High              |
| Payments Operations Manager   | Owns operational performance and control environment                                               | Needs management reporting, SLA visibility, and risk indicators                | High              |
| Finance Operations            | Reviews financial impact of failed, returned, or unresolved payments                               | Needs accurate exception classification and resolution evidence                | Medium            |
| Reconciliation Team           | Identifies payment-related breaks during reconciliation                                            | Needs clear handoff process for payment exceptions                             | Medium            |
| Customer Support              | Receives customer queries related to payment issues                                                | Needs payment exception status updates and resolution outcomes                 | Medium            |
| Risk / Operational Control    | Reviews process risks, controls, and escalation evidence                                           | Needs audit trail, SLA monitoring, and control reporting                       | Medium            |
| Compliance                    | Reviews regulatory or customer-impacting payment issues where relevant                             | Needs visibility of sensitive or high-risk payment exceptions                  | Low/Medium        |
| Technology / Product Team     | Implements the target workflow or system changes                                                   | Needs clear requirements, data fields, business rules, and acceptance criteria | High              |
| Data / Reporting Team         | Supports operational and management reporting                                                      | Needs reporting definitions, fields, metrics, and data logic                   | Medium            |
| External Bank / PSP           | Provides payment statuses, rejection reasons, settlement confirmations, or investigation responses | Needs clear queries and consistenct case references                            | External          |

## 3. Stakeholder needs

# Payments Operations Analyst

Needs:

* one place to view open exceptions;
* clear case ownership;
* standardized exception statuses;
* ability to add investigation notes;
* ability to filter by priority, status, payment channel, and due date;
* clear closure requirements.

Pain points:

* manual spreadsheet tracking;
* duplicated follow-ups;
* inconsistent status updates;
* unclear prioritization.

# Payments Operations Team Lead

Needs:

* visibility of team workload;
* unassigned case monitoring;
* SLA breach monitoring;
* aged exception reporting;
* escalation queue;
* ability to review high-priority cases.

Pain points:

* manual workload checks;
* limited real-time visibility;
* escalations may be missed;
* daily reporting takes too much time.

# Payments Operations Manager

Needs:

* summary of open, aged, breached, and closed exceptions;
* trend reporting by exception type and payment channel;
* evidence that operational controls are working;
* visibility of recurring root causes;
* consistent reporting for senior stakeholders.

Pain points:

* reporting depends on manual spreadsheet updates;
* difficult to evidence control effectiveness;
* limited management-level insight into exception drivers.

# Technology  / Product Team

Needs:

* clear functional requirements;
* status model;
* business rules;
* data dictionary;
* acceptance criteria;
* testable requirements;
* clear scope boundaries.

Pain points:

* unclear requirements create rework;
* ambiguous status and priority logic;
* lack of traceability between business objectives and requested features.

# Risk / Operational Control

Needs:

* defined controls for high-risk payment exceptions;
* audit trail for investigation and closure;
* SLA breach evidence;
* escalation rules;
* reporting on aged and high-value cases.

Pain points:

* inconsistent evidence;
* manual controls are difficult to prove;
* closure may happen without sufficient notes or reason.

## 4. RACI matrix

| Activity                     | Payments Analyst | Team Lead | Operations Manager | Technology / Product | Risk / Control | Reporting Team |
|------------------------------|------------------|-----------|--------------------|----------------------|----------------|----------------|
| Define current process       | R                | A         | C                  | C                    | C              | C              |
| Define Target process        | R                | A         | C                  | C                    | C              | C              |
| Define business requirements | R                | A         | C                  | R                    | C              | C              |
| Approve requirements         | C                | R         | A                  | C                    | C              | C              |
| Define business rules        | R                | A         | C                  | C                    | C              | C              |
| Define reporting needs       | C                | R         | A                  | C                    | C              | R              | 
| Define control requirements  | C                | R         | C                  | C                    | A              | C              |
| Build / configure solution   | I                | C         | I                  | R/A                  | C              | C              |
| Prepare UAT test cases       | R                | A         | C                  | C                    | C              | C              |
| Execute UAT                  | R                | A         | C                  | C                    | C              | C              |
| Sign off UAT                 | C                | R         | A                  | C                    | C              | C              |

Legend:

* R = Responsible
* A = Accountable
* C = Consulted
* I = Informed

## 5. Communication considerations

The project requires regular communication between business and technology stakeholders.

Recommended communication approach:

| Meeting / Artefact    | Audience                                          | Purpose                                    | Frequency                   |
|-----------------------|---------------------------------------------------|--------------------------------------------|-----------------------------|
| Requirements workshop | Operations, Team Lead, Product/Technology         | Gather and validate requirements           | Weekly during discovery     |
| Process review        | Operations, Team Lead, Manager                    | Confirm current and target process         | As needed                   |
| Controls review       | Risk/Control, Operations Manager                  | Validate risk and control requirements     | Once per major scope change |
| UAT planning session  | Operations, Product/Technology, QA                | Confirm test cases and acceptance criteria | Before UAT                  |
| UAT defect review     | Operations, Product/Technology                    | Review failed test cases and defects       | During UAT                  |
| Sign-off meeting      | Operations Manager, Team Lead, Product/Technology | Confirm readiness and acceptance           | End of UAT                  |

## 6. Key stakeholder risks

| Risk                                            | Impact                                                   | Mitigation                                                  |
|-------------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------|
| Stakeholders disagree on status definitions     | Inconsistent workflow design                             | Run status lifecycle review and document agreed definitions |
| Operations requirements are too broad           | Scope creep                                              | Separate MVP requirements from future enhancements          |
| Reporting requirements are unclear              | Dashboard/reporting output may not meet management needs | Define metrics and report fields explicitly                 |
| Control requirements are identified too late    | Rework during UAT or audit review                        | Involve Risk/Control during requirement phase               |
| Technology team receives ambiguous requirements | Build defects or rework                                  | Use testable requirements and acceptance criteria           |
| UAT users are not available                     | Delayed sign-off                                         | Agree UAT owners and timeline early                         |