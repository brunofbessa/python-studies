import itertools
import numbers
from TimeZone import TimeZone

class Account:

    transaction_counter = itertools.count(100)
    _interest_rate = 0.5
    _transaction_codes = {
        'deposit': 'D', 
        'withdraw': 'W', 
        'interest': 'I', 
        'rejected': 'R'
    }

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone
        
        self._balance = Account.validate_real_number(initial_balance, min_value=0)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name
 
    @first_name.setter
    def first_name(self, value):
        #value = Account.validate_name(value, 'first_name')
        #self._first_name = value
        self.validate_and_set_name('_first_name', value, 'first_name')

    @property
    def last_name(self):
        return self._last_name
 
    @last_name.setter
    def last_name(self, value):
        #value = Account.validate_name(value, 'last_name')
        #self._last_name = value
        self.validate_and_set_name('_last_name', value, 'last_name')

    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def validate_name(value, field_title):
         if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'Field {field_title} cannot be empty')
         return str(value).strip()    
    
    def validate_and_set_name(self, property_name, value, field_title):
         if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'Field {field_title} cannot be empty')
         setattr(self, property_name, value) 

    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}.')
        
        return value

    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time Zine must be a valid TimeZone object.')
        self._timezone = value

    @property
    def balance(self):
        return self._balance
    
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    
    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number.')
        if value < 0:
            raise ValueError('Interest rate must be postive.')
        
        cls._interest_rate = value

    def generate_confirmation_code(self, transaction_code):
        datetime_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self.account_number}-{datetime_str}-{next(Account.transaction_counter)}'

    def deposit(self, value): 
        value = Account.validate_real_number(value, 0.01)

        transaction_code = Account._transaction_codes['deposit']
        conf_code = self.generate_confirmation_code(transaction_code)
        self._balance += value

        return conf_code
    
    def withdraw(self, value):
        value = Account.validate_real_number(value, 0.01)
        
        # To make sure funds are changed only if transaction is fully done, 
        # check twice and generate confirmation code once, then deduce value from 
        # account balance

        accepted = False
        if self.balance < value:
            transaction_code = Account ._transaction_codes['rejected'] 
        else:       
            accepted = True
            transaction_code = Account ._transaction_codes['withdraw']          

        conf_code = self.generate_confirmation_code(transaction_code)
        if accepted == True:
            self._balance -= value

        return conf_code

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])

        self._balance += interest

        return conf_code
