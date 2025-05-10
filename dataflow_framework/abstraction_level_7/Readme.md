# Level 7 – Observability and System Introspection

This project is part of a bootcamp on building dataflow frameworks. At Level 7, we add real-time observability to our processing system using FastAPI.

## 📌 Features

- **Metrics Layer**: Live stats for each processor (count, processing time, error count)
- **Tracing System**: Tracks each line's path through the DAG
- **Error Logging**: Collects recent errors from processors
- **Web Dashboard**: View metrics, traces, and errors via REST API

## 🗂️ Directory Structure

```
.
├── dashboard/
│   ├── __init__.py
│   └── server.py
├── processors/
│   ├── __init__.py
│   ├── base.py
│   ├── counter.py
│   ├── error_prone.py
│   └── tagger.py
├── tracing/
│   ├── __init__.py
│   ├── metrics_store.py
│   ├── trace_store.py
│   └── error_store.py
├── utils/
│   ├── __init__.py
│   └── dag_runner.py
├── dag_config.yaml
├── input.txt
├── out.txt
└── main.py
```

## 🚀 Running the Project

1. Install dependencies:

```bash
pip install fastapi uvicorn pyyaml
```

2. Run the pipeline with dashboard:

```bash
python main.py --trace
```

3. Open your browser and visit:

- `http://localhost:8000/stats` → Live processor metrics
- `http://localhost:8000/trace` → Recent traces (last 1000)
- `http://localhost:8000/errors` → Recent error logs

## 📄 Sample Input (`input.txt`)

```text
INFO User logged in
WARN Disk space low
ERROR Failed to save file
INFO File uploaded
```

## ✅ Output (`out.txt`)

The result after flowing through the DAG with processors.

---

## 🧠 Learnings

- Built thread-safe metrics and error stores
- Integrated FastAPI in a separate thread for observability
- Learned how to monitor data systems like a runtime engineer