import pickle


def main():
    # Use pickle.dump() and load() on a basic object
    data = {"name": "Alice", "age": 30}

    # Serialize with pickle
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)

    # Deserialize with pickle
    with open('data.pickle', 'rb') as file:
        loaded_data = pickle.load(file)
        print("Loaded Pickled Data:", loaded_data)


if __name__ == "__main__":
    main()
