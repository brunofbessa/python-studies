"""Metaclass exercises"""


class UnsubclassableType:
    """Metaclass to make classes that cannot be subclassed."""
    # overwrite __new__ method

class InstanceTracker:
    """Metaclass to make iterating over a class iterate through instances."""
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._instances = []

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls._instances.append(instance)
        return instance
    
    def __iter__(cls):
        yeld from cls._instances


class Mapping:
    """Class that acts as a superclass of all mappings."""


class Hashable:
    """Class that acts as a superclass of hashable objects."""


class NoMethodCollisions:
    """Class which disallows class attributes to be redefined."""


class SnakeTestCase:
    """Like unittest.TestCase, but with support for snake_case methods."""
