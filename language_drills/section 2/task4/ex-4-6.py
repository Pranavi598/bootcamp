# temporary_file_example.py
import tempfile

def main():
    with tempfile.TemporaryFile(mode='w+t') as tempf:
        tempf.write("This is some temporary data.\n")
        tempf.seek(0)
        print(f"Temporary file content: {tempf.read()}")

if __name__ == "__main__":
    main()
