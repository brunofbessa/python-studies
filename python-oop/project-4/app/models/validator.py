# Validation class

import numbers

class IntegerField:

    def __init__(self, min_, max_):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.prop_name} must be of type integer.')
        if value < self._min and self._min is not None:
            raise ValueError(f'{self.value} must be greater than or equal to {self._min}.')
        if value > self._max and self._max is not None:
            raise ValueError(f'{self.value} must be less than or equal to {self._min}.')
        else:
            instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
    

class CharField:

    def __init__(self, min_=None, max_=None):
        self._min = min_ or 0
        self._max = max(0, min_)

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.prop_name} must be of type string.')
        if len(value) < self._min and self._min is not None:
            raise ValueError(f'Length of {self.value} must be greater than or equal to {self._min}.')
        if len(value) > self._max and self._max is not None:
            raise ValueError(f'Length of {self.value} must be less than or equal to {self._min}.')
        else:
            instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
    

