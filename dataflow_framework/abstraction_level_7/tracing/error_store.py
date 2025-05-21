from collections import deque
from threading import Lock

class ErrorLog:
    def __init__(self, maxlen=100):
        self.errors = deque(maxlen=maxlen)
        self.lock = Lock()

    def log(self, processor, message):
        with self.lock:
            self.errors.append({"processor": processor, "message": message})

    def get_all(self):
        with self.lock:
            return list(self.errors)

ERROR_LOG = ErrorLog()
