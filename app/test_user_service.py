# test_user_service.py

import pytest
from app.user_service import get_user_profile_summary

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
    return "Hello"