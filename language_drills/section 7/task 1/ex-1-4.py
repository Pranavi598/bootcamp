# Save this as line_profile_example.py
# Run with: kernprof -l -v line_profile_example.py

@profile
def slow_function():
    total = 0
    for i in range(10000):
        total += i * i
    return total

def main():
    print(slow_function())

if __name__ == "__main__":
    main()
