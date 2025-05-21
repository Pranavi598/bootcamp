global_x = 50  # Global variable

def modify_global_variable():
    global global_x
    global_x += 10
    print("Global variable modified inside function:", global_x)

if __name__ == "__main__":
    print("Before function call:", global_x)
    modify_global_variable()
    print("After function call:", global_x)
