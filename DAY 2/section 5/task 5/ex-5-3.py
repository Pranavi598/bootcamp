import subprocess


def main():
    # Run a command and check the exit code
    result = subprocess.run(["ls", "-l"], capture_output=True)

    if result.returncode == 0:
        print("Command executed successfully.")
    else:
        print("Command failed with exit code:", result.returncode)


if __name__ == "__main__":
    main()
