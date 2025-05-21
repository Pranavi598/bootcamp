x = 10  # Global scope

def demo():
    x = 20  # Local scope
    print("Inside function:", x)

if __name__ == "__main__":
    demo()
    print("Outside function:", x)
