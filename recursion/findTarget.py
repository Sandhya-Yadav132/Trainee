#[2,3,5,7,11,13,17,19] prime number

# find the number of pair which is equals to the given target(18)

n=20
target=18

# prime_number=[]
# def IsPrime(n):
#     # breakpoiqnt()
#     for num in range(2,n+1):
#         limit=
#         for i in range(2,limit):
#             if num%i==0:
#                 break
#         else:
#                 prime_number.append(num)
#     return prime_number  
# print(IsPrime(n))


def findTarget(n,target):
     def IsPrime(num):
        if num==0 or num==1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
     prime_number=[i for i in range(n) if IsPrime(i)]
     targetPairs=[]
     for i in range(len(prime_number)):
         for j in range(i+1,len(prime_number)):
             if prime_number[i]+prime_number[j]==target:
                 targetPairs.append([prime_number[i],prime_number[j]])   
    
     return targetPairs


print(findTarget(n,target))