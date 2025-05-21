class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        print(f"{self.greeting}, {name}!")

def main():
    greeter = Greeter("Hello")
    greeter("Alice")  # Calls __call__()

if __name__ == "__main__":
    main()
