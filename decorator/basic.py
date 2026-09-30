def decorator(func):
    def wrapper():
        print("hello")
        func()
    return wrapper

# greet=decorator(greet)
# @decorator
def greet():
    print("Hello")


g=decorator(greet)
g()
# print(k)