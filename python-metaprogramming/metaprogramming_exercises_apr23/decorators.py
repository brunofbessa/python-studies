"""Decorator exercises"""
from functools import wraps

def count_calls():
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def jsonify():
    """Decorate function to JSON-encode return value."""


def groot():
    """Return function which prints 'Groot' (ignore decoratee)."""


def four():
    """Return 4 (ignore decorated function)."""


def record_calls():
    """Recording number of times a decorated function is called."""


def positional_only():
    """Specify arguments to a function positionally only."""


def allow_snake():
    """Add camelCase versions of snake_case methods and vice versa on cls."""


def overload():
    """Allow functions to be overloaded based on arguments count and their types."""
