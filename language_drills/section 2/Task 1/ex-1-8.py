# lbyl_type_check.py

def main():
    value = "hello"

    if isinstance(value, int):
        print(f"[LBYL] Double the number: {value * 2}")
    else:
        print("[LBYL] Not an integer, skipping operation.")

if __name__ == "__main__":
    main()
