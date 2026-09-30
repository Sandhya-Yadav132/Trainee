# Rotate a List
# Given a list and an integer k, rotate the list to the right by k places. (Example: [1, 2, 3, 4, 5] rotated by 2 becomes [4, 5, 1, 2, 3])

lst=[1,2,3,4,5]

def rotate(lst,k):
    #  k=k%len(lst)
     result=[None]*len(lst)
     for i in range(len(lst)):
          indx=(i+k)%len(lst)
          result[indx]=lst[i]
     return result
       
        
        

print(rotate(lst,2))
