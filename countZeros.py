
# count zeros without built in or if ,(i==0) also a if condition

l=[1,0,2,4,0,5,7,0,4,5,0,0]

count=0
for i in l:
    breakpoint()
    count+= not i   # not bool(i) /not i
print(count)

# for i in l:
#     breakpoint()
#     while i:
#         break
#     else:
#         count+=1
# print(count)
