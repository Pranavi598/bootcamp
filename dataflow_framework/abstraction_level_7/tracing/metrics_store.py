from collections import defaultdict
from threading import Lock

class MetricsStore:
    def __init__(self):
        self.lock = Lock()
        self.data = defaultdict(lambda: {"count": 0, "time": 0.0, "errors": 0})

    def record(self, processor, success=True, duration=0.0):
        with self.lock:
            self.data[processor]["count"] += 1
            self.data[processor]["time"] += duration
            if not success:
                self.data[processor]["errors"] += 1

    def get_stats(self):
        with self.lock:
            return dict(self.data)

METRICS = MetricsStore()
