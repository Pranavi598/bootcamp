# System Diagram

```mermaid
flowchart LR
  A[User] --> B[Web Server]
  B --> C[Docker Container]
  C --> D[Python App]
