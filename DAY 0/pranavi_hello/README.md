Here is the full content in markdown as requested:


# pranavi-hello 👋

A simple Python package that says hello to the world—or to anyone you want! Built with ❤️ using [uv](https://github.com/astral-sh/uv), enhanced with [Rich](https://github.com/Textualize/rich), and packaged with [Typer](https://github.com/tiangolo/typer) to run from the command line.

## 🔧 Setup & Environment

1. Initialize the project:
 
   uv init
2.Create and activate a virtual environment:


uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
3.Start your IDE (VSCode, PyCharm, etc.) using this environment and set the Python interpreter to .venv.

🧩 Module: pranavi-hello
This module defines a function that prints a friendly greeting using Rich. By default, it greets the world.

Example Usage:

from pranavi_hello import say_hello

say_hello("Pranavi")
# Output: Hello, Pranavi 👋 (in rich format)
If no argument is provided:

python

say_hello()
# Output: Hello, World 👋
📦 Install the Package
You can install the test version of this package directly from TestPyPI:


pip install -i https://test.pypi.org/simple pranavi-hello
📦 Package Link:
👉 https://test.pypi.org/project/pranavi-hello

💻 Command Line Interface (CLI)
Install the CLI tool by installing the package. Then run:


pranavi-hello --name Alice
CLI Output Example:
Hello, Alice 👋


pranavi-hello
Output:
Hello, World 👋

⚙️ Technologies Used:

🐍 Python

⚡ uv — blazing fast dependency manager

🎨 rich — pretty terminal output

🧰 typer — CLI creation made easy

📦 TestPyPI — safe space for publishing Python packages













