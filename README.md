# Payment Exception Management BA Case Study

Business Analyst portfolio case study for a payment exception management workflow in financial services.

The project demonstrates how an operational problem can be translated into:

- business and functional requirements;
- current-state and target-state processes;
- user stories and acceptance criteria;
- business rules;
- data and reporting requirements;
- risks and controls;
- User Acceptance Testing (UAT);
- requirements traceability;
- conceptual wireframes;
- sample operational data;
- validated CSV working outputs.

This is a documentation-led case study rather than a production application.

## Project overview

Payment exceptions are often managed across spreadsheets, emails, reports, and individual team trackers.

This creates several operational risks:

- unclear ownership;
- inconsistent exception classification;
- limited Service Level Agreement (SLA) visibility;
- aged cases remaining unresolved;
- inconsistent escalation;
- incomplete investigation and closure evidence;
- unreliable management reporting;
- limited audit trail.

The proposed target workflow introduces a centralized payment exception case-management process with controlled statuses, priorities, ownership, SLA monitoring, escalation rules, investigation evidence, closure controls, and management reporting.

## Business objectives

The proposed solution aims to:

1. establish a single source of truth for payment exceptions;
2. assign clear ownership to open cases;
3. standardize exception classification, status, and priority;
4. improve SLA and aging visibility;
5. escalate high-risk and overdue cases;
6. retain investigation and closure evidence;
7. improve operational and management reporting;
8. reduce reliance on spreadsheets and email tracking;
9. improve data quality;
10. support operational risk and control review.

## Target workflow

The conceptual case lifecycle is:

```text
New
  ↓
In Review
  ├── Pending External Response
  ├── Escalated
  └── Resolved
          ↓
        Closed
```

The workflow prevents direct movement from `New` to `Closed`.

A case can only be closed after:

- investigation notes have been recorded;
- the case has reached `Resolved` status;
- a controlled closure reason has been selected;
- the required closure information has been completed.

## Key project artefacts

### Business analysis documentation

| Document                                                           | Description                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Business Case](docs/01_business_case.md)                          | Defines the business problem, objectives, expected benefits, scope, assumptions, and constraints    |
| [Current-State Process](docs/02_current_state_process.md)          | Describes the fragmented manual exception-management process and its pain points                    |
| [Target-State Process](docs/03_target_state_process.md)            | Defines the proposed centralized exception-management workflow                                      |
| [Stakeholder Analysis](docs/04_stakeholder_analysis.md)            | Identifies project stakeholders, responsibilities, influence, and engagement needs                  |
| [Requirements Catalog](docs/05_requirements_catalog.md)            | Contains business, functional, non-functional, data, reporting, and control requirements            |
| [User Stories](docs/06_user_stories.md)                            | Contains user stories and Gherkin-style acceptance criteria                                         |
| [Business Rules](docs/07_business_rules.md)                        | Defines lifecycle, priority, SLA, aging, ownership, escalation, closure, audit, and reporting rules |
| [Data Dictionary](docs/08_data_dictionary.md)                      | Defines payment exception fields, formats, example values, and data-quality rules                   |
| [Reporting Requirements](docs/09_reporting_requirements.md)        | Defines operational reports, management information, metrics, refresh, and export requirements      |
| [Risk and Controls Matrix](docs/10_risk_and_controls_matrix.md)    | Maps operational risks to preventive and detective controls                                         |
| [UAT Plan](docs/11_uat_plan.md)                                    | Defines UAT scope, roles, entry and exit criteria, defect handling, and 30 test cases               |
| [Requirements Traceability Matrix](docs/12_traceability_matrix.md) | Links objectives, requirements, user stories, rules, risks, controls, reports, and UAT tests        |

### Process diagrams

The [`diagrams`](diagrams/) directory contains Mermaid diagrams representing:

- the current-state process;
- the target-state process;
- the payment exception status lifecycle.

### Conceptual wireframes

| Wireframe                                                            | Purpose                                                                        |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Exception Queue](wireframes/exception_queue_wireframe.md)           | Operational queue for reviewing, filtering, assigning, and prioritizing cases  |
| [Exception Detail](wireframes/exception_detail_wireframe.md)         | Detailed case investigation, escalation, resolution, closure, and audit view   |
| [Management Dashboard](wireframes/management_dashboard_wireframe.md) | Management view covering volumes, SLA, aging, escalation, workload, and trends |

The wireframes are low-fidelity business concepts rather than production user interface designs.

## Requirements coverage

The case study includes:

| Requirement area            | Coverage |
|-----------------------------|----------|
| Business requirements       | 7        |
| Functional requirement      | 18       |
| Non-functional requirements | 6        |
| Data requirements           | 20       |
| Reporting requirements      | 9        |
| Control requirements        | 8        |
| Data-quality rules          | 12       |
| Business rules              | 78       |
| User stories                | 14       |
| UAT test cases              | 30       |
| Risks and controls          | 20       |
| Core traceability records   | 23       |

## Sample data

The project includes a fictional payment exception dataset:

[View sample payment exception data](sample_data/payment_exceptions_sample.csv)

The dataset contains 18 scenarios, including:

- bank and Payment Service Provider (PSP) rejections;
- returned and unmatched payments;
- delayed settlements;
- missing references;
- incorrect amount and currency cases;
- duplicate payment risk;
- high-value cases;
- SLA breaches;
- aged exceptions;
- escalated cases;
- unassigned cases;
- resolved and closed cases.

All data is fictional and created solely for demonstration purposes.

The static dataset uses `2025-02-14` as its reporting snapshot date.

Business-day calculations assume Monday to Friday and do not include public-holiday calendars.

## Working CSV outputs

The Markdown documentation is supported by CSV versions of key working artefacts:

| Output                                                                                       | Purpose                                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [Risk and Controls Matrix CSV](output_examples/risk_controls_matrix.csv)                     | Spreadsheet-ready risk, control, ownership, evidence, and UAT mapping             |
| [UAT Test Cases CSV](output_examples/uat_test_cases.csv)                                     | Execution-ready UAT tracker with status, actual result, defect, and retest fields |
| [Requirements Traceability Matrix CSV](output_examples/requirements_traceability_matrix.csv) | Spreadsheet-ready end-to-end traceability output                                  |

Within multi-value CSV fields:

- `|` separates individual identifiers;
- `:` represents an inclusive identifier range.

For example:

```text
TC-010|TC-011|TC-021
```

represents three specific test cases, while:

```text
DR-002:DR-008
```

represents the range from `DR-002` to `DR-008`.

## Python validation

The repository contains Python scripts that validate the sample dataset and CSV outputs.

### Requirements

- Python 3.9 or newer;
- no external Python packages are required.

### Validate the sample dataset

```bash
python3 scripts/validate_sample_data.py
```

The script checks:

- whether the file and header exist;
- column consistency;
- unique case identifiers;
- controlled status and priority values;
- `Yes` and `No` flag values;
- closure requirements;
- SLA due dates for open cases;
- high-value priority rules;
- duplicate-risk priority rules.

### Validate output examples

```bash
python3 scripts/validate_output_examples.py
```

The script checks:

- required columns;
- expected row counts;
- unique identifiers;
- identifier formats;
- controlled risk, control, UAT, and coverage values;
- UAT execution-state consistency;
- completeness of risk, control, test-case, and traceability records.

A successful run ends with:

```text
All output example CSV files passed validation.
```

The scripts return exit code `0` after successful validation and `1` when errors are detected, allowing them to be used in future automated checks.

## Repository structure

```text
payments-exception-management-ba/
├── diagrams/
├── docs/
│   ├── 01_business_case.md
│   ├── 02_current_state_process.md
│   ├── 03_target_state_process.md
│   ├── 04_stakeholder_analysis.md
│   ├── 05_requirements_catalog.md
│   ├── 06_user_stories.md
│   ├── 07_business_rules.md
│   ├── 08_data_dictionary.md
│   ├── 09_reporting_requirements.md
│   ├── 10_risk_and_controls_matrix.md
│   ├── 11_uat_plan.md
│   └── 12_traceability_matrix.md
├── output_examples/
│   ├── requirements_traceability_matrix.csv
│   ├── risk_controls_matrix.csv
│   └── uat_test_cases.csv
├── sample_data/
│   └── payment_exceptions_sample.csv
├── scripts/
│   ├── validate_output_examples.py
│   └── validate_sample_data.py
├── wireframes/
│   ├── exception_detail_wireframe.md
│   ├── exception_queue_wireframe.md
│   └── management_dashboard_wireframe.md
└── README.md
```

## Recommended review path

For a concise review of the project:

1. Read the [Business Case](docs/01_business_case.md).
2. Compare the [Current-State Process](docs/02_current_state_process.md) with the [Target-State Process](docs/03_target_state_process.md).
3. Review the [Requirements Catalog](docs/05_requirements_catalog.md).
4. Review the [User Stories](docs/06_user_stories.md) and [Business Rules](docs/07_business_rules.md).
5. Open the [Exception Queue](wireframes/exception_queue_wireframe.md) and [Exception Detail](wireframes/exception_detail_wireframe.md) wireframes.
6. Review the [Risk and Controls Matrix](docs/10_risk_and_controls_matrix.md).
7. Review the [UAT Plan](docs/11_uat_plan.md).
8. Finish with the [Requirements Traceability Matrix](docs/12_traceability_matrix.md).
9. Run the Python validation scripts.

## Skills demonstrated

This case study demonstrates practical experience in:

- business problem definition;
- current-state and target-state analysis;
- process modelling;
- requirements elicitation and documentation;
- functional and non-functional requirements;
- user stories and acceptance criteria;
- business-rule definition;
- data dictionary design;
- reporting and KPI requirements;
- risk and control analysis;
- UAT planning;
- requirements traceability;
- low-fidelity wireframing;
- sample-data preparation;
- Python-based data validation;
- financial-services and payment-operations domain analysis.

## Assumptions and limitations

This project is based on a fictional organization and conceptual workflow.

The following items are outside the implemented scope:

- real bank or PSP integrations;
- production payment processing;
- authentication and role-based access;
- production database design;
- real customer or payment data;
- external communication functionality;
- automated case creation;
- file attachments;
- reopen workflow;
- public-holiday calendars;
- configurable SLA rules;
- live dashboard implementation;
- performance and security testing.

Several areas would require additional analysis before implementation, including:

- public-holiday treatment;
- jurisdiction-specific business calendars;
- foreign-exchange logic for high-value thresholds;
- SLA treatment during external-party delays;
- role-based permissions;
- data-retention requirements;
- controlled case reopening;
- integration and source-system ownership.

## Disclaimer

This repository is a fictional portfolio case study.

It does not contain confidential employer information, production system details, real customer data, or real payment records.

The processes, requirements, controls, data, and wireframes were created for demonstration and educational purposes.