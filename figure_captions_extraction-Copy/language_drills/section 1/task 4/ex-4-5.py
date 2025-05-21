def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count:", count)

    increment()
    increment()

if __name__ == "__main__":
    counter()
