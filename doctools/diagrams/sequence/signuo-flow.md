# 📈 Sequence Diagram – Sign-Up + Email Verification

This diagram models the interaction flow between a user and system components during the sign-up and email verification process.

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database
    participant EmailService

    User->>Frontend: Fill Sign-Up Form
    Frontend->>Backend: Send Sign-Up Data (username, email, password)
    Backend->>Database: Save User as Inactive
    Backend-->>Frontend: Return "Verify Your Email"

    Backend->>EmailService: Send Verification Email (async)
    EmailService-->>User: Email with Verification Link

    User->>Frontend: Clicks Email Verification Link
    Frontend->>Backend: Submit Token
    Backend->>Database: Activate User
    Backend-->>Frontend: Account Verified
```

---

## ✅ Notes

- **Arrows (`->>`)** indicate message flow (solid line = synchronous, dashed = async).
- **Actors** include: User, Frontend, Backend, Database, and EmailService.
- **Verification Link** is typically token-based and time-limited.
