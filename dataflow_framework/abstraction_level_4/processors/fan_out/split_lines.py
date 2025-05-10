def split_lines(lines, delimiter=" "):
    """Splits each line in the stream into multiple lines based on a delimiter."""
    for line in lines:
        for part in line.split(delimiter):
            yield part + "\n"
