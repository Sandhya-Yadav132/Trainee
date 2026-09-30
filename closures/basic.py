# def outer_function(x):
#     # Outer function: takes 'x' and defines inner_function
#     def inner_function(y):
#         return x + y  # 'x' is remembered from outer_function
#     return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
# closure = outer_function(10)

# Call the closure with different values of 'y'
# print(closure(5)) 
# print(closure(20))

# print(outer_function(10)(5))
# print(outer_function(10)(20))


#-----------------------------------------------------

# def make_counter():
#     count = 0  # This variable will be remembered
#     def counter():
#         nonlocal count  # Modify outer variable
#         count += 1
#         return count
#     return counter

# counter1 = make_counter()
# print(counter1())  # 1
# print(counter1())


#---------------------------------------------

# def make_multiplier(factor):
#     y=factor
#     def multiply_by(x):
#         return x * y
#     return multiply_by

# double = make_multiplier(2)
# print(double(5)) 
# double = make_multiplier(4)
# print(double(2))

# Check closure variables
# print(double.__closure__[0].cell_contents)