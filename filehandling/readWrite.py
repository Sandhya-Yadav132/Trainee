file = open("data.txt", "w")
file.write("Python Developer")
file.close()

file = open("data.txt", "r+")

print(file.read(2))
print(file.tell())

# file.write("XYZ")

# file.seek(0)

print(file.read(24))

# print(file.read())

file.close()