# encoding=utf-8


class ValueTooLowException(Exception):
    pass


class ValueTooHighException(Exception):
    pass


class Calculator(object):
    def __init__(self, min_value=-1000, max_value=1000):
        self.min_value = min_value
        self.max_value = max_value

    def mul(self, a, b):
        if (a < min_value || a > max_value || b < min_value || b > max_value)
            raise Exception('One or both of the given numbers are out of bounds.')

        return a * b

    def div(self, a, b):
        pass
