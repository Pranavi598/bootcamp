def demonstrate_nonlocal():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count incremented to:", count)

    increment()
    increment()

if __name__ == "__main__":
    demonstrate_nonlocal()
