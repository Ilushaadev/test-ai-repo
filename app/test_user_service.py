# test_user_service.py

import pytest
from app.user_service import get_user_profile_summary, is_user_admin


def test_valid_user_summary():
    """Valid user dict input ."""
    user = {
        "first_name": "Alice",
        "last_name": "Test",
        "email": "alice@example.com",
        "role": "admin",
        "is_active": True
    }
    summary = get_user_profile_summary(user)
    print(f'this is a summary print: {summary}')
    assert summary == "Alice Test (alice@example.com) - admin [active]"


def test_non_dict_input_raises():
    """Non-dict input raises TypeError. """
    with pytest.raises(TypeError):
        get_user_profile_summary("notadict")


def test_nothing():
    """
    this is a test
    """
    return "Hello"

def new_func():
    print("new func")

def test_is_user_admin_returns_true_for_admin_and_active():
    user = {"role": "admin", "is_active": True}
    assert is_user_admin(user) is True

def test_is_user_admin_returns_false_for_admin_but_inactive():
    user = {"role": "admin", "is_active": False}
    assert is_user_admin(user) is False

def test_is_user_admin_returns_false_for_non_admin_but_active():
    user = {"role": "user", "is_active": True}
    assert is_user_admin(user) is False

def test_is_user_admin_returns_false_for_missing_role():
    user = {"is_active": True}
    assert is_user_admin(user) is False

def test_is_user_admin_returns_false_for_missing_is_active():
    user = {"role": "admin"}
    assert is_user_admin(user) is False

def test_is_user_admin_returns_false_for_empty_user():
    user = {}
    assert is_user_admin(user) is False