# class A:

#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f'Hello {self.name}!')

# class B(A):

#     def __init__(self):
#         super().__init__(name = '')

#     def greet(self,name):
#         self.name = name
#         super().greet()
#         print('Hi')



# b = B()

# b.greet('sandhya')

#  # i want to ans something like this
#  # Hello sandhya 
#  # Hi



class A:
    a = 10

    def __init__(self):
        self.b = 20

class B(A):
    def m(self):
        print(super().a)
        print(self.)

b = B()
b.m()