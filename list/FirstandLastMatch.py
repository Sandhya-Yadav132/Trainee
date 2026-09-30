lst=[5,2,3,4,6,'5']
def myfun(lst):
    if lst[0]==lst[-1]:
        return True
    return False

print(myfun(lst))