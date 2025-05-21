def process(lines):
    with open("errors.log", "a") as f:
        for tag, line in lines:
            f.write(line + "\n")
            yield ("", line)
