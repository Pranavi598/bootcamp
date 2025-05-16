# Pranavi Hello 👋

A simple and evolving Python package that demonstrates:

- Basic Python packaging (`ex-basics-1`)
- Using rich libraries like `rich` for better CLI UX (`ex-basics-2`)
- Creating a beautiful CLI application using `typer` (`ex-basics-3`)

---

## 📦 Installation

You can install this package directly from [TestPyPI](https://test.pypi.org):

```bash
pip install -i https://test.pypi.org/simple pranavi-hello
```

---

## 🚀 Usage

### ex-basics-1: Basic Hello

```bash
python -m pranavi_hello
# Output: Hello, world!

python -m pranavi_hello --name Pranavi
# Output: Hello, Pranavi!
```

---

### ex-basics-2: Rich Output

This version enhances the output using the [`rich`]library:

```bash
python -m pranavi_hello --name Keifer
# Output: [bold green]Hello, Keifer![/bold green]
```

---

### ex-basics-3: CLI App using Typer

This version uses [`typer`]to expose a proper CLI:

```bash
pranavi-hello --name Angelo
# Output: Hello, Angelo!

# Or use the default
pranavi-hello
# Output: Hello, world!
```

---

## 📚 Features

- ✅ Clean and simple Python package
- ✅ Rich text formatting using `rich`
- ✅ CLI interface using `typer`
- ✅ TestPyPI publishing support

---

## 🔗 Package Link

📦 [Pranavi Hello on TestPyPI](https://test.pypi.org/manage/project/pranavi-hello)

---

## 🛠️ Development

To run locally:

```bash
git clone https://github.com/Pranavi598/pranavi-hello.git
cd pranavi-hello
python -m venv .venv
source .venv/bin/activate  # Or .\.venv\Scripts\activate on Windows
pip install -e .[dev]
```


