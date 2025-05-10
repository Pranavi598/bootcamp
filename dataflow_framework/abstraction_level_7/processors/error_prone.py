class ErrorProne:
    def __init__(self, name, enable_trace):
        self.name = name
        self.enable_trace = enable_trace

    def process(self, line):
        if self.enable_trace:
            return f"{line} [trace={self.name}]"
        return line