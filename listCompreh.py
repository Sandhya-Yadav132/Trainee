numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Using one list comprehension:

# If the number is even and divisible by 4 → calculate its square
# If the number is odd and divisible by 3 → calculate its cube
# If the number is greater than 15 and divisible by 5 → calculate its double
# Ignore all other numbers.

# Write only one list comprehension.
import pdb;
pdb.set_trace()
n = [ (i ** 2) if  (i % 2 == 0 and i % 4 == 0) else (i ** 3) if (i % 2 == 1 and i % 3 == 0) else (i * 2) if (i > 15 and i % 5 == 0) else i for i in numbers]

# n =[]
# for i in numbers:
#     if i % 2 == 0 and i % 4 == 0:
#         n.append(i ** 2)
#     elif i % 2 == 1 and i % 3 == 0:
#         n.append(i ** 3)
#     elif i > 15 and i % 5 == 0:
#         n.append(i*2)
#     else:
#         continue

print(n)