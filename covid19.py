lst=[1,2,3,4,5,6,7]
# output [1,4,6,3,5,7]
newlst=[0]*len(lst)
l=0
r=len(lst)-1
newlst[0]=lst[0]
newlst[-1]=lst[1]
# count=0
for i in range(2,len(lst)):
    if newlst[i]==0:
        # breakpoint()
        # dis=r-l-1
        mid=l+(r-l)//2
        newlst[mid]=lst[i]
        if (mid-l)>=(r-mid):
            r=mid
        else:
            l=mid
        # count+=1
        # if count==3:
        #     break
print(newlst)