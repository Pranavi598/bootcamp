def join_two_lines(lines):
    """Joins two lines into one, separated by a space."""
    joined = " ".join(lines)  # Join with space or another delimiter
    print(f"Joined lines: {joined}")  # Debug output
    yield joined