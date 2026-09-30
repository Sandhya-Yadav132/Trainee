# class Bank:

#     def __init__(self, name):
#         self.name = name
#         self.balance1 = 0
#         self._balance2 = 0
#         self.__balance = 0


#     def details(self):
#         return self.name

# b = Bank('Sandhya')

# print(b.details())
# print(b.balance1)     # public
# print(b._balance2)    #protectd
# # print(b.__balance)    # private dont use like this ,Private properties cannot be accessed directly from outside the class.

# '''
#  but by name mangling we can use it
#  Name mangling is how Python implements private properties and methods.

# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

# For example, __age becomes _Person__age.
# '''

# '''
# The Pythonic Way: Getters, Setters, and @propertyTo achieve safe encapsulation, 
# you provide controlled public methods to read or update private data. 
# The most elegant way to handle this in Python is using the @property decorator, 
# which lets you apply validation rules without forcing users to call clunky get_ and set_ methods
# '''

# print(b._Bank__balance)      # output will be 0

#---------------------------------------------------

class Bank:

    def __init__(self, name, age, balance = 0):
        self._name = name
        self._age = age
        self.__balance = balance

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def balance(self):
        return self.__balance

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
            print(f'Successfully deposited ₹{amount}')
        else:
            print('Amount must be valid')

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be Valid!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew ₹{amount}.")
    

b = Bank('sandhya', 23)

# print(b.name)
# print(b.balance)
b.deposit(1000)
# b.withdraw(500)


        

