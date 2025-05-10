# Level 6 – State-Based Routing System

## Overview

In this level, you will build a **state-based routing engine**. This engine routes lines based on tags and handles dynamic, tag-based routing where processors represent states and transitions occur depending on the tags. The system also supports cyclic routing, feedback loops, and flexible configuration.

## Features

- **Dynamic Routing**: Lines are routed based on tags. Each line is tagged, and processors are triggered depending on these tags.
- **Tag-Based Transitions**: Processors are registered with specific tags, and lines transition through the system depending on those tags.
- **State Transitions**: The system behaves like a state machine. Tags act as state labels, and processors perform state transitions.
- **Fan-In/Fan-Out**: Multiple processors can handle lines with different tags, allowing fan-out (multiple downstream processors) and fan-in (multiple upstream processors).
- **Cyclic Routing**: Tags can loop back to earlier processors, allowing for feedback or retry mechanisms.
- **Configuration-Driven**: The routing behavior is defined in the `pipeline.yaml` file.

## Project Structure

```
abstraction_level_6/
├── config/
│   └── pipeline.yaml         # Configuration file defining the routing flow
├── processors/
│   ├── __init__.py
│   ├── filters.py            # Contains filtering logic like error or warning filters
│   ├── formatters.py         # Contains formatters like snakecase
│   ├── output.py             # Outputs lines to the terminal or other formats
│   └── start.py              # Start processor for routing logic
├── routing/
│   └── state_router.py       # Main engine to handle tag-based routing
├── util/
│   └── config_loader.py      # Loads the pipeline configuration file
├── input.txt                 # Input data to process
├── main.py                   # Entry point for the routing system
└── README.md
```

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the system**:
   ```bash
   python main.py --input input.txt --output out.txt --config config/pipeline.yaml
   ```

3. **Check the output**:  
   The processed lines will be written to `out.txt`.

## Testing

- **Add new tags**: Test new tags and ensure they are correctly routed through the system.
- **Check routing behavior**: Validate if the lines are correctly routed based on tags.
- **Cycle handling**: Test cyclic routing to ensure no infinite loops.
```

