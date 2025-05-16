# use_and_for_guarded_expression_example.py

def main():
    is_admin = bool(int(input("Are you an admin? Enter 1 for Yes, 0 for No: ")))
    user_id = input("Enter user ID to delete: ")

    # Guarded expression: Execute if is_admin is True
    is_admin and print(f"Deleting user {user_id}...")


if __name__ == "__main__":
    main()
