'''
Python does not support true compile-time polymorphism because method calls are resolved at runtime.
However, similar behavior can be achieved using default arguments, variable-length arguments (*args),
or keyword arguments (**kwargs).
'''

class Calculator:

    def multiply(self, a = 1, b = 1, *args):
        result = a * b
        for i in args:
            result*=i
        return result

clc = Calculator()

print(clc.multiply())
print(clc.multiply(4))
print(clc.multiply(4,5))
