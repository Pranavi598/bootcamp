import yaml
import os
from collections import defaultdict
from processors import tagger, counter, error_prone
from processors.base import BaseProcessor

PROCESSOR_MAP = {
    "tagger": tagger.Tagger,
    "counter": counter.Counter,
    "error_prone": error_prone.ErrorProne,
}


def load_dag(config_file):
    config_file_path = os.path.join(os.path.dirname(__file__), '..', config_file)  # Go up one level
    with open(config_file_path) as f:
        dag = yaml.safe_load(f)  # Load the YAML file into a dictionary
    return dag


def run_pipeline(input_path, output_path, config_file, enable_trace=False):
    dag = load_dag(config_file)
    processors = {}

    # Initialize processors
    for name in dag:
        cls = PROCESSOR_MAP.get(name)
        if cls:
            processors[name] = cls(name, enable_trace)

    # Build adjacency list
    outputs = defaultdict(list)
    for src, targets in dag.items():
        for tgt in targets:
            outputs[src].append(tgt)

    # Process input
    with open(input_path) as infile, open(output_path, "w") as outfile:
        print(f"Output will be written to: {output_path}")  # Debugging line to show where the output is being written

        for line in infile:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            trace = ["start"] if enable_trace else []
            queue = [("start", line, trace)]

            while queue:
                node, data, tr = queue.pop(0)
                print(f"Processing node: {node}, data: {data}, trace: {tr}")  # Debug print
                for next_node in dag.get(node, []):
                    processor = processors.get(next_node)
                    if not processor:
                        continue
                    result = processor.process(data)  # Call the correct method
                    print(f"Next node: {next_node}, result: {result}")  # Debug print
                    if dag.get(next_node) == ["end"]:
                        print(f"Writing to file: {result}")  # Debugging line
                        try:
                            outfile.write(result + "\n")  # Write result to the file
                        except Exception as e:
                            print(f"Error writing to file: {e}")  # Error handling

                    if result:
                        if dag.get(next_node) == ["end"]:
                            outfile.write(result + "\n")
                        else:
                            queue.append((next_node, result, tr + [next_node]))  # Add the next node to the queue
