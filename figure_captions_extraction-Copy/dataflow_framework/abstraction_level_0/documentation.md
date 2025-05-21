# Level 0 Documentation – Basic Script (No Abstraction)

## 📌 Purpose

This level serves as the baseline for understanding how input processing works in Python. It helps you appreciate the improvements you'll make later when you modularize and refactor the code.

## ⚙️ Script Behavior

- Reads from `stdin`
- For each line:
  - Trims leading and trailing whitespace
  - Converts the line to uppercase
  - Outputs the processed line to `stdout`

## 💡 Technical Notes

- Only built-in Python features are used
- No `def`, `class`, or `import` statements
- Designed to be simple, direct, and without abstraction

## 🧑‍💻 How to Run

1. Create a file named `test.txt` with any sample text (one line per entry).
2. Run the script using input redirection:

```bash
python process.py < test.txt
```

3. Output will be printed directly to your terminal window.

## 📥 Example Input and Output

### Input (`test.txt`)
hello world

### Output
HELLO WORLD

## ⚠️ Limitations

- Not reusable across other scripts
- Cannot handle input files directly (stdin-only)
- No error handling or custom logic — just line transformation

## ✅ Conclusion

This stage is about getting it to work, not making it elegant. Later stages will show how to structure this for reuse, clarity, and testability.
