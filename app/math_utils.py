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

def analyze_word_lengths(words):
    """
    Given a list of strings, returns statistics about word lengths:
    - total_words
    - shortest_word
    - longest_word
    - average_length
    - all_uppercase (True if all words are uppercase)
    """
    if not isinstance(words, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(w, str) for w in words):
        raise ValueError("All items must be strings")

    if not words:
        return {
            "total_words": 0,
            "shortest_word": "",
            "longest_word": "",
            "average_length": 0,
            "all_uppercase": False
        }

    total = len(words)
    shortest = min(words, key=len)
    longest = max(words, key=len)
    average = sum(len(w) for w in words) / total
    all_upper = all(w.isupper() for w in words)

    return {
        "total_words": total,
        "shortest_word": shortest,
        "longest_word": longest,
        "average_length": average,
        "all_uppercase": all_upper
    }

def analyze_character_frequencies(text):
    """
    Given a string, returns statistics about character usage:
    - total_chars
    - unique_chars
    - most_common_char
    - least_common_char
    - is_all_alpha (True if all characters are alphabetic)
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text:
        return {
            "total_chars": 0,
            "unique_chars": 0,
            "most_common_char": "",
            "least_common_char": "",
            "is_all_alpha": False
        }

    from collections import Counter

    counter = Counter(text)
    total = sum(counter.values())
    unique = len(counter)
    most_common = counter.most_common(1)[0][0]
    least_common = min(counter.items(), key=lambda x: x[1])[0]
    all_alpha = text.isalpha()

    return {
        "total_chars": total,
        "unique_chars": unique,
        "most_common_char": most_common,
        "least_common_char": least_common,
        "is_all_alpha": all_alpha
    }


def analyze_word_lengths_test(words):
    """
    Given a list of strings, returns statistics about word lengths:
    - total_words
    - shortest_word
    - longest_word
    - average_length
    - all_uppercase (True if all words are uppercase)
    """
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    else:
        return "Test"

def test():
    return print("hello")