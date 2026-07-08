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