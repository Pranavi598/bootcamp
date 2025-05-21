# Level 1 Documentation – Parameters and CLI Interface

## 📌 Purpose

In this level, we focus on turning our previously monolithic script into a parameterized tool by adding command-line arguments. This makes the script more configurable and allows users to control its behavior via the CLI. We also introduce the use of environment variables to set default values for certain parameters.

## ⚙️ Key Features

1. **Command-Line Interface (CLI)**:
   - Uses `typer` to define a clean and intuitive CLI.
   - Supports required (`--input`) and optional (`--output`, `--mode`) arguments.

2. **Environment Configuration**:
   - The script loads default values (like `mode`) from an `.env` file using `python-dotenv`.

3. **Processing Modes**:
   - `uppercase`: Converts each line to uppercase.
   - `snakecase`: Replaces spaces with underscores and converts to lowercase.

4. **Modular Functions**:
   - `read_lines(path: str) -> Iterator[str]`: Reads lines from a file.
   - `transform_line(line: str, mode: str) -> str`: Transforms a line based on the mode.
   - `write_output(lines: Iterator[str], output_path: Optional[str]) -> None`: Writes processed lines to a file or prints to `stdout`.

## 💡 Technical Details

- **`typer`** is used for building the command-line interface. It helps define required and optional arguments with ease.
- **`.env`** file stores default configuration values (like processing mode) to be loaded at runtime using `python-dotenv`.
- **String transformations** are handled via basic Python string methods:
  - **Uppercase mode**: `line.upper()`
  - **Snakecase mode**: `line.replace(" ", "_").lower()`

## 🧑‍💻 How to Run

1. Ensure your `.env` file is in place to specify defaults.
2. Use the `--input` flag to specify the input file path.
3. Optionally, use `--output` to specify an output file, or leave it blank to print to `stdout`.
4. Optionally, use `--mode` to select the transformation mode.

### Example:

```bash
python process.py --input input.txt --mode snakecase
```

### Expected Output:

```
hello_world
python_is_awesome
let's_code!
```

## ⚠️ Limitations

- The script is still monolithic (i.e., all code is within a single file).
- There’s minimal error handling (no validation for file paths, etc.).
- The environment configuration is simplistic and only supports a basic `mode`.

## ✅ Conclusion

This stage focuses on taking a simple script and making it configurable. By introducing parameters, environment variables, and basic CLI handling, we prepare the code for future refactoring and modularization in the upcoming levels.

## 📌 What's Next?

In the following levels, we will:
- Separate the functionality into different modules for better organization.
- Add more sophisticated processing logic and error handling.
- Expand the CLI with additional commands and options.

This level sets the foundation for a tool that can grow and be reused across various tasks in your data processing pipeline.
