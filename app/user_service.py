def get_user_email(user):
    return user.get("email", None)

def is_admin(user):
    return user.get("role") == "admin"

def get_user_profile_summary(user):
    if not isinstance(user, dict):
        raise TypeError("User must be a dictionary")

    name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip()
    email = user.get("email", "N/A")
    role = user.get("role", "user")
    active = "active" if user.get("is_active", False) else "inactive"

    return f"{name} ({email}) - {role} [{active}]"

def is_user_new():
    """
    is_admin responsible for checking which user is admin
    """
    new_user = 1
    if new_user != 1:
        print("new user added")