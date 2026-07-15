# Payment Exception Queue Wireframe

## 1. Purpose

This document presents a conceptual wireframe for the payment exception queue.

The exception queue is the primary operational view used by Payments Operations Analysts and Team Leads to review, prioritize, assign, investigate, and monitor paymen exception cases.

The wireframe is not a production user interface design. It illustrates how documented requirements, business rules, reporting needs, and operational controls could be represented in a business-facing screen.

## 2. Primary users

* Payments Operations Analyst
* Payments Operations Team Lead
* Payments Operations Manager
* Risk/Operational Control reviewe

## 3. Main user objectives

The exception queue should allow users to:

* Identify cases requiring immediate action;
* filter and sort payment exception;
* review SLA breaches and aged cases;
* identify unassigned cases;
* identify High and Critical priority cases;
* open individual cases for investigation;
* review workload by owner or team queue;
* export filtered results.

## 4. Conceptual layout

```text
+------------------------------------------------------------------------------------------------+
| PAYMENT EXCEPTION MANAGEMENT                                                                   |
+------------------------------------------------------------------------------------------------+
| Open: 128 | SLA Breaches: 14 | Aged: 22 | High/Critical: 11                                    |
| Unassigned: 6 | Escalated: 8                                                                   |
+------------------------------------------------------------------------------------------------+
| FILTERS                                                                                        |
| Status: [All ▾]      Priority: [All ▾]     Owner: [All ▾]                                      |
| Type: [All ▾]        Channel: [All ▾]      SLA Breach: [All ▾]                                 |
| Aging: [All ▾]       Escalated: [All ▾]                                                        |
|                                                                                                |
| [Apply Filters]  [Clear Filters]  [Export CSV]  [Create Case]                                  |
+------------------------------------------------------------------------------------------------+
| CASE-000145 | Bank Rejection    | Critical    | Escalated              | Analyst A             |
| 125,000 EUR | SLA: Breached     | Age: 8 days | Bank Transfer                                  |
+------------------------------------------------------------------------------------------------+
| CASE-000149 | PSP Rejection     | High        | In Review              | Analyst B             |
| 12,500 EUR  | SLA: Due Today    | Age: 3 days | Customer Impact                                |
+------------------------------------------------------------------------------------------------+
| CASE-000151 | Missing Reference | Medium      | New                    | Unassigned            |
| 920 GBP     | SLA: Tomorrow     | Age: 1 day  | Digital Payments Queue                         |
+------------------------------------------------------------------------------------------------+
| Showing 1-25 of 128                                              [Previous] 1 / 6 [Next]       |
+------------------------------------------------------------------------------------------------+
```

## 5. KPI cards

| KPI           | Definition                                                               | Related requirement |
|---------------|--------------------------------------------------------------------------|---------------------|
| Open cases    | Count of cases where status is not ```text Closed```                     | RR-001              |
| SLA Breaches  | Count of open cases where SLA breach flag = Yes                          | RR-004              |
| Aged Cases    | Count of open cases older than 5 business days                           | RR-003              |
| High/Critical | Count of open High or Critical priority cases                            | CR-003              |
| Unassigned    | Count of open cases without owner or team queue                          | FR-017, CR-006      |
| Escalated     | Count of cases with status ```text Escalated``` or escalation flag = Yes | FR-018              |

## 6. Queue columns

| Column            | Description                             | Related field        |
|-------------------|-----------------------------------------|----------------------|
| Case ID           | Unique exception case identifier        | case_id              |
| Payment Reference | Internal or external payment reference  | payment_reference    |
| Exception Type    | Controlled exception category           | exception_type       |
| Amount/Currency   | Payment amound and ISO currency         | amount_currency      |
| Payment Channel   | Channel used for payment processing     | payment_channel      |
| Status            | Current lifecycle status                | status               |
| Priority          | Current operational priority            | priority             |
| Owner             | Assigned analyst or queue               | owner_team_queue     |
| SLA Due Date      | Resolution deadline                     | sla_due_date         |
| SLA Breach Flag   | Indicates whether SLA has been breached | sla_breach_flag      |
| Days Open         | Number of business days open            | days_open            |
| Aging Bucket      | Aging category                          | aging_bucket         |
| Escalation Flag   | Indicates whether case is escalated     | escalation_flag      |
| Customer Impact   | Indicates customer or client impact     | customer_impact_flag |  

## 7. Filters

The queue should support the following filters:

| Filter           | Type         | Example values                                                 |
|------------------|--------------|----------------------------------------------------------------|
| Status           | Multi-select | New, In Review, Pending External Response, Escalated, Resolved |
| Priority         | Multi-select | Low, Medium, High, Critical                                    |
| Owner            | Multi-select | Individual analyst names                                       |
| Team Queue       | Multi-select | Bank Transfer, Card Payments, Digital Wallets                  |
| Exception Type   | Multi-select | BankRejection, PSP Rejection, Duplicate Payment Risk           |
| Payment Channel  | Multi-select | Bank Transfer, Card, Wallet, PSP                               |
| Exception Source | Multi-select | Bank File, PSP Report, Reconciliation                          |
| SLA Breach       | Boolean      | Yes, No                                                        |
| Aging Bucket     | Multi-select | 0-2 days, 3-5 days, 6-10 days, 11-30 days, Over 30 days        |
| Escalated        | Boolean      | Yes, No                                                        |
| Customer Impact  | Boolean      | Yes, No                                                        |
| High Value       | Boolean      | Yes, No                                                        |
| Created Date     | Date range   | From/To                                                        |

## 8. Default sorting 

The queue should display the most urgent cases first.

Recommended default sorting:

1. Critical priority cases;
2. High priority SLA-breached cases;
3. Other SLA-breached cases;
4. escalated cases;
5. oldest created date.

Users should also be able to sort by:

* priority;
* SLA due date;
* created date;
* days open;
* amount;
* owner.

## 9. Visual indicators

| Indicator         | Suggestor representation             |
|-------------------|--------------------------------------|
| Critical priority | Strong warning label                 |
| High priority     | High-priority label                  |
| SLA breach        | ```text Breached``` status indicator |
| SLA due today     | ```text DUE TODAY``` indicator       |
| Aged case         | Aging badge showing days open        |
| Escalated case    | Escalation badge                     |
| Unassigned case   | ```text UNASSIGNED``` warning        |
| Customer impact   | Customer impact icon label           |
| High-value case   | High-value flag                      |
| Duplicate risk    | Duplicate-risk warning               |

## 10. Available actions

### Queue-level actions

* Create new case
* Apply filters
* Clear filters
* Export filtered results to CSV
* Save personal filter view 
* Assign selected cases
* Open selected case

### Team Lead actions

* Assign unassigned cases
* Reassing case owner
* Review escalated cases
* Review SLA breaches
* Export daily control view

Bulk status changes should not be included in the MVP because they may weaken investigation and audit controls.

## 11. Row interaction

Selecting a queue row should open the Exception Detail view:

* payment information;
* exception classification;
* current owner and status;
* SLA and aging details;
* investigation notes;
* escalation history;
* case history;
* closure information.

## 12. Empty and error states

| Scenario                           | Expected behavior                                                             |
|------------------------------------|-------------------------------------------------------------------------------|
| No cases match filters             | Display message: ```text No payment exceptions match the selected filters.``` |
| No open exceptions exist           | Display zero-value KPI cards and empty queue message                          |
| Reporting data unavailable         | Display clear data availability warning                                       |
| Export fails                       | Display error message without losing selected filters                         |
| User lacks access                  | Display access restriction message                                            |
| Mandatory source field unavailable | Flag case for data quality review                                             |

## 13. Related requirements

The wireframe supports the following requirements:

* FR-015: Filter exception queue
* FR-017: View unassigned cases
* FR-018: View escalated cases
* RR-001: Open exceptions reporting
* RR-002: Priority reporting
* RR-003: Aged exceptions reporting
* RR-004: SLA breach reporting
* RR-007: Owner workload reporting
* CR-003: High-priority case visibility
* CR-004: SLA breach visibility
* CR-005: Aged case visibility
* CR-006: Unassigned case visibility
* EXP-001: Export queue data to CSV

## 14. MVP scope

The Minimum Viable Product (MVP) version of the queue should include:

* KPI summary;
* case table;
* standard operational filters;
* default risk-based sorting;
* case detail navigation;
* CSV export;
* clear SLA, aging, escalation, and ownership indicators.

The following capabilities may be considered future enhancements:

* saved personal views;
* bulk assignment;
* configurable column layouts;
* real-time notifications;
* automated case creation;
* advanced workload balancing;
* mobile layout;
* direct external bank or PSP communication.

## 15. Summary

The Payment Exception Queue wireframe translates operational requirements into a structured view for analysts and team leads.

It prioritizes visibility of urgent, aged, SLA-breached, escalated, and unassigned cases while supporting filtering, workload management, investigation, reporting, and control review.