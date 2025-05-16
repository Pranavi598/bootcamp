# Task 4: Variable Keyword Args
def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

def main_task_4():
    print("\nTask 4: Variable Keyword Arguments")
    # Calling show_settings with keyword arguments inside main_task_4
    show_settings(theme="Light", language="Python", version="3.11")

# Entry point
if __name__ == "__main__":
    main_task_4()
