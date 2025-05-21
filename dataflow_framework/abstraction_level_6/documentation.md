Level 6: State-Based Routing System

## Overview

In this level, you will build a **state-based routing engine**. This engine routes lines based on tags and handles dynamic, tag-based routing where processors represent states and transitions occur depending on the tags. The system also supports cyclic routing, feedback loops, and flexible configuration.

## Key Concepts

### Tag-Based Routing

- **Tags**: Every line is tagged with a specific value. These tags determine the processor that will handle the line.
- **Processors**: Functions or classes that perform processing on the lines. Processors are registered under specific tags and process the lines based on those tags.
- **State Transitions**: The tags represent the transitions from one state (processor) to another.

### Fan-In/Fan-Out

- **Fan-Out**: One processor can emit lines with multiple tags, which routes the lines to multiple downstream processors.
- **Fan-In**: Multiple processors can emit the same tag, routing their output to a single processor.

### Cyclic Routing

- **Cyclic Transitions**: Tags can loop back to earlier processors, allowing for retry mechanisms, feedback, or revisiting certain stages.

### Configuration (`pipeline.yaml`)

Routing is defined by a `pipeline.yaml` file, which specifies how tags are routed to different processors. Each processor is associated with a tag, and lines flow dynamically based on those tags.

Sample `pipeline.yaml`:

```yaml
nodes:
  - tag: start
    type: processors.start.tag_lines
  - tag: error
    type: processors.filters.only_error
  - tag: warn
    type: processors.filters.only_warn
  - tag: general
    type: processors.formatters.snakecase
  - tag: end
    type: processors.output.terminal
```

### Processor Interface

Each processor implements the `process` method, which is defined as:

```python
def process(lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
    ...
```

- **Input**: A list of tuples, each containing a `tag` and a `line`.
- **Output**: A list of tuples, where each tuple contains a `next_tag` and a `processed_line`.

### Router Engine (`state_router.py`)

The **State Router** (`state_router.py`) handles the flow of lines based on tags. It uses the configuration to determine the appropriate processors for each tag and ensures that lines flow through the system as defined.

## Processor Modules

- **filters.py**: Contains filtering processors like `only_error` and `only_warn`.
- **formatters.py**: Contains formatters like `snakecase` to format the line content.
- **output.py**: Outputs the processed lines to the terminal or to other formats.
- **start.py**: The entry point for the routing, tagging lines with the `start` tag.

## Example Workflow

1. **Start**: The input lines are tagged with the `start` tag.
2. **Processing**: Processors process the lines based on the tags, yielding new `(next_tag, line)` pairs.
3. **Routing**: The system routes the lines to the correct processor based on the emitted tags.
4. **End**: The process terminates when a processor emits the `end` tag.

### Sample `pipeline.yaml` Configuration

```yaml
nodes:
  - tag: start
    type: processors.start.tag_lines
  - tag: error
    type: processors.filters.only_error
  - tag: warn
    type: processors.filters.only_warn
  - tag: general
    type: processors.formatters.snakecase
  - tag: end
    type: processors.output.terminal
```

### Extensions and Customization

- **Adding New Processors**: You can add custom processors by creating them in the `processors/` directory and then updating the `pipeline.yaml` file.
- **Customizing Flow**: Modify the `pipeline.yaml` to change the flow, add new tags, or implement new processors.
- **Handling Cycles**: The system supports cyclic routing for scenarios like retry mechanisms or feedback loops.

---

This state-based routing system allows for dynamic and flexible routing flows, enabling the creation of complex data pipelines with conditional and cyclic routing behavior.
```