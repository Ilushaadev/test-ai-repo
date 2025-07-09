from app.math_utils import add, multiply

def test_add():
    assert add(2, 3) == 5

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

@app.post("/get-user-password")
def get_user_math_data(data: UserRequest):
    user = fake_db.get(data.username.lower())
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user