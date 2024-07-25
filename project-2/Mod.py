"""
privide an implementation so that int(mon_object) will return its residue
privide a proper representation (repr)
impement the operators +, -, *, **, 
 - support that other operand to be mod (with same modulus only)
 - suppoet other operand to be an integer (and use rhe same modulus)
 - always return a mod instance
  - perform opeations on the value: mod(2, 3) + 16 = mod(2+16, 3) = mod(0, 3)
implement the corresponding in-place atithmetic operators
implement ordering(makes sense since we are comparing residues)
 - support other operand to be a mod (with same modulus, or an integer)

"""

class Mod:

    def __init__(self, value, modulus):
        self._modulus = modulus
        self._value = value % modulus
    
    @property
    def modulus(self):
        return self._modulus
    
    @property
    def value(self): 
        return self._value % self._modulus
    
    @modulus.setter
    def modulus(self, modulus):
        self._modulus = modulus
        return self
    
    @value.setter
    def value(self, value):
        self._value = value

    def _validate_operand(self, other):
        if isinstance(other, int):
            return other % self.modulus
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible operands. ')

    def __int__(self):
        return self.value
    
    def __hash__(self):
        return hash(self.value, self.modulus)

    def __repr__(self):
        return f'Mod({self.value}, {self.modulus})'
    
    def __eq__(self, other):
        other_value = self._validate_operand(other)
        return self.value == other_value

    def __add__(self, other):
        other_value = self._validate_operand(other)
        return Mod(self.value + other_value, self.modulus)
        
    def __iadd__(self, other):
        other_value = self._validate_operand(other)
        self.value = (self.value + other_value) % self.modulus
        return self

    def __sub__(self, other):
        other_value = self._validate_operand(other)
        return Mod(self.value - other_value, self.modulus)

    def __isub__(self, other):
        other_value = self._validate_operand(other)
        self.value = (self.value - other_value) % self.modulus
        return self

    def __mul__(self, other):
        other_value = self._validate_operand(other)
        return Mod(self.value * other_value, self.modulus)
        
    def __imul__(self, other):
        other_value = self._validate_operand(other)
        self.value = (self.value * other_value) % self.modulus
        return self

    def __pow__(self, other):
        other_value = self._validate_operand(other)
        return Mod(self.value ** other_value, self.modulus)
        
    def __ipow__(self, other):
        other_value = self._validate_operand(other)
        self.value = (self.value ** other_value) % self.modulus
        return self
    
    def __lt__(self, other):
        other_value = self._validate_operand(other)
        return self.value < other_value 