from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


fake_db = {
    "alice": {"name": "Alice", "email": "alice@example.com"},
    "bob": {"name": "Bob", "email": "bob@example.com"},
}

class UserRequest(BaseModel):
    username: str


def get_user_email(user):
    return user.get("email", None)

def is_admin(user):
    return user.get("role") == "admin"

def get_user_profile_summary(user):
    """
    Returns a string summary of the user profile.
    Includes name, email, role and active status.
    """
    if not isinstance(user, dict):
        raise TypeError("User must be a dictionary")

    name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip()
    email = user.get("email", "N/A")
    role = user.get("role", "user")
    active = "active" if user.get("is_active", False) else "inactive"

    return f"{name} ({email}) - {role} [{active}]"

def new_user_created5222():
    new_user = 1
    if new_user != 0:
        return print("new user created1332")

def new_users_list():
    user_list = []
    if user_list:
        print("user list is not empty")


@app.post("/get-user")
def get_user(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/get-old-user")
def get_old_user(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="Old User not found")
    return user

@app.post("/get-user-list")
def get_user_list(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User List not found")
    return user