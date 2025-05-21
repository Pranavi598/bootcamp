# Level 8 - Folder Monitor and Recovery System

This system continuously monitors a folder for incoming files and processes them using a streaming engine. Key features include:

- **File Recovery on Restart**: Automatically recovers files in case of crashes and restarts.
- **Live Monitoring**: View real-time processing status via a FastAPI-powered dashboard.
- **Safe File Movement**: Files are safely moved through three stages:
  - `unprocessed/` → files waiting for processing
  - `underprocess/` → files being processed
  - `processed/` → successfully processed files

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Pranavi598/folder-monitor.git
    cd folder-monitor
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create Directories**:
    ```bash
    mkdir -p watch_dir/unprocessed watch_dir/underprocess watch_dir/processed
    ```

4. **Run the Application**:
    Start both the monitoring system and the live dashboard:
    ```bash
    python main.py
    ```

5. **Access the Dashboard**:
    Open `http://127.0.0.1:8000` in your browser to view the live status.

## Testing the System

Run unit tests for monitoring functionality:
```bash
pytest tests/test_monitor.py
