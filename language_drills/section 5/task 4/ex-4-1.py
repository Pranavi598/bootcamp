import json


def main():
    # Serialize and deserialize a Python dict using json.dumps() and json.loads()
    data = {"name": "Alice", "age": 30}

    # Serialize to JSON
    json_data = json.dumps(data)
    print("Serialized JSON:", json_data)

    # Deserialize back to Python dict
    deserialized_data = json.loads(json_data)
    print("Deserialized data:", deserialized_data)


if __name__ == "__main__":
    main()
