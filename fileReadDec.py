# import os

# def outer(func):

#     def inner(a):
#         if os.path.getsize(a)==0:
#             return "Empty File"
#         return func(a)
#     return inner


# @outer
# def main_func(a):
#     with open(a,'r') as file:
#         data=file.read()
#         return data

# file='demo.txt'
# print(main_func(file))




# from datetime import datetime

# breakpoint()
# datetime.now()


# print(datetime.datetime.__dir__())


# def func(a):

#     if len(a)==0:     # it check the len of a which is demo.txt not the length of data 
#         print('hi')
#         return "Empty"
#     with open(a,'r') as file:
#         return file.read()

# print(func("demo.txt"))




def func(a):

    with open(a,'r') as file:
         c = file.read()
    if len(c)==0:
        return "Empty"

    return c
    

print(func("demo.txt"))


# print(len('demo.txt'))