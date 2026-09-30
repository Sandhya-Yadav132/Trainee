# 1. instance methods
# 2. class methods
# 3. static methods

class Methods:

    # def __init__(self):
    #     pass

    def my_method(self):
        print('This is instance method')

    @classmethod
    def my_clasmethod(cls):
        print("This is classmethod")

    @staticmethod
    def my_staticmethod():
        print('This is staticmethod')

m1 = Methods()

m1.my_method()

Methods.my_clasmethod()
m1.my_clasmethod()

Methods.my_staticmethod()
m1.my_staticmethod()