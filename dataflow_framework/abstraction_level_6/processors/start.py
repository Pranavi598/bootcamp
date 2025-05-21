from typing import Iterator, Tuple

def tag_lines(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    for line in lines:
        if "error" in line:
            yield "error", line
        elif "warn" in line:
            yield "warn", line
        else:
            yield "general", line
