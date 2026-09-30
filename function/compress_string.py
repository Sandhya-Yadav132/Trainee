str1="aabcccccaaa"
# output- a2b1c5a3

def compress_string(str1):
    # map={}
    # for ch in str1:
    #     if ch not in map:
    #         map[ch]=1
    #     else:
    #         map[ch]+=1
    # str2=''
    # for k,v in map.items():
    #     str2+=k+str(v)
     
    str2=''
    count=0
    for ch in set(str1):
        count+=1
        str2+=ch+str(count)
    return str2

print(compress_string(str1))