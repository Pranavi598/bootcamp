import importlib
from typing import List, Tuple, Iterator, Dict
from collections import defaultdict
from routing.types import TaggedLine

class DAGRunner:
    def __init__(self, config):
        self.config = config
        self.processors = self.load_processors(config["processors"])
        self.dag = config["dag"]
        self.routes = self.dag["routes"]

    def load_processors(self, processor_configs):
        processors = {}
        for name, proc in processor_configs.items():
            module = importlib.import_module(proc["module"])
            func = getattr(module, proc["function"])
            processors[name] = func
        return processors

    def run(self, lines: List[str]):
        initial_tagged_lines = [("", line) for line in lines]
        print(f"🚀 Starting DAG execution with lines: {initial_tagged_lines}")
        self._execute(self.dag["start"], initial_tagged_lines)

    def _execute(self, node, input_lines):
        processor = self.processors[node]
        output_lines = processor(input_lines)

        route_config = self.routes.get(node, [])
        if isinstance(route_config, list):
            # Single route
            for next_node in route_config:
                self._execute(next_node, output_lines)
        elif isinstance(route_config, dict):
            # Conditional routes based on tags
            tagged_outputs = defaultdict(list)
            for tag, line in output_lines:
                tagged_outputs[tag].append((tag, line))
            for tag, next_nodes in route_config.items():
                for next_node in next_nodes:
                    self._execute(next_node, tagged_outputs.get(tag, []))
