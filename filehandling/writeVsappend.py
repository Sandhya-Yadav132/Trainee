file = open("data.txt", "w")
file.write("Python Developer")
file.close()

file = open("data.txt", "a")
file.write("\nDjango")
file.close()

file = open("data.txt", "r")
print(file.read())
file.close()