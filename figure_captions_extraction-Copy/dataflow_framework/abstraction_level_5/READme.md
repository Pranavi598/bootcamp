# Level 5 – DAG Routing and Conditional Flows

In this level, the pipeline evolves into a flexible DAG-based routing system. Each line can take a different route through the processing chain based on its content or tags, allowing more complex data flows.

## 🔄 Key Features

- **Tagged Lines**: Each processor can tag its output, which is used to route lines to different paths.
- **DAG Routing**: Build a Directed Acyclic Graph (DAG) where lines are routed based on tags, defining flexible flow.
- **Conditional Processing**: Based on tags, lines can take multiple routes with different processors applied.


## 🛠️ Setup

1. **Install dependencies**:
   ```bash
   pip install typer pyyaml
   ```

2. **Run the pipeline**:
   ```bash
   python main.py --input input.txt --config pipeline.yaml
   ```

## ✅ Example Processors

```yaml
pipeline:
  - type: processors.trim.TrimProcessor
  - type: processors.tagger.TaggerProcessor
  - type: processors.error_handler.ErrorProcessor
    tags: ["error"]
  - type: processors.warning_handler.WarningProcessor
    tags: ["warn"]
