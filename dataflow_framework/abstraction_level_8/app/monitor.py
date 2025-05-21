import os
import time
import shutil
from app.processor import process_file
from app.state import set_current_file, clear_current_file, log_processed_file, get_state

WATCH_DIR = "watch_dir"
UNPROCESSED = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS = os.path.join(WATCH_DIR, "underprocess")
PROCESSED = os.path.join(WATCH_DIR, "processed")
POLL_INTERVAL = 2  # seconds


def recover_underprocess():
    """
    Moves files from underprocess/ to unprocessed/ at startup if they were left behind after an unexpected shutdown.
    """
    for filename in os.listdir(UNDERPROCESS):
        src = os.path.join(UNDERPROCESS, filename)
        dst = os.path.join(UNPROCESSED, filename)
        shutil.move(src, dst)


def start_monitoring():
    """
    Continuously monitors the unprocessed/ folder for new files, processes them,
    and moves them to processed/ after completion. If system crashes and restarts,
    files left in underprocess/ will be moved back to unprocessed/.
    """
    recover_underprocess()  # Ensure that files from underprocess/ are moved back to unprocessed/

    while True:
        files = sorted(os.listdir(UNPROCESSED))

        if files:
            filename = files[0]
            src = os.path.join(UNPROCESSED, filename)
            dst = os.path.join(UNDERPROCESS, filename)

            # Move file from unprocessed/ to underprocess/
            shutil.move(src, dst)

            # Set the current file being processed
            set_current_file(filename)

            # Process the file
            process_file(dst)

            # After processing, clear current file, and move to processed/
            clear_current_file()
            shutil.move(dst, os.path.join(PROCESSED, filename))
            log_processed_file(filename)

        # Wait before checking again
        time.sleep(POLL_INTERVAL)
