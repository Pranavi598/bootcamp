# Documentation – Level 5: DAG Routing and Conditional Flows

## 🎯 Objective

The goal of this level is to enhance the pipeline to support a Directed Acyclic Graph (DAG)-based processing system. Each line of input will be routed through different paths based on its content, represented by tags (e.g., `error`, `warn`, `general`). This flexibility allows different processors to handle lines differently, enabling conditional processing paths.

---

## 🧩 Modules Overview

### `main.py`
- **Role**: Entry point of the pipeline.
- **Responsibilities**:
  - Reads input from `input.txt`.
  - Initializes and runs the pipeline using the configurations in `pipeline.yaml`.
  - Writes the final output to `out.txt`.

### `processors/`
This folder contains various processors responsible for transforming, tagging, and handling lines.

#### **`archive.py`**
- **Role**: Archives lines tagged as errors.
- **Input**: Lines tagged as `"error"`.
- **Output**: Lines saved to a separate error log or archive.

#### **`count.py`**
- **Role**: Counts the number of lines processed.
- **Input**: Any line.
- **Output**: The count of processed lines.

#### **`format.py`**
- **Role**: Formats lines according to predefined rules (e.g., trimming, adding timestamps).
- **Input**: Any line.
- **Output**: Formatted version of the input line.

#### **`print_line.py`**
- **Role**: Prints each processed line to the console or log.
- **Input**: Any line.
- **Output**: Print output.

#### **`splitter.py`**
- **Role**: Splits each line into multiple lines based on custom delimiters.
- **Input**: A single line.
- **Output**: Multiple lines after splitting.

#### **`tag_error.py`**
- **Role**: Tags lines that match the "error" criteria.
- **Input**: A line that may contain an error.
- **Output**: A tagged line with the `error` tag.

#### **`tag_warn.py`**
- **Role**: Tags lines that match the "warning" criteria.
- **Input**: A line that may contain a warning.
- **Output**: A tagged line with the `warn` tag.

#### **`tally.py`**
- **Role**: Tallies the number of warning and error lines.
- **Input**: Lines tagged as `warn` or `error`.
- **Output**: A count of warnings and errors.

### `routing/`
This folder contains components for routing and managing the flow of lines through different processors.

#### **`dag_runner.py`**
- **Role**: The engine responsible for running the DAG-based pipeline.
- **Responsibilities**:
  - Routes each line to the correct processor based on its tags.
  - Ensures lines are processed in the correct order, respecting the DAG.

#### **`types.py`**
- **Role**: Defines necessary types for routing and processor logic.
- **Responsibilities**:
  - Includes data types that help define the flow of tagged lines through the DAG.

### `util/`
This folder contains utility modules that support the pipeline.

#### **`config_loader.py`**
- **Role**: Loads configuration settings from `pipeline.yaml`.
- **Responsibilities**:
  - Parses the YAML file and returns the necessary configuration to initialize processors and routing.

#### **`file_utils.py`**
- **Role**: Provides utility functions for file handling (e.g., reading and writing files).
- **Responsibilities**:
  - Handles the reading of `input.txt` and writing to `out.txt`.

---

## 🧠 Key Concepts

### 1. **DAG-Based Processing**
- A Directed Acyclic Graph (DAG) defines the pipeline's structure, where each node (processor) can take different routes based on tags.
- Lines are routed to different processors depending on the tags assigned to them.
- Processors can fan-out to multiple processors based on conditions, and fan-in is supported where multiple inputs feed into a processor.

### 2. **Tagged Lines**
- Each processor in the pipeline can add tags to the lines it processes.
- Tags such as `"error"`, `"warn"`, and `"general"` help route the line to specific processors.
- Tags can be used to filter and direct the flow of data based on the line's content.

### 3. **Configuration-Driven Routing**
- The routing behavior of the DAG is defined in the `pipeline.yaml` file.
- This file specifies which processors to run and their order, as well as the tags and routing rules.

### 4. **Modular Processors**
- Each processor handles a specific part of the processing.
- Processors are designed to be modular and reusable, enabling the addition of new processors as needed.
- Processors can maintain internal state (e.g., counts, accumulations) or be stateless.

---

## 📦 Configuration (`pipeline.yaml`)

The configuration file `pipeline.yaml` defines the flow of data and the processors to be used in the pipeline. Here’s an example configuration:

```yaml
pipeline:
  - type: processors.trim.TrimProcessor
  - type: processors.tagger.TaggerProcessor
  - type: processors.tag_error.TagErrorProcessor
    tags: ["error"]
  - type: processors.tag_warn.TagWarnProcessor
    tags: ["warn"]
  - type: processors.splitter.SplitterProcessor
  - type: processors.archive.ArchiveProcessor
    tags: ["error"]
  - type: processors.tally.TallyProcessor
```

### Explanation of the Configuration:
- The pipeline consists of a sequence of processors.
- Each processor can be configured with specific tags that determine when it should be triggered.
- The `TagErrorProcessor` and `TagWarnProcessor` add the `"error"` and `"warn"` tags, respectively, which are then used to route lines to appropriate processors like `ArchiveProcessor` or `TallyProcessor`.

---

## 🧪 Testing

Testing is crucial for ensuring that the system works as expected:

### **Unit Testing**:
- Each processor should be unit tested to verify its logic (e.g., `TagErrorProcessor` correctly tags error lines).
  
### **Integration Testing**:
- End-to-end tests ensure that lines are correctly routed based on tags and processed by the right processors.

---

## ✅ Checklist

- [x] Implemented tagged routing where lines are routed based on tags.
- [x] Created a DAG-based system that allows dynamic branching based on tags.
- [x] Processors are configurable through `pipeline.yaml`.
- [x] Designed modular processors for processing lines.
- [x] End-to-end tests ensure correctness of the pipeline and routing.

--- 

## 🛠️ Troubleshooting

- **Issue**: Processor is not receiving the correct lines.
  - **Solution**: Check the `pipeline.yaml` file for incorrect tag assignments or routing issues.
  
- **Issue**: Line is not being tagged correctly.
  - **Solution**: Verify the logic inside the tagging processors (`TagErrorProcessor`, `TagWarnProcessor`).
  
- **Issue**: Output is not being written to `out.txt`.
  - **Solution**: Check the file paths and permissions for writing output files.



