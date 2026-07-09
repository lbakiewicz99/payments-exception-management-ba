# User Stories and Acceptance Criteria

## 1. Purpose

This document translates business and functional requirements into user stories with acceptance criteria.

The goal is to make requirements testable and understandable for business users, product owners, developers, QA, and UAT participants.

## 2. User stories

## US-001: Create payment exception case

As a Payments Operations Analyst, I want to create a new payment exception case, so that the exception can be tracked, investigated, and resolved in a controlled workflow.

### Acceptance criteria

```gherkin
Given I am a Payments Operations Analyst
When I create a new payment exception case
Then the case should be assigned a unique case ID
And the case status should be set to New
And the created date should be recorded
```

### Related requirements:

* FR-001
* FR-002
* DR-001
* DR-012

## US-002: Capture payment exception details

As a Payment Operations Analyst, I want to capture key payment and exception details, so that the case contains enought information for investigation and reporting.

### Acceptance criteria

```gherkin
Given I am creating or editing a payment exception case
When I enter payment details
Then I should be able to capture payment reference, payment date, amount, currency, payment channel, exception source, and exception type
And mandatory fields should be clearly identified
```

### Related requirements:

* FR-003
* FR-004
* DR-002
* DR-003
* DR-004
* DR-005
* DR-006
* DR-007
* DR-008

## US-003: Assign case owner

As a Payments Operations Team Lead, I want to assign an owner to a payment exception case, so that each case has clear accountability.

### Acceptance criteria

```gherkin
Given a payment exception case exists
When I assign an owner
Then the selected owner should be saved on the case
And the case should appear in owner's workload view
```

### Related requirements:

* FR-006
* DR-011
* CR-006

## US-004: Update case status

As a Payments Operations Analyst, I want to update the status of a payment exception case, so that the case accurately reflects the current investigation stage.

### Acceptance criteria

```gherkin
Given a payment exception case exists
When I update the case status
Then I should only be able to select a valid status
And the updated status should be visible in the exception queue
```

### Valid statuses:

* New
* In Review
* Pending External Response
* Escalated
* Resolved
* Closed

### Related requirements:

* FR-005
* DR-009

## US-005: Add investigation notes

As a Payments Operations Analyst, I want to add investigation notes to a payment exception case, so that the investigation history is available for review and audit purposes.

### Acceptance criteria

```gherkin
Given a payment exception case exists
When I add an investigation nore
Then the note should be saved against the case
And the note should be visible in the case history
```

### Related requirements:

* FR-011
* DR-017
* CR-002

## US-006: Calculate SLA due date

As a Payments Operations Team Lead, I want the workflow to calculate SLA due dates, so that the team can monitor which cases require urgent action.

### Acceptance criteria

```gherkin
Given a payment exception case has a priority and created date
When the case is created or priority is updated
Then the SLA due date should be calculated based on the priority rules
```

### Related requirements:

* FR-008
* DR-013

## US-007: Flag SLA breaches

As a Payments Operations Team Lead, I want SLA-breached cases to be clearly flagged, so that overdue exceptions can be reviewed and escalated.

### Acceptance criteria

```gherkin
Given a payment exception case has an SLA due date
When the current date is after the SLA due date
And the case is not Closed
Then the case should be flagged as SLA breached
```

### Related requirements:

* FR-009
* DR-014
* CR-004

## US-008: Escalate high-risk or aged case

As a Payments Operations Analyst, I want to escalate a high-risk or aged payment exception, so that the case receives team lead or manager attention.

### Acceptance criteria

```gherkin
Given a payment exception case is open
When I mark the case as Escalated
Then the case status should be updated to Escalated
And the case should appear in the escalated cases view
```

### Related requirements:

* FR-012
* DR-016
* CR-003
* CR-005

## US-009: Close case with closure reason

As a Payments Operations Analyst, I want to close a resolved payment exception with a closure reason, so that the case has sufficient evidence for operational control and reporting.

### Acceptance criteria

```gherkin
Given a payment exception case is marekd as Resolved
When I close the case
Then I must select a closure reason
And I must provide investigation notes
And the closed date should be recorded
```

### Related requirements:

* FR-013
* DR-018
* DR-019
* CR-001
* CR-002

## US-010: Filter exception queue

As a Payments Operations Analyst, I want to filter the exception queue by status, priority, owner, exception type, payment channel, and SLA brach flag, so that I can focus on the most relevant cases.

### Acceptance criteria

```gherkin
Given I am viewing the exception queue
When I apply one or more filters
Then only cases matching the selected filter criteria should be displayed
```

### Related requirements:

* FR-015
* RR-001
* RR-002
* RR-003
* RR-004

## US-011: View unassigned cases

As a Payments Operations Team Lead, I want to view unassigned payment exception cases, so that I can assign ownership and prevent cases from being missed.

### Acceptance criteria

```gherkin
Given payment exception cases exist
When I filter for unassigned cases
Then all cases without an owner should be displayed
```
### Related requirements:

* FR-017
* CR-006

## US-012: View management reporting summary

As a Payments Operations Manager, I want to view management summary of payment exceptions, so that I can monitor operational performance, SLA breaches, and exception trends.

### Acceptance criteria

```gherkin
Given payment exception data exists
When I view the management summary
Then I should see open exceptions, aged exceptions, SLA breaches, high-priority cases, and closed cases
And I should be able to review breakdowns by exception type and payment channel
```

### Related requirements:

* RR-001
* RR-002
* RR-003
* RR-004
* RR-005
* RR-006
* RR-009