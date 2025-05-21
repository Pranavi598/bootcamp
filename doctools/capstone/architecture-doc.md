# 🏛 Architecture Document – Real-Time File Processing System

## 📘 Overview

This document provides a high-level map of the real-time file processing system. It outlines the major components, how data flows through them, and key architectural constraints.

## 🧩 Major Components

### 1. **File Watcher**
- Monitors an input folder continuously.
- Detects new files and emits file paths for processing.

### 2. **Stream Processor Engine**
- Reads files line-by-line using an iterator pattern.
- Passes lines through a configurable series of processors (e.g., clean, transform).
- Handles fan-in and fan-out routing if configured.

### 3. **Stateful Processors**
- Custom processors can retain state across lines.
- Useful for counting, aggregation, or pattern tracking.

### 4. **Output Writer**
- Writes transformed data to an output file or directory.

### 5. **Metrics + Dashboard (FastAPI)**
- Collects logs, processor state, and error traces.
- Exposes live metrics via a FastAPI web interface (`/status`).

---

## 🔄 Data Flow

```mermaid
flowchart TD
    A[New File Detected] --> B[Stream Reader]
    B --> C[Processor: Clean]
    C --> D[Processor: Transform]
    D --> E[Output Writer]
    C --> F[Metrics Collector]
    F --> G[FastAPI Dashboard]
