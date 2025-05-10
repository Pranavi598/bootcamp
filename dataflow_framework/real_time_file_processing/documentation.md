# 📚 Documentation: Real-Time File Processing System

This document explains the architecture, configuration, usage, and internals of the Real-Time File Processing System. It is designed to be used by developers, contributors, and maintainers.

---

## 📌 Overview

The system processes files from an input folder in two modes:

1. **Single File Mode** — Processes a single specified file.
2. **Watch Mode** — Continuously monitors a folder and processes new files as they arrive.

It uses a stream-based architecture with modular processors, real-time monitoring via FastAPI, and supports Dockerized deployments.

---

## 🛠️ Components

### 1. `main.py`

- Entry point for the CLI.
- Parses `--input` or `--watch` mode flags.
- Initializes processor DAG and begins processing.

### 2. `dashboard/server.py`

- Runs a FastAPI web server.
- Hosts endpoints:
  - `/health` – System health status.
  - `/stats` – Current file processing metrics.
  - `/files` – List of processed files.

### 3. `dashboard/state.py`

- Stores application state in memory.
- Tracks:
  - Number of files processed
  - Errors
  - Active processors

### 4. `utils/dag_runner.py`

- Core streaming engine.
- Executes processors as a directed acyclic graph (DAG).
- Supports iterator-based processing and fan-in/fan-out.

### 5. `utils/watch.py`

- Implements file system watcher.
- Uses polling to detect new files in `watch_directory/unprocessed`.

---

## ⚙️ Dual Execution Modes

### 1. Single File Mode

```bash
python main.py --input path/to/file.txt
```

- Processes the file and exits.
- Suitable for batch processing or testing.

### 2. Watch Mode

```bash
python main.py --watch
```

- Watches `watch_directory/unprocessed/`.
- Automatically processes new files.
- Moves them to `processed/` after successful completion.

---

## 🔗 FastAPI Dashboard

Start the API:

```bash
uvicorn dashboard.server:app --reload
```

### Endpoints:

| Endpoint        | Method | Description                       |
|----------------|--------|-----------------------------------|
| `/health`       | GET    | Returns `"healthy"` if live       |
| `/stats`        | GET    | Shows count of files processed    |
| `/files`        | GET    | Lists processed file history      |

---

## 🐳 Docker Instructions

### Build the Docker Image

```bash
docker build -t file-processor .
```

### Run with Docker (Watch Mode)

```bash
docker run -v $(pwd)/watch_directory:/app/watch_directory file-processor --watch
```

> Mounting the volume ensures access to input/output folders.

---

## 🧪 Development Workflow

### 1. Local Testing

```bash
python main.py --input sample.txt
```

### 2. Real-Time Watch Mode

```bash
python main.py --watch
```

### 3. View Dashboard

```bash
uvicorn dashboard.server:app --reload
```

Visit: `http://127.0.0.1:8000/docs` for auto-generated Swagger UI.

---

## 📝 run.sh Script

```bash
./run.sh --input sample.txt   # One-shot mode
./run.sh --watch              # Real-time mode
```

Includes logic to simplify usage and avoid long commands.

---

## 🧰 Makefile Targets

```makefile
make run           # Default runner
make docker-build  # Build container image
make docker-run    # Run container with volume mount
make clean         # Remove __pycache__ and temp files
```

---

## 📤 File Handling

- Drop files into: `watch_directory/unprocessed/`
- After processing, files are moved to: `watch_directory/processed/`
- Processing is atomic and traceable.

---

## 📡 Uptime Monitoring

Use a free monitoring tool like [Better Uptime](https://betteruptime.com/):

1. **Deploy FastAPI app** to a public cloud server (Azure, AWS, etc.)
2. **Expose health endpoint**, e.g.:  
   `http://<your-public-ip>:8000/health`
3. **Add the monitor** in Better Uptime:
   - Name: File Processor Health
   - URL: Your health endpoint
   - Alert if: Down for more than 30 seconds

> Ensure firewall rules allow external access to port 8000.

---

## 📦 Packaging (Optional)

To build and publish this as a Python package:

```bash
python -m build
twine upload dist/*
```

Add metadata in `pyproject.toml` if required.

---

## 🔍 Troubleshooting

- **Port Already in Use?**  
  Kill existing FastAPI server or use another port.

- **Permission Denied in Docker?**  
  Ensure volume mounts have correct file permissions.

- **No Files Being Processed in Watch Mode?**  
  Confirm files are placed in the correct `unprocessed` folder.

---

## ✅ Best Practices

- Use `.venv` files or config classes for port numbers, watch paths, etc.
- Add `logging` for real-time debugging.
- Extend FastAPI with upload support or authentication if needed.
- Keep tests for each processor module.

---

#
