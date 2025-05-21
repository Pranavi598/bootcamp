def process(lines):
    for tag, line in lines:
        yield (tag, line.strip())
