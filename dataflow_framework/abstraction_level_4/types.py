from typing import Iterator, Callable

ProcessorFn = Callable[[Iterator[str]], Iterator[str]]
