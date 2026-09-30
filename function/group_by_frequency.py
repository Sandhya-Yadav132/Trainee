l=[4, 4, 5, 6, 6, 6, 7, 7, 7, 7,8,8]
# output -{2: [4,8], 1: [5], 3: [6], 4: [7]}

def group_by_frequency(l):
    map={}
    for i in l:
        if i not in map:
            map[i]=1
        else:
            map[i]+=1
    group={}
    for k,v in map.items():
        if v not in group:
            group[v] = [k]  # Agar frequency pehle nahi dekhi, toh nayi list banayein
        else:
            group[v].append(k)  # Agar frequency pehle se hai, toh usme append karein
    return group

print(group_by_frequency(l))