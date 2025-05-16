x = 5

def modify_global():
    global x
    x = 100
    print("Inside function:", x)

if __name__ == "__main__":
    modify_global()
    print("Outside function:", x)
