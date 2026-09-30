class A:
    ''' This is a normal funtion'''

    name = 'sandhya'
    age = 22

    def a(self):
        add = "kgn"

# print(globals())

obj = A()

print(obj.a)
print(A.a)
print(A.__dict__)

# print(locals())

# print(len('python'))