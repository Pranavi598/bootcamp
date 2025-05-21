def info(name, age=0):
    return f"Name: {name}, Age: {age}"

if  __name__ == "__main__":
    print("\nTask 2: Keyword Arguments")
    print(info(age=25, name="Alice"))
    print(info(name="Bob"))
