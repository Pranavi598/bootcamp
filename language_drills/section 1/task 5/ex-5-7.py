def name_shadowing_example():
    local_len = 5
    print("Shadowed 'len' as variable:", local_len)
    try:
        # This would normally raise TypeError if len() is shadowed globally
        length = len("hello")
        print("Built-in len('hello') still works:", length)
    except TypeError as e:
        print("TypeError:", e)

if __name__ == "__main__":
    name_shadowing_example()
