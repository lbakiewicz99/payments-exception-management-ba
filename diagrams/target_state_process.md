# Target State Process Diagram

```mermaid
flowchart TD
    A[Exception case created] --> B[Unique case ID assigned]
    B --> C[Exception details captured]
    C --> D[Exception type selected]
    D --> E[Priority assigned]
    E --> F[SLA deadline calculated]
    F --> G[Owner assigned]
    G --> H[Investigation notes added]
    H --> I{Resolved?}
    I -- No --> J{SLA breached or high risk?}
    J -- Yes --> K[Escalate case]
    J -- No --> H
    K --> H
    I -- Yes --> L[Closure reason selected]
    L --> M[Case closed]
    M --> N[Reporting update]
```

## Notes

This diagram represents the proposed target workflow for payment exception handling.

Key improvements:

* each case receives a unique case ID;
* exception details are captured consistently;
* priority and SLA are assigned based on business rules;
* ownership is clear;
* aged and high-risk cases can be escalated;
* closure requires a valid reason;
* reporting is updated from structured case data.

