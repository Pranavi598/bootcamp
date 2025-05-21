def process(lines):
    count = 0
    for tag, line in lines:
        count += 1
        yield ("", f"[WARN COUNT {count}] {line}")
