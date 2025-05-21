
def main():
    my_dict = {"a": 1, "b": 2}
    key = "c"

    try:
        value = my_dict[key]
        print(f"[EAFP] Value: {value}")
    except KeyError:
        print("[EAFP] Key not found!")

if __name__ == "__main__":
    main()
