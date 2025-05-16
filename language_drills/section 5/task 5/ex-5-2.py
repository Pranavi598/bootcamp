import subprocess


def main():
    # Run a command and capture the output
    result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)

    print("Command output:", result.stdout)


if __name__ == "__main__":
    main()
