from typing import Iterator, Tuple

def process(lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
    with open("out.txt", "w") as f:
        for tag, line in lines:
            f.write(f"{line}\n")         # Write to file
            print(f"💾 Output: {line}")  # Optional: still show in terminal
            yield (tag, line)            # Continue yielding if needed
