# 🛠️ Design Document – Real-Time File Processing System

## 📌 Problem

We need a system to monitor a folder for incoming text files, process them line-by-line in real-time using a streaming dataflow framework, and expose system status and metrics via a web dashboard.

## 🎯 Goals

- Detect and process new files in a specific directory in real-time.
- Use a modular pipeline (streaming processors) to transform content.
- Allow both single-file and watch modes.
- Show metrics and live system state on a FastAPI dashboard.

## 🚫 Non-Goals

- No support for distributed or multi-machine processing.
- Not focusing on binary file handling or advanced ML transformations.
- No user interface beyond a basic FastAPI JSON endpoint.

## 🧠 Design Options

### Option 1: Python + Watchdog + FastAPI (Chosen)
- Use Python’s `watchdog` library to monitor the folder.
- Implement stream-based processors using iterators.
- Build a FastAPI server to show metrics, logs, and system health.

### Option 2: Bash + Cron + Logging
- Periodic checks using cron jobs or shell scripts.
- Simple log aggregation.
- Very limited flexibility or live feedback.

## ✅ Decision

We choose **Option 1** because:
- It supports streaming pipelines and real-time feedback.
- FastAPI gives us rich monitoring endpoints.
- It is modular and extensible for future enhancements.

## ⚠️ Risks

- Watchdog may miss events under high file throughput.
- Long-running processors may block the pipeline unless async/split.
- FastAPI endpoints may become a bottleneck if not optimized.

## 🧪 Future Enhancements (Optional)

- Add S3/GCS upload support.
- Dockerize and deploy to cloud.
- Add retries or error-handling modules for corrupt files.
