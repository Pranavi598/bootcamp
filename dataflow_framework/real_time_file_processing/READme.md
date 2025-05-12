# Real-Time File Processing System

A dynamic, observable, fault-tolerant, and self-managing file processing system built with Python and FastAPI. It supports both single-file and real-time monitoring modes, with a live dashboard and Docker support.

---

## ✅ Features

- **Dual Execution Modes**:
  - `--input <file>`: Process a single file and exit.
  - `--watch`: Monitor a folder and process incoming files in real-time.
- **Live Dashboard** with FastAPI:
  - View processing stats, health status, and file history.
- **Docker Support**: Easily containerize and deploy the application.
- **run.sh / Makefile**: Simplifies running and deploying the system.
- **Monitoring Support**: Integrate with Better Uptime or similar tools.

---

## 🗂 Project Structure

```
real_time_file_processing/
├── main.py                     # CLI entry point for both modes
├── run.sh                      # Shell script to run the app
├── Makefile                    # Automation for build/run tasks
├── Dockerfile                  # Docker setup
├── requirements.txt            # Dependencies
│
├── dashboard/
│   ├── main.py                 # Optional dashboard starter
│   ├── server.py               # FastAPI server with endpoints
│   └── state.py                # In-memory state tracking
│
├── utils/
│   ├── dag_runner.py           # Stream processor framework
│   └── watch.py                # Watch mode utilities
│
└── watch_directory/
    ├── unprocessed/            # Incoming files
    └── processed/              # Processed files archive
```

---

## 🚀 How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Single File Mode

```bash
python main.py --input path/to/file.txt
```

### 3. Watch Mode

```bash
python main.py --watch
```

---

## 🌐 FastAPI Endpoints

Start the server:

```bash
uvicorn dashboard.server:app --reload
```

Available endpoints:

- `GET /health` — Returns system health.
- `GET /stats` — Displays processing statistics.
- `GET /files` — Lists processed files.
  

Default URL: http://127.0.0.1:8000

---

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t file-processor .
```

### Run in Watch Mode

```bash
docker run -v $(pwd)/watch_directory:/app/watch_directory file-processor --watch
```

---

## 🛠 run.sh Usage

```bash
chmod +x run.sh
./run.sh --watch               # Watch mode
./run.sh --input file.txt      # Single file mode
```
---

---

## 📤 Uploading Files

Upload manually or programmatically:

- **Manual**: Place input files into `watch_directory/unprocessed/`.
- **Processed files** are automatically moved to `watch_directory/processed/`.
- **file upload**: Extended FastAPI for file uploads
- http://127.0.0.1:8000/docs
- http://localhost:8000/docs#/default/files_files_get

---

## 📈 Monitoring with Better Uptime

To set up uptime monitoring:


. **Go to [Better Uptime](https://betteruptime.com/)** and:
   - Create a new monitor.
   - Set the URL to: `https://8191-223-178-21-9.ngrok-free.app/health`
   - Configure alerts and ping frequency.

> Note: Monitoring won't work with `localhost`. You must deploy the server publicly.

---

## ✅ Final Checklist

- [x] `run.sh` or `Makefile` supports common tasks
- [x] Dual execution modes implemented (`--input`, `--watch`)
- [x] FastAPI endpoints available for health, stats, files
- [x] Docker-compatible
- [x] All files structured and documented
- [x] README includes clear deployment instructions
- [x] Monitoring enabled via Better Uptime or similar



