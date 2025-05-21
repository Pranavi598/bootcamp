Level 0 – Basic Script (No Abstraction)

This is the first level of the Dataflow Framework Bootcamp. At this stage, we focus on writing a simple, single-purpose script that processes text line by line. There are no abstractions, no functions — just raw sequential Python code.

## 🎯 Objective

The goal is to build a working script that:

- Reads from standard input (`stdin`)
- Strips leading and trailing whitespace
- Converts each line to uppercase
- Writes the processed lines to standard output (`stdout`)

## 📁 File Structure

```
abstraction_level_0/
└── process.py     # Your basic processing script (no functions or modules)
```

## ▶️ How to Run

You can run the script from the command line using input redirection:

```bash
python process.py < input.txt
```

Where `input.txt` is any text file containing lines you want to process.

## 🧪 Example

### input.txt

```
  hello world  
  
```

### Command

```bash
python process.py < test.txt
```

### Output

```
HELLO WORLD

```

## 🚫 Constraints

- ❌ No functions
- ❌ No custom modules
- ✅ Only use Python built-in tools
- ✅ One file only (`process.py`)
- ✅ Sequential code only (top-to-bottom logic)

## ✅ Checklist

- [x] Script produces expected output for sample input
- [x] Runs cleanly from the command line
- [x] No functions or abstractions introduced

#