def main():
    functions = [abs, str, hex]
    value = -42
    results = [func(value) for func in functions]
    print(results)  # Output: [42, '-42', '-0x2a']

if __name__ == "__main__":
    main()
