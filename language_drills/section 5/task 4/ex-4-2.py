import json


def main():
    # Dump a JSON string with indentation and sorting keys
    data = {"name": "Alice", "age": 30, "city": "New York"}

    # Pretty print the JSON
    pretty_json = json.dumps(data, indent=4, sort_keys=True)
    print("Pretty JSON:", pretty_json)


if __name__ == "__main__":
    main()
