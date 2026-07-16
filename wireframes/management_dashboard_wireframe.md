# Payment Exception Management Dashboard Wireframe

## 1. Purpose

This document presents a conceptual wireframe for the payment exception management dashboard.

The dashboard provides Payments Operations Tem Leads, Managers, and Risk/Operational Control stakeholders with a summarized view of exception volumes, SLA performance, aging, escalation, workload, and recurring exception drivers.

The wireframe is not a production user interface design. It illustrates how reporting requirements, business rules, controls, and management information could be represented in a business-facing dashboard.

## 2. Primary users

* Payments Operations Team Lead
* Payments Operations Manager
* Risk/Operational Control reviewer
* Finance Operations stakeholder
* Product/Technologu stakeholder
* Data/Reporting stakeholder

## 3. Main user objectives

The dashboard should allow users to:

* monitor current open payment exceptions;
* identify SLA breaches and aged cases;
* monitor High and Critical priority cases;
* review escalated and unassigned cases;
* understand exception trends;
* identify recurring exception types and payment channels;
* review workload distribution;
* review closure reasons and root causes;
* drill down from summary metrics to individual cases;
* export reporting data.

## 4. Conceptual layout

```text
+------------------------------------------------------------------------+
| PAYMENT EXCEPTION MANAGEMENT DASHBOARD                                 |
+------------------------------------------------------------------------+
| Reporting Period: [01 Jan 2025] to [31 Jan 2025]   [Refresh] [Export]  |
+------------------------------------------------------------------------+
| Open Cases | SLA Breaches | Aged Cases | High/Critical | Escalated     |
|    128     |      14      |     22     |       11      |      8        |
+------------------------------------------------------------------------+
| New This Period: 46 | Closed: 39 | Unassigned: 6 | Avg. Age: 4.8 days  |
+------------------------------------------------------------------------+
| EXCEPTION STATUS MIX                                                   |
| New                       18  ##################                       |
| In Review                 57  ######################################## |
| Pending External Response 31  ############################             |
| Escalated                  8  ########                                 |
| Resolved                  14  ##############                           |
+------------------------------------------------------------------------+
| EXCEPTION TREND                                                        |
| Jan W1       24 exceptions                                             |
| Jan W2       31 exceptions                                             |
| Jan W3       28 exceptions                                             |
| Jan W4       35 exceptions                                             |
+------------------------------------------------------------------------+
| TOP EXCEPTION TYPES          | EXCEPTIONS BY CHANNEL                   |
| Bank Rejection           34  | Bank Transfer                       49  |
| PSP Rejection            29  | Card                                38  |
| Returned Payment         21  | Wallet                              22  |
| Delayed Settlement       18  | PSP                                 13  |
| Duplicate Payment Risk    9  | Internal Transfer                    6  |
+------------------------------------------------------------------------+
| AGING AND SLA                                                          |
| 0-2 days: 54 | 3-5 days: 52 | 6-10 days: 15 | Over 10 days: 7          |
| SLA Within Target: 114 | SLA Breached: 14                              |
+------------------------------------------------------------------------+
| OWNER WORKLOAD                                                         |
| Analyst A: 24 | Analyst B: 21 | Analyst C: 19 | Unassigned: 6          |
+------------------------------------------------------------------------+
| PRIORITY CASES REQUIRING ATTENTION                                     |
| CASE-000145 | Critical | SLA Breached | 8 days | Analyst A             |
| CASE-000149 | High     | Due Today    | 3 days | Analyst B             |
| CASE-000163 | High     | Escalated    | 7 days | Unassigned            |
|                                              [View All Priority Cases] |
+------------------------------------------------------------------------+
```

## 5. Dashboard filters

The dashboard should support the following filters:

| Filter           | Type         | Example values                                          |
|------------------|--------------|---------------------------------------------------------|
| Reporting Period | Date range   | From/To                                                 |
| Status           | Multi-select | New, In Review, Escalated, Resolved, Closed             |
| Priority         | Multi-select | Low, Medium, High, Critical                             |
| Exception Type   | Multi-select | Bank Rejection, PSP Rejection, Returned Payment         |
| Payment Channel  | Multi-select | Bank transfer, Card, Wallet, PSP                        |
| Exception Source | Multi-select | Bank File, PSP Report, Reconciliation                   |
| Owner            | Multi-select | Analyst or team queue                                   |
| Team Queue       | Multi-select | Bank Transfers, Card Payments, Digitwal Wallets         |
| SLA Breach       | Boolean      | Yes, No                                                 |
| Aging Bucket     | Multi-select | 0-2 days, 3-5 days, 6-10 days, 11-30 days, Over 30 days |    
| Escalation Flag  | Boolean      | Yes, No                                                 |
| Customer Impact  | Boolean      | Yes, No                                                 |
| High Value       | Boolean      | Yes, No                                                 |
| Duplicate Risk   | Boolean      | Yes, No                                                 |

Filters should apply consistently to KPI cards, charts, breakdowns, and drill-down tables where appropriate.

## 6. Primary KPI cards

| KPI                 | Definition                                                          | Related requirement |
|---------------------|---------------------------------------------------------------------|---------------------|
| Open Cases          | Count of cases where status is not ```Closed```                     | RR-001              |
| SLA Breaches        | Count of open cases where SLA breach flag = Yes                     | RR-004              |
| Aged Cases          | Count of open cases older than 5 business days                      | RR-003              |
| High/Critical Cases | Count of open High and Critical priority cases                      | CR-003              |
| Escalated Cases     | Count of cases with status ```Escalated``` or escalation flag = Yes | FR-018              |
| Unassigned Cases    | Count of open cases without owner or team queue                     | FR-017, CR-006      |
| New Cases           | Count of cases created in selected reporting period                 | RR-009              |
| Closed Cases        | Count of cases closed in selected reporting period                  | RR-009              |

## 7. Supporting indicators

| Indicator               | Definition                                                                 |
|-------------------------|----------------------------------------------------------------------------|
| Average Days Open       | Average business days open for active cases                                |
| Average Resolution Time | Average business days between case creation and closure                    |
| SLA Compliance Rate     | Percentage of closed cases resolved within SLA                             |
| Escalation Rate         | Percentage of cases escalated during selected period                       |
| Reopen Rate             | Percentage of closed cases reopened, if reopen functionality is introduced |
| Customer Impact Rate    | Percentage of cases marked as customer impacting                           |
| High-Value Case Count   | Number of cases meeting the defined high-value threshold                   |
| Duplicate Risk Count    | Number of cases flagged for potential duplicate payment risk               | 

## 8. Status mix

The status mix should show the number of cases by lifecycle status.

Required statuses:

* New;
* In Review;/
* Pending External Response;
* Escalated;
* Resolved;
* Closed.

Recommended visualization:

* horizontal bar chart; or
* stacked bar chart by reporting period.

The chart should support drill-down to the underlying exception queue.

## 9. Exception trend

The exception trend should show case volumes over time.

Recommended views:

| Trend view                | Purpose                                           |
|---------------------------|---------------------------------------------------|
| New cases by week         | Shows incoming operational workload               |
| Closed cases by week      | Shows resolution capacity                         |
| Open case balance         | Shows whether backlog is increasing or decreasing |
| SLA breaches over time    | Shows changes in SLA performance                  |
| Aged cases over time      | Shows changes in long-running exceptions          |
| Escalated cases over time | Shows changes in operational risk                 |

User should be able to select:

* daily;
* weekly;
* monthly reporting intervals.

## 10. Exception type breakdown

The dashboard should show exception volumes grouped by controlled exception type.

Example exception type:

* Bank Rejection;
* PSP Rejection;
* Returned Payment;
* Failed Payment;
* Delayed Settlement;
* Duplicate Payment Risk;
* Unmatched Payment;
* Incorrect Amount;
* Incorrect Currency;
* Missing Reference;
* Customer Query;
* Manual Review Required;

The visualization should support drill-down volumes by payment channel

## 11. Payment channel breakdown

The dashboard should show exception volumes by payment chnnael.

Example channels:

* Bank Transfer;
* Card;
* Wallet;
* PSP;
* Internal Transfer;
* Other.

This view should support comparison of:

* total exceptions;
* SLA breaches;
* aged cases;
* High/Critical cases;
* average resolution time.

## 12. Aging and SLA section

### Aging distribution

| Aging bucket | Definition                          |
|--------------|-------------------------------------|
| 0-2 days     | Open for 0 to 2 business days       | 
| 3-5 days     | Open for 3 to 5 business days       |
| 6-10 days    | Open for 6 to 10 business days      |
| 11-30 days   | Open for 11 to 30 business days     | 
| Over 30 days | Open for more than 30 business days |

### SLA indicators

The dashboard should show:

* cases within SLA;
* cases due today;
* cases due next business day;
* SLA-breached cases;
* SLA compliance rate;
* SLA breaches by priority;
* SLA breches by owner;
* SLA breaches by exception type.

High and Critical SLA breaches should be visually emphasized and available for immediate drill-down.

## 13. Owner workload

The workload section should support team lead review of case distribution.

Required metrics by owner or team queue.

| Metric                   | Description                       |
|--------------------------|-----------------------------------|
| Open Cases               | Total active workload             |
| High/Critical Cases      | Priority workload                 |
| SLA Breaches             | Overdue workload                  |
| Aged Cases               | Long-running workload             |
| Escalated Cases          | Cases requiring additional review |
| Cases Closed This Period | Resolution volume                 |
| Average Case Age         | Average days open                 |

The dashboard should identify:

* analysts with unusualy high workload;
* analysts with multiple SLA breaches;
* unassigned cases;
* queues with growing backlog.

Workload metrics should support management decisions but should not be used without operational context. A higher case count may reflect simpler cases, different working hours, or specliast responsibilites.

## 14. Priority cases requiring attention

The dashboard should include a drill-down table for cases requiring immediate review.

A case should appear if one or more of the following applies:

* priority is ```Critical```
* priority is ```High``` and SLA is breached;
* case is aged and priority is High or Critical;
* escalation flag = Yes;
* high-value flag = Yes;
* duplicate risk flag = Yes;
* customer impact flag = Yes;
* case is unassigned and SLA due date is approaching.

Required fields:

| Field             | Description                |
|-------------------|----------------------------|
| Case ID           | Unique case identifier     |
| Exception Type    | Current classification     |
| Priority          | High or Critical           |
| Status            | Current lifecycle status   | 
| Owner             | Assigned owner or queue    |
| Days Open         | Current case age           |
| SLA Status        | Due, due soon, or breached |
| Escalation Reason | Reason for escalation      |
| Amount/Currency   | Payment value              |
| Customer Impact   | Customer impact flag       |

## 15. Closure and root cause analysis

The dashboard should support review of closed cases.

Required breakdowns:

* closed cases by period;
* closure reason;
* root cause;
* exception type;
* payment channel;
* average resolution time;
* cases closed within SLA;
* cases closed after SLA breach.

Example closure reasons:

* Payment settled;
* Payment reprocessed;
* Payment cancelled;
* Duplicate resolved;
* Bank rejection resolved;
* PSP issue resolved;
* Customer query resolved;
* No action required;
* Incorrect exception.

Root cause analysis should help identify recurring operational or system issues rather than merely count how efficiently analysts cleaned up the consequences.

## 16. Control indicators

The dashboard should include or link to the following key control indicators:

| Indicator                                | Expected resul         |
|------------------------------------------|------------------------|
| Open cases without owner or queue        | Zero or reviewed daily |
| Open cases without priority              | Zero                   |
| Open cases without SLA due date          | Zero                   |
| High/Critical SLA breaches not escalated | Zero                   |
| Aged High/Critical cases not escalated   | Zero                   |
| Closed cases without investigation ntoes | Zero                   |
| Closed cases without closure reason      | Zero                   |
| Cases with invalid status                | Zero                   |
| Cases with invalid exception type        | Zero                   |
| High-value cases not flagged or review   | Zero                   |
| Duplicate-risk cases not escalated       | Zero                   | 

Control failures should provide drill-down to the affected cases.

## 17. Drill-down behavior

Users should be able to select a KPI, chart segment, or table row and navigate to:

* filtered exception queue;
* SLA breach report;
* aged exceptions report;
* escalation report;
* owner workload report;
* individual exception detail view;
* control evidence report.

Example:

```text
Select SLA Breaches KPI
→ Open exception queue
→ Apply SLA Breach = Yes
→ Sort by Priority and SLA Due Date
```

## 18. Export requirements

The dashboard should support export of:

* filtered exception data;
* KPI summary;
* SLA brech report;
* aged exception report;
* escalation report;
* owner workload report;
* management summary data;
* control evidence data.

Recommended export format:

* CSV for detailed records;
* PDF or presentation-ready format as a future enhancement for management summaries.

## 19. Data refresh and reporting period

| Reporting element       | Refresh expectation                      |
|-------------------------|------------------------------------------|
| Exception queue metrics | Latest available case data               |
| SLA breach indicators   | Recalculated at least daily              |
| Aging indicators        | Recalculated at least daily              |
| Management summary      | Available for weekly review              |
| Closure metric          | Based on selected reporting period       |
| Trend charts            | Based on case creation and closure dates |
| Control indicators      | Daily or according to control frequency  |

The dashboard should display:

* last refresh date and time;
* selected reporting period;
* active filters;
* data availability warning.

## 20. Empty and error states

| Scenario                            | Expected behavior                                                       |
|-------------------------------------|-------------------------------------------------------------------------|
| No cases exist for selected period  | Display zero-value KPI cards and clear message                          |
| No cases match selected filters     | Display ```No cases match the selected filters.```                      |
| Reporting data is unavailable       | Display data availability warning                                       |
| One metric cannot be calculated     | Display unavailable indicator without breaking other dashboard sections |
| Export fails                        | Display error while retaining selected filters                          | 
| Data refresh is delayed             | Display last successful refresh timestamp                               |
| User lacks access to detailed cases | Show aggregate data only and display access message                     |

 ## 21. Accessibility and usability considerations

 The dsahboard should:

 * avoid using color as the only risk indicator;
 * include labels for SLA breach, priority, escalation, and aging;
 * use consistent metric and field names;
 * support clear keyboard navigation where implemented;
 * provide readable chart labels;
 * avoid excessive visual elemtns;
 * keep the most important risk information above the fold;
 * provide definitions or tooltips for complex metrics.

 ## 22. Related requirements
 
 The dashboard supports:

 * RR-001: Open exceptions reporting
 * RR-002: Priority reporting
 * RR-003: Aged exceptions reporting
 * RR-004: SLA breach reporting
 * RR-005: Exception type breakdown
 * RR-006: Payment channel breakdown
 * RR-007: Owner workload reporting
 * RR-008: Closure reason reporting
 * RR-009: Weekly management summary
 * FR-017: Unassigned case visibility
 * FR-018: Escalated case visibility
 * CR-003: High-priority case visibility
 * CR-004: SLA breach visibility
 * CR-005: Aged case visibility
 * CR-006: Unassigned case visibility
 * EXP-003: Management summary export
 * EXP-004: Control evidence export

 ## 23. Minimum Viable Product scope

 The Minimum Viable Product version should include:

 * primary KPI cards;
 * reporting period filter;
 * status and priority breakdowns;
 * exception type breakdown;
 * payment channel breakdown;
 * aging and SLA reporting;
 * owner workload summary;
 * priority case drill-down;
 * CSV export;
 * last refresh timestamp.

 Future enhancements may include:

 * configurable dashboard layout;
 * scheduled management reports;
 * email or Teams notifications;
 * predictive SLA breach indicators;
 * automated root cause suggestions;
 * cross-team benchmarking;
 * direct links to bank or PSP investigation tools;
 * mobile dashboard layout;
 * configurable control thresholds.

 ## 24. Summary

 The Payment Exception Management Dashboard wireframe translates reporting and control requirements into a structured management view.

 It supports workload oversight, SLA monitoring, aging review, escalation control, trend analysis, root cause identification, management reporting, and drill-down to individual payment exception cases.