import time
from tracing.metrics_store import METRICS
from tracing.trace_store import TRACE_STORE
from tracing.error_store import ERROR_LOG

class BaseProcessor:
    def __init__(self, name, enable_trace=False):
        self.name = name
        self.enable_trace = enable_trace

    def process(self, line):
        raise NotImplementedError

    def __call__(self, line, trace):
        start = time.time()
        try:
            result = self.process(line)
            METRICS.record(self.name, success=True, duration=time.time() - start)
            if self.enable_trace:
                TRACE_STORE.add(trace + [self.name])
            return result
        except Exception as e:
            METRICS.record(self.name, success=False)
            ERROR_LOG.log(self.name, str(e))
            return None
