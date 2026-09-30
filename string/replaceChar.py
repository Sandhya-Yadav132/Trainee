# replace char to other char

# s="Hello python! welcome"

# replace starting n char l with j

# print(s.replace('l','j',2))  # All l replaced by j


#--------------------------------------
# n=int(input("Enter no of char : "))
# replaced=[]
# count=0
# for ch in list(s.lower()):
#     if ch=='l' and count<n:
#             count+=1
#             replaced.append('j')
#     else:
#          replaced.append(ch)

    
# print(''.join(replaced))
#----------------------------------------


#-------------------------------------
# s='All string methods return new values. They do not change the original string.'
# newstr=''
# count=0
# n=int(input("Enter no of char you want to replace : "))
# for ch in s:
#     if ch.lower()=='l' and count<n:
#             count+=1
#             newstr+='j'
#     else:
#          newstr+=ch
# print(newstr)

#--------------------------------------

s=input("Enter string : ")

newstr=''
for ch in range(len(s)):
    if ch=='i':
        newstr+='j'
    else:
        newstr+=ch

print(newstr)

