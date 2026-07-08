# Target State Process

## Summary

The target process introduces a structured payment exception management workflow.

Each payment exception should have a unique case ID, standardized status, priority, owner, SLA, investigation history, escalation flag, and closure reason.

## Target Process steps

| Step | Activity                       | Owner               | Expected outcome                               |
|------|--------------------------------|---------------------|------------------------------------------------|
| 1    | Exception case is created      | Analyst / System    | Unique case ID assigned                        |
| 2    | Exception details are captured | Analyst / System    | Required payment and exception fields recorded |
| 3    | Exception type is selected     | Analyst             | Standard exception taxonomy applied            |
| 4    | Priority is assigned           | System / Analyst    | Priority based on business rules               |
| 5    | SLA deadline is calculated     | System              | SLA due date and aging status available        |
| 6    | Owner is assigned              | Team lead / System  | Case has clear ownership                       |
| 7    | Analyst investigates case      | Analyst             | Investigation notes recorded                   |
| 8    | Case is resolved or escalated  | Analyst / Team lead | Status updated consistently                    |
| 9    | Closure reason is selected     | Analyst             | Closure evidence captured                      |
| 10   | Case is closed                 | Analyst             | Closed case retained for reporting and audit   |
| 11   | Reporting is refreshed         | System              | Operational and management views updated       |

## Target status values

| Status                    | Description                                                                  |
|---------------------------|------------------------------------------------------------------------------|
| New                       | Case has been created but not yet reviewed                                   |
| In Review                 | Analyst is actively investigating the case                                   |
| Pending External Response | Waiting for bank, PSP, client, or other external party                       |
| Escalated                 | Case requires team lead, manager, risk, or compliance attention              |
| Resolved                  | Root cause has been addressed but case is not formally closed                |
| Closed                    | Case is completed with closure reason and required notes                     |

## Target process benefits

* Clear ownership of each exception.
* Consistent status lifecycle.
* Standarized exception categorization.
* SLA and aging visibility.
* Better escalation control.
* Reduced manual reporting.
* Stronger audit trail.
* Improved management oversight.