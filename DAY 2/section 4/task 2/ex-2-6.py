def role_required(role):
    """Decorator to check if a user has the required role"""
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                raise PermissionError("You do not have the required role!")
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_role, user_id):
    return f"User {user_id} deleted"

def main():
    print(delete_user("admin", 123))  # Works
    print(delete_user("user", 123))  # Raises PermissionError

if __name__ == "__main__":
    main()
