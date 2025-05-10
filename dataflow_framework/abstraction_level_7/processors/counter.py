class Counter:
    def __init__(self, name, enable_trace):
        self.name = name
        self.enable_trace = enable_trace
        self.count = 0

    def process(self, line):
        self.count += 1
        return f"{line} [count={self.count}]"
