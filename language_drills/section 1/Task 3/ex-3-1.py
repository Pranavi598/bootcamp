# Task 1: Default Arguments (Command-Line Program)
def greet(name="Guest"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    import sys
    # If name is passed as a command-line argument, greet the name; otherwise, greet with default "Guest"
    name = sys.argv[1] if len(sys.argv) > 1 else "Guest"
    greet(name)
