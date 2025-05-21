import subprocess

def main():
    # Run a command to list files in the current directory
    result = subprocess.run(["ls", "-l"], check=True)
    print("Command executed successfully.")

if __name__ == "__main__":
    main()
