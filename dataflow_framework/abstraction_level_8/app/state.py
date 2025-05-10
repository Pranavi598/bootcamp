import os
import time

# File directories
WATCH_DIR = "watch_dir"
UNPROCESSED = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS = os.path.join(WATCH_DIR, "underprocess")
PROCESSED = os.path.join(WATCH_DIR, "processed")

current_file = None
processed_log = []

def set_current_file(filename):
    global current_file
    current_file = filename

def clear_current_file():
    global current_file
    current_file = None

def log_processed_file(filename):
    processed_log.append((filename, time.strftime("%Y-%m-%d %H:%M:%S")))

def get_state():
    return {
        "unprocessed": len(os.listdir(UNPROCESSED)),
        "underprocess": len(os.listdir(UNDERPROCESS)),
        "processed": len(os.listdir(PROCESSED)),
        "current_file": current_file,
        "recent": processed_log[-5:],
    }
