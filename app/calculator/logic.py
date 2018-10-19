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
        if (a < self.min_value or a > self.max_value or b < self.min_value or b > self.max_value):
            raise ValueError('One or both of the given numbers are out of bounds.')

        return a * b

    def div(self, a, b):
        if (b == 0):
            raise ValueError('Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn’t make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends.')
        
        return a / b
