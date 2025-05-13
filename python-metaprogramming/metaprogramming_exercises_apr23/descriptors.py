"""Descriptor exercises"""
from random import randint

class RandomNumber():
    """Descriptor that generates a random number when accessed."""

    def __init__(self, a, b=None):
        if b is None:
            self.a = 0
            self.b = a
        self.a = a
        self.b = b
    
    def __get__(self, instance, owner_class=None):
        # if instance is None:
        #     return self
        return randint(self.a, self.b)
        


class alias:
    """Descriptor that proxies one attribute to another."""


class class_property:
    """Property that works on the class."""


class class_only_method:
    """A method that can only be called at the class-level."""


class computed_property:
    """A property which is re-computed only when another attribute changes."""
