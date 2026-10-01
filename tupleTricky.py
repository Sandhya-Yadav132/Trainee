a=(10,(20,30,10),40,(50,60,10),(10,20,10))
# output- (80,110)

def func(l):
    t=[]
    
    for i in l:
        if isinstance(i,tuple):
            t.append(i)

    t1=[sum(g) for g in zip(*t)]
    return tuple(t1)

print(func(a))