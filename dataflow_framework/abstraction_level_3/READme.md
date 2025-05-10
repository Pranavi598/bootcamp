# Level 3 – Dynamic Config-Driven Pipeline

This level introduces configuration-driven processing pipelines. Instead of hardcoding transformation logic, the user provides a YAML configuration specifying which functions to apply and in what order.

## Features

- 📄 **YAML-Based Pipeline**: Define processors using dotted import paths.
- 🔄 **Dynamic Import**: Load processor functions at runtime.
- 🧩 **Composable**: Add your own processors without modifying core logic.
- 🖥️ **CLI**: Use Typer to control the program via command-line arguments.

## Example `pipeline.yaml`

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```

## File Structure

```
abstraction-level-3/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── types.py
├── processors/
│   ├── upper.py
│   └── snake.py
└── pipeline.yaml
```

## Setup Instructions

1. **Install dependencies**
   ```bash
   pip install typer pyyaml
   ```

2. **Run the script**
   ```bash
   python main.py --input input.txt --config pipeline.yaml
   ```

3. **Output**
   - Transformed lines printed to terminal or written to output file (if `--output` is used).

## Notes

- All processor functions must follow the `str -> str` signature.
- Helpful errors are shown for invalid paths in the YAML config.
