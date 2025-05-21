class LineCounter:
    def __init__(self, **options):
        self.count = 0

    def process(self, lines):
        self.count += len(lines)
        print(f"Processed {self.count} lines.")
        return lines  # Return the lines unchanged (or modify if needed)
