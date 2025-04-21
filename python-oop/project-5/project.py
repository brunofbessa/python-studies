import enum

class GenericException(Exception):
    pass

class Timeout(Exception):
    pass

@enum.unique
class AppException(enum.Enum):
    Generic = 100, GenericException, 'Application generic exception.'
    Timeout = 101, Timeout, 'Timeout error.'
    NotAnInteger = 200, ValueError, 'Value must be an integer.'
    NotAList = 201, ValueError, 'Value must be a list.'


    def __new__(cls, ex_code, ex_class, ex_message):
        member = object.__new__(cls)

        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message

        return member
    
    @property
    def code(self):
        return self.value
    
    def throw(self, message=None):
        message = message or self.message
        raise self.exception(f'{self.code} - {message}')
    
if __name__ == '__main__':
    
    try:
        AppException.NotAnInteger.throw()
    except Exception as ex:
        print(ex)

    try:
        AppException.NotAnInteger.throw('test error message.')
    except Exception as ex:
        print(ex)

    try:
        AppException.NotAList.throw('This is not a list!')
    except Exception as ex:
        print(ex)