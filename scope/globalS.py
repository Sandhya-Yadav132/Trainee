# 1. Global

# x=0
# def outer():
#     def inner():
#         # x=x+1         #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#         x=2             # 2 create local variable
#         print(x)
#     return inner

# s=outer()
# s()

# Also, use the global keyword if you want to make a change to a global variable inside a function.

# x=0
# def outer():
#     def inner():
#         global x
#         x=x+1         
#         print(x)
#     return inner

# s=outer()
# s()

# 2.Nonlocal


def outer():
    x=0
    def inner():
        nonlocal x
        x=x+1         
        print(x)
    return inner

s=outer()
s()


# x=20
# def fumc():
#     global x
#     x=30
#     def inner():
#         nonlocal x
#         x=40
#     inner()
#     print(x)
# fumc()
# print(x)


