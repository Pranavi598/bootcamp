def faulty():
    print(x)  # Error: local variable 'x' referenced before assignment
    x = 10

if __name__ == "__main__":
    try:
        faulty()
    except UnboundLocalError as e:
        print("Scope error:", e)

