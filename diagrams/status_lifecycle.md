# Payment Exception Status Lifecycle

```mermaid
stateDiagram-v2
    [*] --> New
    New --> InReview
    InReview --> PendingExternalResponse
    PendingExternalResponse --> InReview
    InReview --> Escalated
    PendingExternalResponse --> Escalated
    Escalated --> InReview
    InReview --> Resolved
    Escalated --> Resolved
    Resolved --> Closed
    Closed --> [*]