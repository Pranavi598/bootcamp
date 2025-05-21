# Level 1 – Parameters and CLI Interface

In this level, we enhance the script by adding command-line arguments and configuration from environment variables. The tool becomes more flexible, allowing users to specify input files, output files, and processing modes. This brings us one step closer to a reusable tool.

## 🎯 Objective

Refactor the script to:

- Use `typer` to define a command-line interface (CLI)
- Accept command-line arguments for:
  - `--input`: Input file path (required)
  - `--output`: Output file path (optional)
  - `--mode`: Processing mode (optional, defaults via `.env`)
- Load default values (like mode) from a `.env` file using `python-dotenv`
- Implement two processing modes:
  - **uppercase**: Convert each line to uppercase
  - **snakecase**: Convert spaces to underscores and lowercase the text

## 📁 File Structure

```
abstraction_level_1/
├── process.py       # The main script with CLI and parameterized behavior
└── .env             # Environment file for default configuration (e.g., mode)
```

## ▶️ How to Run

You can run the script using the following command format:

```bash
python process.py --input input.txt
```

### Optional Arguments:

- `--input`: Path to the input file (required)
- `--output`: Path to the output file (optional)
- `--mode`: Select processing mode (`uppercase` or `snakecase`, optional)
  
The mode defaults to **uppercase** as specified in the `.env` file.

### Example Usages:

```bash
python process.py --input input.txt             # Process in uppercase mode by default
python process.py --input input.txt --mode snakecase  # Process in snakecase mode
python process.py --input input.txt --output out.txt   # Process and write to out.txt
```

## 🧪 Example Input and Output

### Input (`input.txt`):

```
Hello World
This is a Test
```

### Command:

```bash
python process.py --input input.txt --mode snakecase
```

### Output (`stdout` or `out.txt`):

```
hello_world
this_is_a_test

```

## 🚫 Constraints

- The script should handle both `--input` and `--mode` arguments.
- Default mode is **uppercase**, but it can be changed to **snakecase** via the `--mode` flag or `.env` file.
- **No major refactor yet** — you’re still working within a single file.
- Keep code modular with functions like `read_lines`, `transform_line`, and `write_output`.

## ✅ Checklist

- [x] Can process any file passed via `--input`
- [x] Defaults to **uppercase** mode via `.env`
- [x] Supports `--mode snakecase` for an alternate transformation
- [x] Can print results to `stdout` or write to a file via `--output`
- [x] Clean CLI using `typer`
- [x] Clean, modular logic with functions



