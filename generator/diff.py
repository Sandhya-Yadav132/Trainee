def gen(a):
    yield a
    print(a)

for i in range(5):
    print(next(gen(i)))

# print(a)