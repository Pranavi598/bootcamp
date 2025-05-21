import threading
import argparse
from utils.dag_runner import run_pipeline
from dashboard.server import start_dashboard

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", action="store_true", help="Enable tracing")
    args = parser.parse_args()

    # Start dashboard on a separate thread
    threading.Thread(target=start_dashboard, daemon=True).start()

    # Define file paths
    input_path = "input.txt"  # Ensure this file exists in the working directory
    output_path = "out.txt"   # Output will be written to this file
    config_file = "dag_config.yaml"  # Path to the DAG configuration YAML file

    # Run the pipeline
    run_pipeline(input_path, output_path, config_file, enable_trace=args.trace)

if __name__ == "__main__":
    main()
