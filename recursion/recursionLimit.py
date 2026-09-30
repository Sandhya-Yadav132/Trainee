# By default, Python enforces a maximum recursion depth limit of 1,000.

'''Aapne bilkul sahi notice kiya! Agar limit 1000 set hai, 
toh code lagbhag 990, 995 ya 998 par hi ruk jata hai, pure 1000 tak nahi pahunchta.'''

import sys

def check_depth(current_depth):
    try:
        check_depth(current_depth + 1)
    except RecursionError:
        # Jab error aayega, tab actual loop count print hoga
        print(f"Actual frames executed: {current_depth}")

print(f"System Recursion Limit: {sys.getrecursionlimit()}")
check_depth(1)
