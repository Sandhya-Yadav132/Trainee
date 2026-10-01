import random

# # for i in range(random.choice(10)):
# #     print(i)


# seq1=['sandhya','prachi','vaishnavi','payal','tulja','chuchu']

# print(random.choice(seq1))

import time 

# print('Hi')
# s=time.sleep(2)
# print('Hello')
# print(s)

# print("Welcome Player in Hagman Game!")


import os
import time

print("This entire screen will clear in 10 seconds...")

# Wait for 10 seconds
time.sleep(10)

# Clear the screen (works on Windows, Mac, and Linux)
os.system('cls' if os.name == 'nt' else 'clear')

print("Screen cleared!")


# import os
# import subprocess
# import time

# # print("This entire screen will clear in 10 seconds...")
# print("Welcome Player in Hagman Game!")

# # Wait for 10 seconds
# time.sleep(5)

# # The new, safer method to clear the screen (works on Windows, Mac, and Linux)
# command = 'cls' if os.name == 'nt' else 'clear'
# subprocess.run(command, shell=True)

# # print("Screen cleared!")

# seq1=['sandhya','prachi','vaishnavi','payal','tulja','chuchu']

# print(seq1)

# res = True

# while res:

#     print("Choose a word from the list:")
#     choose = input()
#     c = random.choice(seq1)
#     if choose.lower() == c:
#         print('You Win!')
#     else:
#         print('You Lose!')

#     ans = input('If you want to continue?[y/n] : ')
#     if ans.lower()=='y':
#         res = True
#     else:
#         res = False
# print(f"Thank You Correct answer is {c}")

# # print(random.choice(seq1))
