# Sequence Diagram – Login Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant DB

    User->>Frontend: Enter username/password
    Frontend->>Backend: Send login request
    Backend->>DB: Query user credentials
    DB-->>Backend: Return user info
    Backend-->>Frontend: Success/Failure response
    Frontend-->>User: Display login result