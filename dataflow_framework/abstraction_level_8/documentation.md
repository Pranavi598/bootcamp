# Folder Monitor and Recovery System - Documentation

## Overview

The Folder Monitor and Recovery System automatically monitors a specified folder for incoming files, processes them through a streaming engine, and ensures reliability through automatic file recovery. The system is fault-tolerant, self-running, and resilient to crashes and restarts.

### Key Features:
- **Continuous Monitoring**: Watches the `unprocessed/` directory for new files.
- **File Movement**: Files move safely through three stages: 
  - `unprocessed/` → `underprocess/` → `processed/`
- **Fault Recovery**: Files in `underprocess/` are moved back to `unprocessed/` on system restart.
- **Live Status**: A FastAPI-powered web dashboard shows real-time file processing status, including the current file, processed files, and folder stats.

## System Components

### `monitor.py`
Handles folder monitoring:
- **`recover_underprocess()`**: Moves files from `underprocess/` to `unprocessed/` on startup.
- **`start_monitoring()`**: Polls the `unprocessed/` directory for new files, moves them to `underprocess/`, processes them, and finally moves them to `processed/`.

### `processor.py`
Handles the processing of files:
- **`process_file()`**: Processes each file by reading it line-by-line and performing the necessary operations.

### `dashboard.py`
Provides a FastAPI-powered web dashboard to show:
- Current file being processed.
- Number of files in each folder.
- Recent processed files and timestamps.

### `state.py`
Tracks and manages the state of the files:
- **`get_state()`**: Returns the current status of the system.
- **`set_current_file()`**: Sets the current file being processed.
- **`clear_current_file()`**: Clears the current file once processing is complete.
- **`log_processed_file()`**: Logs the processed files.

## File Lifecycle
1. **New Files**: Land in `unprocessed/` directory.
2. **Processing**: Moved to `underprocess/` directory while being processed.
3. **Completion**: Once processed, files are moved to `processed/`.
4. **Recovery**: Files in `underprocess/` are moved back to `unprocessed/` after a restart.

## Access the Dashboard:
    Navigate to `http://127.0.0.1:8000` in your browser to view the live status.

## Error Recovery
The system is designed to automatically recover from crashes by:
- Moving files in `underprocess/` back to `unprocessed/` on restart.
- Ensuring the system processes files in a fault-tolerant and idempotent manner.

## Testing
Unit tests for monitoring logic can be run using:
```bash
pytest tests/test_monitor.py
