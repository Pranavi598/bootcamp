import importlib
from typing import Iterator, Tuple, Dict, Callable

class StateRouter:
    def __init__(self, config: dict):
        self.tag_to_processor: Dict[str, Callable] = {}
        for node in config["nodes"]:
            tag = node["tag"]
            module_name, func_name = node["type"].rsplit(".", 1)
            module = importlib.import_module(module_name)
            func = getattr(module, func_name)
            self.tag_to_processor[tag] = func

    def run(self, lines: Iterator[str]):
        queue = [("start", line) for line in lines]

        while queue:
            tag, line = queue.pop(0)
            if tag == "end":
                print(f"✅ Exiting: {line}")
                continue

            processor = self.tag_to_processor.get(tag)
            if processor is None:
                print(f"⚠️ No processor for tag: {tag}")
                continue

            for new_tag, new_line in processor(iter([line])):
                queue.append((new_tag, new_line))
