# 📚 Level 2 – Documentation

## 🧠 Overview

In Level 2, the goal is to transform a working CLI script into a **modular**, **extensible**, and **cleanly designed** tool. This structure promotes code reuse, testability, and future enhancements like dynamic plugin loading or custom pipelines.

---

## 🗂️ File Structure

```
abstraction-level-2/
├── main.py         # Entry point: coordinates file I/O and processing
├── cli.py          # Typer-based CLI app
├── core.py         # Contains individual processors
├── pipeline.py     # Constructs a pipeline of processors based on mode
└── types.py        # Defines the ProcessorFn callable type
```

---

## 🧩 Processor Interface

All processors follow a **standard signature** for consistency and composition:

```python
ProcessorFn = Callable[[str], str]
```

This enables us to chain them like:

```python
line = to_uppercase(line)
line = to_snakecase(line)
```

Or dynamically apply them via:

```python
for processor in processors:
    line = processor(line)
```

---

## 🛠️ Available Processors (in `core.py`)

- `to_uppercase(line: str) -> str`: Converts line to uppercase.
- `to_snakecase(line: str) -> str`: Replaces spaces with underscores and converts to lowercase.

---

## 🔄 Modes (in `pipeline.py`)

- `uppercase`: Uses `[to_uppercase]`
- `snakecase`: Uses `[to_snakecase]`
- Default mode is loaded from `.env` using `python-dotenv`

---

## 📥 CLI Usage (via `cli.py`)

Run from terminal:

```bash
python main.py --input input.txt --output out.txt --mode snakecase
```

### Options:

- `--input`: Path to the input text file (**required**)
- `--output`: Path to save the output (**optional**, defaults to stdout)
- `--mode`: Transformation mode (`uppercase`, `snakecase`, etc.)

---

## 🧪 Testing Checklist

- [x] Is each module doing only one thing?
- [x] Are processors clearly separated and composable?
- [x] Does CLI still work correctly?
- [x] Can a new processor be added easily by modifying `core.py` and `pipeline.py`?
- [x] Is the `.env` default mode loaded correctly?

---

## 📌 Example

```bash
# Uppercase default from .env
python main.py --input data.txt

# Snakecase with output written to file
python main.py --input data.txt --output out.txt --mode snakecase
```

---

## ✅ Conclusion

This level lays the foundation for a scalable data processing tool. With a modular architecture and processor interface, it's now easy to add, test, and reuse functionality in future levels.
