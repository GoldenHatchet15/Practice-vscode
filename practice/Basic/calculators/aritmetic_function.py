class ArithmeticFunctions:
    """ Arithmetic Functions with add and subtract methods. """

    @staticmethod
    def add_func(x, y):
        return x + y

    @staticmethod
    def sub_func(x, y):
        return x - y

    @staticmethod
    def mul_func(x, y):
        return x * y
    
    @staticmethod
    def div_func(x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero is not allowed."