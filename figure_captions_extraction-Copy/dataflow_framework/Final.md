# FINAL.md

## 1. Design Decisions

The most critical architectural decision was to structure the folder as a state machine with three distinct stages: `unprocessed/`, `underprocess/`, and `processed/`. This abstraction made file movement and recovery clear and reliable. Another key decision was to encapsulate all file state and metadata updates in a separate `state.py` module, which helped isolate the UI from core logic. Leveraging FastAPI for the live dashboard was also an effective choice—it allowed us to visualize real-time progress without adding heavy infrastructure.

The abstraction that helped most was treating each file as an independent processing unit. This ensured idempotency and fault-tolerance, as each file could be retried safely without corrupting results or requiring cleanup.

---

##  2. Tradeoffs

To keep the system simple and focused, we chose to process files sequentially, rather than in parallel. We also assumed that all files are fully written before appearing in the `unprocessed/` folder—meaning we did not implement checks for partially written files. 

Another simplification was using local state (e.g., in-memory and logs) instead of persistent storage (like a database) to track processed files. This means state would be lost if logs are deleted or corrupted.

Current limitations include:
- No support for parallel or distributed processing.
- No validation for file integrity or format.
- Dashboard only supports polling, not push-based updates (e.g., via WebSockets).

---

##  3. Scalability

To scale this system for 100x larger input:
- The first change would be to introduce concurrent processing using threads or async tasks, ensuring each file is handled in isolation.
- We’d also decouple file ingestion from processing using a job queue like Celery or RabbitMQ.
- File state and logs would need to be stored in a durable backend (e.g., PostgreSQL or Redis) for resilience and better analytics.
- For very large files, streaming processing would need to be optimized with memory limits and batching.

Yes, parallelization is feasible because each file is processed independently. We'd need to ensure thread-safe state tracking and avoid race conditions during file movement.

---

## 4. Extensibility & Security

To run this in production:
- We'd require authentication and authorization for dashboard access (e.g., using OAuth or JWT).
- File uploads would need validation for file type, size, and format.
- The system should scan for malicious files (e.g., using ClamAV or similar).
- Logging and error handling would need to be robust, with alerts and retry policies.

For protecting output data:
- Store results in a secure, access-controlled location.
- Encrypt sensitive content at rest and in transit.
- Use signed URLs or tokens to access processed results securely.

Extending this system to support more formats, real-time alerts, and configurable workflows would make it viable for production-scale ingestion pipelines.

---
