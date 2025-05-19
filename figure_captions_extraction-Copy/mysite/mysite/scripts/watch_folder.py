import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from extractor.tasks import ingest_from_file

WATCH_DIR = "/app/watch_folder"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".txt"):
            print(f"Detected new file: {event.src_path}")
            ingest_from_file(event.src_path)

if __name__ == "__main__":
    os.makedirs(WATCH_DIR, exist_ok=True)
    observer = Observer()
    observer.schedule(Handler(), WATCH_DIR, recursive=False)
    observer.start()
    print(f"Watching folder: {WATCH_DIR}")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
