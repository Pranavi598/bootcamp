# Save this as profile_example.py and run: python -m cProfile profile_example.py
def compute():
    return sum(i * i for i in range(10000))

def main():
    print("Computation result:", compute())

if __name__ == "__main__":
    main()
