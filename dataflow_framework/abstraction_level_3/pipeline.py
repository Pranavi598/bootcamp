# pipeline.py

import importlib
import yaml
from typing import List  # <-- Add this import
from abstraction_level_3.types import ProcessorFn


def load_pipeline(config_path: str) -> List[ProcessorFn]:
    # Load the pipeline configuration from the YAML file
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    pipeline = []
    for step in config['pipeline']:
        processor_path = step['type']
        module_name, function_name = processor_path.rsplit('.', 1)

        try:
            # Dynamically import the function from its module
            module = importlib.import_module(module_name)
            function = getattr(module, function_name)
            pipeline.append(function)
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Error loading processor {processor_path}: {e}")

    return pipeline
