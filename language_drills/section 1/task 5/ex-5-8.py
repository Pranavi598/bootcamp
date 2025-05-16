def scope_error_example():
    try:
        print("Trying to read variable before assignment:")
        print(a)  # UnboundLocalError
        a = 10
    except UnboundLocalError as e:
        print("Caught UnboundLocalError:", e)

if __name__ == "__main__":
    scope_error_example()
