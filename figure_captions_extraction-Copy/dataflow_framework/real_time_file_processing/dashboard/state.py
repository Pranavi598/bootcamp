# state.py

from typing import List
from threading import Lock

class FileProcessingState:
    def __init__(self):
        self.processed_files: List[str] = []
        self.lock = Lock()

    def update_processed_files(self, file_name: str):
        with self.lock:
            self.processed_files.append(file_name)

    def get_processed_files(self) -> List[str]:
        with self.lock:
            return list(self.processed_files)

    def get_stats(self):
        with self.lock:
            return {
                "total_processed": len(self.processed_files)
            }

# Global state instance
state = FileProcessingState()
