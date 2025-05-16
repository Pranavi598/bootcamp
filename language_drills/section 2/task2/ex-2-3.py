# any_all_example.py

def main():
    numbers = [1, -2, 3, 4]

    if any(num < 0 for num in numbers):
        print("[any] There is at least one negative number.")

    if all(num > 0 for num in numbers):
        print("[all] All numbers are positive.")
    else:
        print("[all] Not all numbers are positive.")


if __name__ == "__main__":
    main()
