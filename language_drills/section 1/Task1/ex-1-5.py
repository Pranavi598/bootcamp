def dict_iteration(person):
    """
    Iterates over a dictionary and prints all keys and values using dict.items().
    """
    return {key: value for key, value in person.items()}

if __name__ == "__main__":
    # 5. Dictionary Iteration
    person = {"name": "Bob", "age": 30}
    iterated_dict = dict_iteration(person)
    print("Iterated Dictionary:", iterated_dict)
