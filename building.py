# lst=[1,2,1,2,3,2,3,3,4]
lst=[4,3,3,2,3,2,1,2,1]
# lst=[4,5,3,2,1,5,3,1,3]
# lst=[2,3,5,3,2,1]
# lst=[2,2,2,2,2,2]

def build(lst):
    newlst=[]
    curr=lst[-1]
    for i in range(len(lst)-1,-1,-1):
        breakpoint()
        if curr<=lst[i]:
            curr=lst[i]
    #         newlst.append(lst[i])
    # return list(reversed(newlst))
            newlst.insert(0,lst[i])
    return newlst

# print(build(lst))
# print(lst)


def build1(lst):
    lst.reverse()
    newlst=[]
    curr=lst[0]

    for i in range(len(lst)):
        if curr<=lst[i]:
            curr=lst[i]
            newlst.insert(0,lst[i])
    return newlst
print(build1(lst))