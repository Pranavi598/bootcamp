def process(lines):
    for tag, line in lines:
        print(f"✅ Output: {line}")
        yield (tag, line)
