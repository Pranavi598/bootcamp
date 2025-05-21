import sys
from routing.dag_runner import DAGRunner
from util.file_utils import read_lines
from util.config_loader import load_config  # ✅ Now valid

def main():
    config_path = sys.argv[1]
    input_file = sys.argv[2]

    print(f"🔧 Loading config from: {config_path}")
    print(f"📄 Reading input from: {input_file}")

    config = load_config(config_path)
    lines = read_lines(input_file)

    print(f"🧪 Input lines: {lines}")

    runner = DAGRunner(config)
    runner.run(lines)

if __name__ == "__main__":
    main()
