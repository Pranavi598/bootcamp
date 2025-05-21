import sys
from util.config_loader import load_config
from routing.state_router import StateRouter

if __name__ == "__main__":
    config_path, input_path = sys.argv[1], sys.argv[2]
    config = load_config(config_path)

    with open(input_path) as f:
        input_lines = [line.strip() for line in f]

    print("🚀 Starting state-based dashboard...")
    router = StateRouter(config)
    router.run(input_lines)
