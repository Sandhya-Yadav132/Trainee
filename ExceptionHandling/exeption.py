# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# a=[2,3]
# for i in range(True):
#     print(i)

# a = 5
# b = 0
# l = [1, 2]


# try:
#     c = a / b 
#     print(c)
#     for i in range(len(l)+1):
#         print(l[i])
# except* Exception as e:
#     print(e)
# # except ZeroDivisionError as e:
# #     print(e)
# # except IndexError :
# #     print("indexing out of range")
# finally:
#     print('program ran succesfully')


# import p

# # def func(*args, **kwargs):
# #     return 2*2
# def func(a):
#     return a*a
# # print(func())
# try:
#     output = func()
#     print(output)
# except:
#     output = func(2)
#     print("no params are provided!")
# else:
#     print("else!")
# finally:
#     print("finally")
# print(output)


