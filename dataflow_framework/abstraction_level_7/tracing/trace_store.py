from collections import deque
from threading import Lock

class TraceStore:
    def __init__(self, maxlen=1000):
        self.traces = deque(maxlen=maxlen)
        self.lock = Lock()

    def add(self, trace):
        with self.lock:
            self.traces.append(trace)

    def get_all(self):
        with self.lock:
            return list(self.traces)

TRACE_STORE = TraceStore()
