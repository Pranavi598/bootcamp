# Level 4 – Stream Processing and State

This level introduces true streaming processors: instead of line-by-line transformations, processors now operate over line streams. This unlocks more powerful features like stateful processing, fan-in/fan-out, and buffer-based logic.

## 🔄 New Features

- **Stream-Based Interface**: Processors accept `Iterator[str]` and return `Iterator[str]`.
- **Line Count & State Tracking**: Enable internal memory per processor.
- **Fan-In / Fan-Out**: Processors can emit more or fewer lines.
- **Reusability**: Old `str -> str` processors wrapped for compatibility.

## 🧱 Processor Types

- `Stateless`: e.g. `to_uppercase`, `to_snakecase` (wrapped).
- `Stateful`: e.g. LineCounter (adds count prefix to each line).
- `Fan-Out`: e.g. SplitProcessor (splits a line into multiple).
- `Fan-In`: e.g. JoinProcessor (joins every 2 lines into one).

## 📂 File Structure

```
abstraction-level-4/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── types.py
├── processors/
│   ├── upper.py
│   ├── snake.py
│   ├── counter.py
│   ├── splitter.py
│   └── joiner.py
└── pipeline.yaml
```

## 🛠️ Setup

1. **Install requirements**:
   ```bash
   pip install typer pyyaml
   ```

2. **Run pipeline**:
   ```bash
   python main.py --input input.txt --config pipeline.yaml
   ```

## ✅ Example Processors

```yaml
pipeline:
  - type: processors.upper.to_uppercase
  - type: processors.counter.LineCounter
```

## ✅ Checklist

- [x] Stream processors using `Iterator[str] -> Iterator[str]`
- [x] Fan-in/fan-out support
- [x] Line-counting stateful processor
- [x] Configurable initialization logic
- [x] Old `str -> str` logic reusable via wrappers
