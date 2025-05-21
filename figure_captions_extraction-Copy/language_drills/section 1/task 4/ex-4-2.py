def outer():
    message = "Hello from outer"

    def inner():
        print(message)  # Accessing outer's variable

    inner()

if __name__ == "__main__":
    outer()
