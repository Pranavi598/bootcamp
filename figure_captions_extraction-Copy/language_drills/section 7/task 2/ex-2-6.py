def main():
    result = sum(x for x in range(1000000))  # Avoid creating a temporary list
    print(f"Sum: {result}")

if __name__ == "__main__":
    main()
