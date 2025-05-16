import tempfile


def main():
    # Create a temporary file and write to it
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Temporary file content")
        temp_file_name = temp_file.name
        print(f"Temporary file created: {temp_file_name}")

    # Ensure the file is closed and can be accessed manually
    with open(temp_file_name, "r") as file:
        print(f"Content of temp file: {file.read()}")


if __name__ == "__main__":
    main()
