# Documentation – Level 4: Stream Processing and State

## 🎯 Objective

Migrate from simple `str -> str` processors to fully streaming `Iterator[str] -> Iterator[str]` processors to support more advanced transformations, including stateful and fan-in/out operations.

---

## 🧩 Modules Overview

### 1. `main.py`
- Orchestrates input reading, processor pipeline, output writing.

### 2. `cli.py`
- Typer-based CLI:
  - `--input`: input file
  - `--output`: optional output
  - `--config`: processor YAML

### 3. `core.py`
- Core logic for applying a pipeline of `Iterator[str] -> Iterator[str]` processors.

### 4. `pipeline.py`
- Loads processor config from YAML
- Dynamically imports and initializes each processor

### 5. `types.py`
```python
Processor = Callable[[Iterator[str]], Iterator[str]]
```

---

## 🧠 Processor Types

### ✅ Stateless (wrapped)
```python
def to_uppercase(line: str) -> str

# Converted to stream:
def stream_wrapper(fn: Callable[[str], str]) -> Processor
```

### ✅ Stateful
```python
class LineCounter:
    def __init__(self): self.count = 0
    def __call__(self, lines: Iterator[str]) -> Iterator[str]
```

### ✅ Fan-In
```python
class JoinProcessor:
    def __call__(self, lines: Iterator[str]) -> Iterator[str]
    # Joins 2 lines -> 1
```

### ✅ Fan-Out
```python
class SplitProcessor:
    def __call__(self, lines: Iterator[str]) -> Iterator[str]
    # "A B" -> ["A", "B"]
```

---

## 📦 Configuration (`pipeline.yaml`)

```yaml
pipeline:
  - type: processors.upper.to_uppercase
  - type: processors.counter.LineCounter
  - type: processors.splitter.SplitProcessor
```

---

## 📌 Highlights

- Dynamic function/class import via `importlib`.
- Config-driven processor initialization (supports parameters).
- Compatible with Level 3 structure.

---

## 🧪 Testing

- Test each stream processor with mocked `Iterator[str]`.
- Test both wrapped and stateful processors in isolation.

---

## ✅ Checklist

- [x] All processors conform to `Iterator[str] -> Iterator[str]`
- [x] Fan-in, fan-out behaviors implemented
- [x] At least one stateful class-based processor
- [x] Clean separation of init/config and logic
- [x] Legacy function reuse supported via wrapper
