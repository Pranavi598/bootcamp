
def main():
    my_dict = {"a": 1, "b": 2}
    key = "c"

    if key in my_dict:
        print(f"[LBYL] Value: {my_dict[key]}")
    else:
        print("[LBYL] Key not found!")

if __name__ == "__main__":
    main()
