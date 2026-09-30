lst=[1,2,3,4,5,6,7,8,9,10]

# for i in range(len(lst)):
#    lst.remove(lst[i])   # list index out of range
# i=0

# while len(lst)!=1:
#     if lst[i] in lst:
#         print(lst[i],lst)
#         lst.remove(lst[i+1])


# curr=1
# while len(lst)!=1:
#     for i in lst[curr::2]:
#         # print(i)
#         print('elm:',i,'index:',lst.index(i),'curr:',curr)
#         lst.remove(i)
#         # curr=i
#         # print(lst)
# print(lst)

lst=list(range(1,101))
pos=0
while len(lst)>1:
        pos=(pos+1)%len(lst)
        removed=lst.pop(pos)
        # print('removed :',removed,'list',lst)
print(lst)