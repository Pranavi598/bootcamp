# processors/tag_warn.py
def process(lines):
    for tag, line in lines:
        if 'warn' in line.lower():
            print(f"Tagging line as warn: {line}")  # Debug print
            yield ('warn', line)
        else:
            print(f"No warn tag for line: {line}")  # Debug print
            yield ('', line)
