#second element access

# tup=((1,2),(3,4),(5,6))

# for ele  in tup:
#     print(ele[0]) 

# for first,second in tup:
#     print(first)


#Find the Index: Write a custom loop to find the index of a specific target value inside a tuple without using .index()

tup1=(2,3,1,4,5)

def findIndx(tup1,ele):
    for i in range(len(tup1)):
        if tup1[i]==ele:
            return i
    return -1

print(findIndx(tup1,6))

