# 🧠 Bootcamp Journey

Welcome to my bootcamp journey! This repository documents my step-by-step progress as I explored system design, data processing, Python tooling, real-time processing, and web development — all while building production-grade tools and infrastructure.

---

## 📁 Project Structure

```
bootcamp/
├── DAY 0/
├── basics/
├── dataflow_framework/
├── doctools/
├── figure_captions_extraction/
├── figure_captions_extraction-Copy/
├── language_drills/
├── persistence_drills/
```

---

## 🟢 DAY 0 – Cloud Setup and Docker Demo

> **Goal**: Get comfortable with cloud environments, basic web deployment, and Docker containers.

### ✅ What I Did:
- Created an Azure VM using Ubuntu.
- Deployed a simple static web page showing my name and photo using Python's built-in HTTP server.
- Installed Docker on the VM.
- Pulled a Python image and ran a "Hello, World!" container.
- Recorded CLI demos using Asciinema.

### 🌐 Skills:
- Linux command line
- Azure VM setup
- HTTP server basics
- Docker fundamentals

---

## 🟡 basics/ – Python Essentials

> **Goal**: Learn professional packaging and publishing of Python tools with CLI interfaces.

### ✅ What I Did:
- Created a Python module `helloworld` using `uv` and `pyproject.toml`.
- Added rich CLI interface using `typer` and `rich`.
- Created a separate consumer CLI `many-hellos` that reused the module.
- Published to TestPyPI.
- Used YAML for external configuration.
- Integrated Python `logging`.

### 📦 Tools:
- `uv` for packaging and envs
- `typer`, `rich`
- `loguru`, `pyyaml`
- TestPyPI


---

## 🔴 doctools/ – Python Packaging & CLI Tools

> Goal: *Developer Documentation & Visual Communication*

This folder focuses on writing and publishing clear technical documentation.

**Key Learning Areas:**

- Markdown basics and README authoring
- Daily log of what I learned and what confused me
- Visual documentation:
  - Mermaid.js (sequence diagrams)
  - Draw.io (architecture block diagrams)
  - XMind (mind maps for planning)
- Using MkDocs + Material Theme for beautiful documentation sites
- Google Docs for collaborative proposals
- Linking references and system design documentation
- Final Capstone: end-to-end project docs with diagrams and publishing

---

## 🟠 language_drills/

> **Goal**: Practice essential Python language features.

### ✅ Focus Areas:
- Control flow (loops, conditionals)
- Comprehensions
- Functional programming (`map`, `filter`, `lambda`)
- String formatting
- File I/O
- Organized Python scripts with `main()` and meaningful function names.
- Wrote examples for profiling, decorators, logging, exceptions, and debugging.
- Used `argparse` for basic CLI usage.

### 🧠 Skills:
- Clean Python scripting
- Code modularization
- Debugging and logging techniques
---

## 🔵 dataflow_framework/ – Real-time File Processing System

> **Goal**: Build a full streaming pipeline framework from scratch with file watching, processors, and web monitoring.

### ✅ Key Features:
- Streaming processor pattern using `Iterator[str] -> Iterator[str]`.
- Fan-in and fan-out processors for line-based data transformation.
- Stateful and configurable processors.
- FastAPI-based monitoring dashboard with live stats and errors.
- Dual execution modes: single file and directory watch mode.
- Dockerized and production-ready.

### 🧩 Technologies:
- Python
- FastAPI
- Docker
- Asynchronous file watching
- Modular CLI
- Makefile / `run.sh` automation

---
## ⚪ persistence_drills/

> **Goal**: Learn data persistence strategies.

### ✅ Covered:
- Working with JSON and CSV
- File reading/writing
- SQLite basics with `sqlite3`
- Object serialization (`pickle`)

---

## 🟣 figure_captions_extraction/ – Final Project: Scientific Figure Metadata Extractor

> **Goal**: Extract and serve figure captions and metadata from scientific articles.

### ✅ Main Features:
- Pulls full-text papers from PMC (PubMed Central) API.
- Extracts figure URLs, captions, title, abstract.
- Fetches biomedical entities using PubTator API.
- Stores results in SQLite database.
- Exposes data using a FastAPI REST API.
- Organized Django project with `extractor` app:
  - `api/`: REST API logic
  - `templates/`: Optional HTML rendering
  - `ingestion/`: PMC + PubTator fetchers
  - `tasks.py`: Ingestion coordination
  - `management/commands/ingest.py`: Custom CLI
  - `models.py`: ORM
  - `views.py`: Web views

### 🧠 Concepts Used:
- API consumption
- SQLite storage
- Async ingestion
- Django management commands
- REST API serving
- Modular Django structure

---



## ✅ Highlights

- 🚀 Deployed multiple tools and services on the cloud.
- 🔄 Built a custom dataflow pipeline with real-time streaming.
- 📦 Published Python modules with TestPyPI.
- 📊 Built a scientific metadata extractor powered by PMC + PubTator APIs.
- 🧠 Mastered packaging, CLI design, error handling, and monitoring.

---
