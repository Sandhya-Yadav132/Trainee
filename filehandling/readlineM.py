# with open('demo.txt') as f:
#     print(f.read())
# import os

# with open('demo.txt') as f:
    # print(f.readline())
    # print(f.readline()r
    # for ch in f.readline():
    #     print(ch)
    # for lines in f:
    #     print(lines)

file = open("data.txt", "r")

print(file.readline())
print(file.readline())

data = file.read()
print(data)

file.close()