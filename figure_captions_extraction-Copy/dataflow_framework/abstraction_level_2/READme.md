# Level 2 – Modular Structure and Standardized Processing

This level refactors the Level 1 script into a clean, modular structure, where each file has a clear responsibility. It also introduces a standardized interface for text processors, enabling a flexible and composable transformation pipeline.

## 🎯 Objective

Refactor the CLI tool into a proper multi-file project structure:

```
abstraction-level-2/
├── main.py         # Entry point: reads input and writes output
├── cli.py          # Defines CLI with typer
├── core.py         # Core processing functions and logic
├── pipeline.py     # Selects processor pipeline based on mode
└── types.py        # Defines ProcessorFn type alias
```

## 🧱 Key Features

- **Modular structure**: Clean separation between CLI, core logic, and configuration.
- **Composable processing**: Define each transformation as a function (`ProcessorFn`) and apply them in sequence.
- **Dynamic pipeline**: Based on the mode, build a list of processors to apply.
- **CLI**: Continues to use `typer` for user-friendly interaction.

## 🧩 Modules Explained

- `main.py`: Handles file I/O, reads input, applies processors, writes/prints output.
- `cli.py`: Contains the typer app and CLI definition.
- `core.py`: Implements processors like `to_uppercase` and `to_snakecase`.
- `pipeline.py`: Builds the processor pipeline (`List[ProcessorFn]`) based on the mode.
- `
