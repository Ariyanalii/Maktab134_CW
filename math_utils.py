

class MathUtils:

    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot Divide By Zero.")
        return a / b
    
    def is_even(self, n):

        if n == 0:
            raise ZeroDivisionError("Cannot Divide By Zero.")

        return n % 2 == 0


