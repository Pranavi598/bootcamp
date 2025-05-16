import json
import pickle


def main():
    # Discuss dangers of pickle and show safe alternatives (json, marshal)
    print("Warning: Unpickling data from untrusted sources can lead to arbitrary code execution.")

    # Safe alternative: JSON (serialization and deserialization)
    data = {"name": "Alice", "age": 30}
    safe_json = json.dumps(data)
    loaded_data = json.loads(safe_json)
    print("Safe data (using JSON):", loaded_data)

    # Avoid using pickle for untrusted data
    # Always prefer JSON or other safer serialization formats.


if __name__ == "__main__":
    main()
