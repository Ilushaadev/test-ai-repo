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
    cloud_db: str



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

def mask_email(email: str) -> str:
    """Returns a masked version of the email (e.g., a***@domain.com)."""
    if "@" not in email:
        return email
    local, domain = email.split("@")
    if len(local) <= 1:
        return "*" + "@" + domain
    return local[0] + "*" * (len(local) - 1) + "@" + domain


def normalize_username(username: str) -> str:
    """Normalizes a username by stripping whitespace and lowercasing."""
    return username.strip().lower()


def is_user_admin(user: dict) -> bool:
    """Returns True if user role is 'admin' and user is active."""
    return user.get("role") == "admin" and user.get("is_active") is True


def user_can_access_feature(user: dict, feature_name: str) -> bool:
    """Checks if a user has access to a specific feature."""
    return feature_name in user.get("features", [])


def generate_user_summary(user: dict) -> str:
    """Generates a summary string for a given user dictionary."""
    name = user.get("first_name", "") + " " + user.get("last_name", "")
    email = user.get("email", "")
    return f"{name.strip()} <{email}>"

def has_access_to_feature(user: dict, feature_flag: str) -> bool:
    """
    Returns True if the user has the requested feature enabled.
    """
    features = user.get("features", [])
    return feature_flag in features

def get_user_initials(user: dict) -> str:
    """Returns the initials of the user's name, e.g., 'John Doe' → 'JD'."""
    first = user.get("first_name", "")
    last = user.get("last_name", "")
    return (first[:1] + last[:1]).upper()


def is_valid_username(username: str) -> bool:
    """Checks if username is alphanumeric and between 3–15 characters."""
    return username.isalnum() and 3 <= len(username) <= 15


def count_user_logins(logins: list) -> int:
    """Counts how many times the user has logged in, ignoring None values."""
    return len([x for x in logins if x is not None])


def format_user_role(role: str) -> str:
    """Returns a title-cased version of the role with fallback."""
    if not role:
        return "User"
    return role.strip().title()


def has_required_fields(user: dict) -> bool:
    """Checks that the user has all required fields."""
    required = ["first_name", "last_name", "email"]
    return all(field in user and user[field] for field in required)


def is_test_environment(env: str) -> bool:
    """Determines if the current environment is a testing one."""
    return env.lower() in ["test", "testing", "staging"]

def is_prod_environment(env: str) -> bool:
    """Determines if the current environment is a prod one."""
    return env.lower() in ["prod", "production"]

def is_user_in_environment(env: str) -> bool:
    """Determines if the user exists in the environment."""
    return env.lower() in ["prod", "production", "staging"]

def check_if_data_exists(user: str) -> bool:
    return user in ["test", "aws", "gcp"]


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


@app.post("/get-user-token")
def get_user_list(data: UserRequest):
    user = fake_db.get(data.usertoken.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User token not found")
    return user

@app.post("/get-user-logs")
def get_user_logs(data: UserRequest):
    user = fake_db.get(data.log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User log not found")
    return user

@app.post("/get-user-external-logs")
def get_user_external_logs(data: UserRequest):
    user = fake_db.get(data.log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User external log not found")
    return user

@app.post("/get-user-external-logs-gcp")
def get_user_external_logs_gcp(data: UserRequest):
    user = fake_db.get(data.log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User external GCP log not found")
    return user

@app.post("/get-user-external-logs-aws")
def get_user_external_logs_aws(data: UserRequest):
    user = fake_db.get(data.external_log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User external AWS log not found")
    return user

@app.post("/post-user-external-logs-aws")
def post_get_user_test(data: UserRequest):
    user = fake_db.get(data.external_log.lower())
    if not user:
        raise HTTPException(status_code=404, detail="User external AWS log not found")
    return user

@app.post("/post-data-to-cloud")
def sync_data_to_cloud(data: UserRequest):
    user = fake_db.get(data.cloud_db.lower())
    if not user:
        raise HTTPException(status_code=404, detail="Failed to send data")
    return user