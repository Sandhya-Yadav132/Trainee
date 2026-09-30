# s="python"

#with built in function sorted() and ascii value
#1. print(sorted(s))


#2. ascii value
# ascii=list(s.encode('ascii'))

# for i in range(len(ascii)):
#     for j in range (i+1,len(ascii)):
#         if ascii[i]>ascii[j]:
#             ascii[i],ascii[j]=ascii[j],ascii[i]

# sorted_string=bytes(ascii).decode('ascii')  # sorted string
# print(sorted_string) #hnopty

# print(list(sorted_string))  #['h', 'n', 'o', 'p', 't', 'y']

#Without built in function or module

s='Python'

arrange=[]

# for ch in s.lower():
#     arrange.append(ch)

arrange = list(s.lower())

for i in range(len(arrange)):
    for j in range(i+1,len(arrange)):
        if arrange[i] > arrange[j]:
            arrange[i],arrange[j]=arrange[j],arrange[i]

print(arrange)


# a='a'
# b='b'
# print(a>b)