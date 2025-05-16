# Task 6: Positional-Only Args
def pos_only(x, y, /):
    return f"Positional-only args: x={x}, y={y}"

def main_task_6():
    print("\nTask 6: Positional-Only Arguments")
    print(pos_only(10, 20))  # Valid usage: positional arguments
    # Uncommenting the following line will raise an error:
    # print(pos_only(x=10, y=20))  # This would raise a TypeError

# Entry point
if __name__ == "__main__":
    main_task_6()
