# processors/tag_error.py
def process(lines):
    for tag, line in lines:
        if 'error' in line.lower():
            print(f"Tagging line as error: {line}")  # Debug print
            yield ('error', line)
        else:
            print(f"No error tag for line: {line}")  # Debug print
            yield ('', line)
