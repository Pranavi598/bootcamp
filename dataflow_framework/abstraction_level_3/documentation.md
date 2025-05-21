# Documentation – Level 3: Dynamic Config-Driven Pipeline

## 🎯 Goal

Replace the hardcoded pipeline from Level 2 with a config-based system that dynamically loads processors using import paths.

---

## 🧩 Components Overview

### 1. `main.py`
- Entry point of the app.
- Reads input, loads pipeline, applies processors, writes output.

### 2. `cli.py`
- Defines CLI using Typer.
  - `--input`: input file path
  - `--output`: optional output path
  - `--config`: required pipeline YAML config

### 3. `core.py`
- `apply_processors(lines: Iterator[str], processors: List[ProcessorFn])` – applies functions to each line.

### 4. `pipeline.py`
- Parses `pipeline.yaml`
- Dynamically loads processor functions using `importlib`.

### 5. `types.py`
```python
ProcessorFn = Callable[[str], str]
```

### 6. `processors/`
Contains transformation logic:
- `upper.py`: `to_uppercase(line)`
- `snake.py`: `to_snakecase(line)`

---

## 📂 `pipeline.yaml` Example

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```

---

## ✅ Usage

```bash
python main.py --input input.txt --config pipeline.yaml
```

---

## 🛡️ Error Handling

- Import errors are caught and shown with descriptive messages.
- Only valid `str -> str` functions are allowed.

---

## ✅ Checklist

- [x] CLI accepts input and config paths
- [x] Processor functions loaded dynamically
- [x] Follows `Callable[[str], str]` interface
- [x] Easily extendable and decoupled
