import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .file_ingestor import ingest_from_file  # assuming you renamed process_file

logger = logging.getLogger(__name__)

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            logger.info(f"New file detected: {event.src_path}")
            try:
                # Optional: wait briefly to ensure file write is complete
                time.sleep(1)
                ingest_from_file(event.src_path)
                logger.info(f"Processed file: {event.src_path}")
            except Exception as e:
                logger.error(f"Failed to process {event.src_path}: {e}")

def watch_folder(path: str):
    observer = Observer()
    observer.schedule(FileHandler(), path, recursive=False)
    observer.start()
    logger.info(f"Watching folder: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("Stopping folder watcher...")
    observer.join()
