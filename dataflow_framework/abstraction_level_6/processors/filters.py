from typing import Iterator, Tuple

def only_error(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    for line in lines:
        if "error" in line:
            print(f"[error] {line}")
            yield "end", line

def only_warn(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    for line in lines:
        if "warn" in line:
            print(f"[warn] {line}")
            yield "end", line
