class Tagger:
    def __init__(self, name, enable_trace):
        self.name = name
        self.enable_trace = enable_trace

    def process(self, line):
        if "ERROR" in line:
            return f"[error] {line}"
        elif "WARN" in line:
            return f"[warn] {line}"
        else:
            return f"[info] {line}"
