from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


fake_db = {
    "alice": {"name": "Alice", "email": "alice@example.com"},
    "bob": {"name": "Bob", "email": "bob@example.com"},
}

class UserRequest(BaseModel):
    username: str
    usertoken: int
    log: str
    external_log: str



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

def test_user():
    user_test = "test"
    return user_test

def get_user_role(user_dict):
    return user_dict.get("role", "guest")

def should_user_be_active(user_active):
    return user_active == "active"

def should_user_be_admin(user: dict) -> bool:
    return user.get("is_active") == True and user.get("role") == "admin"

def has_access_to_feature(user: dict, feature_flag: str) -> bool:
    """
    Returns True if the user has the requested feature enabled.
    """
    features = user.get("features", [])
    return feature_flag in features

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


@app.post("/get-user-token")
def get_user_list(data: UserRequest):
    user = fake_db.get(data.usertoken.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User token not found")
    return user

@app.post("/get-user-logs")
def get_user_test(data: UserRequest):
    user = fake_db.get(data.log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User log not found")
    return user

@app.post("/get-user-external-logs")
def get_user_test(data: UserRequest):
    user = fake_db.get(data.log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User external log not found")
    return user

@app.post("/get-user-external-logs-gcp")
def get_user_test(data: UserRequest):
    user = fake_db.get(data.log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User external GCP log not found")
    return user