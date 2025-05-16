
---

### ✅ `capstone/block-diagram.md`

```markdown
# 🧱 Block Diagram – System Overview

```mermaid
graph TD
    A[Input Folder] --> B[File Watcher]
    B --> C[Streaming Engine]
    C --> D[Processor 1: Clean]
    D --> E[Processor 2: Transform]
    E --> F[Output Writer]
    C --> G[Metrics Collector]
    G --> H[FastAPI Dashboard]
