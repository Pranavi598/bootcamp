import subprocess
import time


def main():
    # Start a long subprocess and terminate it after a delay
    process = subprocess.Popen(["sleep", "60"])  # 'sleep 60' simulates a long-running process

    print("Subprocess started.")
    time.sleep(2)

    process.terminate()  # Terminate the subprocess
    print("Subprocess terminated.")


if __name__ == "__main__":
    main()
