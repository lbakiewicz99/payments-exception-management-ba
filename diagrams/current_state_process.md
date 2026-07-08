# Current State Process Diagram

```mermaid
flowchart TD
    A[Payment exception identified] --> B[Analyst reviews source repot]
    B --> C[Manual lookup in payment system]
    C --> D[Exception added to spreadsheet]
    D --> E[Priority assigned manually]
    E --> F[Owner assigned by email or team lead]
    F --> G[Investigation performed]
    G --> H[Follow-up via email or Teams]
    H --> I[Spreadsheet status updated]
    I --> J{Resolved?}
    J -- No --> K[Manual escalation if noticed]
    K --> G
    J -- Yes --> L[Case closed in spreadsheet]
    L --> M[Manual management report prepated]
```

## This diagram represents the current manual process for payment exception handling.

Key weaknesses:

* exception tracking is spreadsheet-based;
* ownership is assigned manually;
* SLA and aging are not systematically calculated;
* escalation depends on analyst or team lead review;
* reporting is prepared manually.