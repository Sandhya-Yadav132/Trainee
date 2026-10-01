# input =  [[1, 2,[10,12,],0,], [[13,14,15,[7,77,[90,50]]],3, 4], [5, 6]]
# output = [1, 2, 10, 12, 0, 13, 14, 15, 7, 77, 90, 50, 3, 4, 5, 6]

l=[[1, 2,[10,12,],0,], [[13,14,15,[7,77,[90,50]]],3, 4], [5, 6]]


def arrange(l):
    result=[]
    for ele in l:
        if isinstance(ele,list):
            result.extend(arrange(ele))
        else:
            result.append(ele)
    return result

print(arrange(l))


# def arrange(l):
#     result=[]
#     for ele in l:
#         # breakpoint()
#         if type(ele)==list:
#             result.extend(arrange(ele))
#         else:
#             result.append(ele)
#     return result

# print(arrange(l))

