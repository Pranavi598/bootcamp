def process(lines):
    for tag, line in lines:
        if tag == 'error':
            print(f"Splitter: Routing to 'errors' -> {line}")
            yield ('errors', line)
        elif tag == 'warn':
            print(f"Splitter: Routing to 'warnings' -> {line}")
            yield ('warnings', line)
        else:
            print(f"Splitter: Routing to 'general' -> {line}")
            yield ('general', line)
