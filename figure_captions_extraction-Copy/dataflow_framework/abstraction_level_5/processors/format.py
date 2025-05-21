def process(lines):
    for tag, line in lines:
        yield ("", f"[INFO] {line}")
