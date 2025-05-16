# multiple_unpack_example.py

def main():
    a, b, *rest = [1, 2, 3, 4, 5]
    print(f"a = {a}, b = {b}, rest = {rest}")

if __name__ == "__main__":
    main()
