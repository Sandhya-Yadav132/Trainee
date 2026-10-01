import numpy as np
import random

rows = 3
cols = 9

# arr = np.random.randint(0, 10, size =(r, c)) 
# print(arr)

# matrix = [i for i in range(c) for _ in range(r)]

# for _ in range(r):
#     for i in range(c):
#         print(i, end = ' ')
#     print()

l = 1
h = 9

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

con = 0 



for col in range(cols):
    for row in range(rows):
         matrix[row][col] = random.randint(l, h)
            
    l = h + 1
    h = l + 9

# breakpoint()
for _ in range(cols):
    if con <= cols - 5:
        for _ in range(rows):
         
            col1 = random.randrange(cols)
            row1 = random.randrange(rows)
            print(col1,row1)
            matrix[row1][col1] = 0
        con+=1
          
for row in matrix:
      print(row)


# print(matrix)

# print(type(None))
# print(type(int))