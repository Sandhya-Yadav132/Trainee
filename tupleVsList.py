import sys 
# l=[1,2,3,4,5]
# t=(1,2,3,4,5)

# print('List :',sys.getsizeof(l))
# print('Tuple :',sys.getsizeof(t))


l=[]
t=()


for i in range(38):
    l.append(i)
    t+=(i,)

    print(
        i+1,
        'List :',sys.getsizeof(l),
        'Tuple :',sys.getsizeof(t)
    )