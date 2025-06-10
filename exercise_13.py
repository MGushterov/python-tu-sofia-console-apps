class Calculator:
    def __init__(self):
        pass

    def perform_operation(self, operation, a, b):
        if operation == "add":
            return self.__add(a, b)
        elif operation == "subtract":
            return self.__subtract(a, b)
        elif operation == "multiply":
            return self.__multiply(a, b)
        elif operation == "divide":
            return self.__divide(a, b)
        else:
            print("Invalid operation")

    def __add(self, a, b):
        return a + b

    def __subtract(self, a, b):
        return a - b

    def __multiply(self, a, b):
        return a * b

    def __divide(self, a, b):
        return a / b

calc = Calculator()
print(calc.perform_operation("add", 10, 20))