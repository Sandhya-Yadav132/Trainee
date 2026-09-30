
def makeUsername(username):
    n=username.split()
    return f'fname: {n[0]} lname: {n[1]}'

print(makeUsername('sandhya yadav'))