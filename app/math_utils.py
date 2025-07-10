


class userData():
    user_age: int
    user_agree: bool
    log_out: bool


def test_add():
    assert (2, 3) == 5

def test_multiply():
    assert multiply(4, 5) == 20


def calculate_statistics(numbers):
    """
    Given a list of numbers, returns a dictionary with:
    - count
    - average
    - min
    - max
    - is_all_positive
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All items must be numeric")

    count = len(numbers)
    avg = sum(numbers) / count
    min_val = min(numbers)
    max_val = max(numbers)
    all_positive = all(n > 0 for n in numbers)

    return {
        "count": count,
        "average": avg,
        "min": min_val,
        "max": max_val,
        "is_all_positive": all_positive
    }

def calculate_somthing():
    return print("test")

def calculate_somthing4():
    return print("test41")

def calculate_somthing12222():
    return print("test2")

def calculates_somthing12():
    return print("test2")

def calculates_somthing15():
    return print("test2")


def is_valid_age(age):
    return age >= 18

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def greet_user(name):
    return f"Hello, {name.capitalize()}!"

def should_grant_access(user_type, is_admin):
    return user_type == "premium" or is_admin

def send_error_msg_to_user():
    raise Exp("User not allowed")

def calculate_user_age():
    if userData.user_age < 18:
        send_error_msg_to_user()

def send_user_welcome_msg():
    return print("Welcome User")

def send_user_goodbye_msg():
    return print("Good Bye User")

def calculate_user_agreement():
    if userData.user_agree == "True":
        send_user_welcome_msg()

def logout_user_prompt_message():
    if userData.log_out == "log_out":
        send_user_goodbye_msg()

def error_msg_user():
    if userData.log_out == "Error":
        raise Exp(f"Error displayed{userData.log_out}")

@app.post("/get-user-password")
def get_user_math_data(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


@app.post("/get-users-data")
def get_data_of_user(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.post("/get-users-age")
def get_data_of_user(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User age not found")
    return user

@app.post("/post-users-data")
def post_user_data_to_aws_log(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User data not found")
    return user


@app.post("/post-users-data-to-gcp-db")
def put_user_logs_to_gcp_data(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User data not found")
    return user

@app.post("/get-users-data-gcp")
def get_user_logs_cloud(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User data not found")
    return user

