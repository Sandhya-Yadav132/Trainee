l=['cow','you','this','do','cat','they','my']
# o/p= {3: ['cow', 'you', 'cat'], 4: ['this', 'they'], 2: ['do', 'my']}

def group_by_wordLen(l):
    map={}
    for i in l:
        if i not in map:
            map[i]=len(i)
        else:
            map[i]+=len(i)

    # return map
    group={}
    for k,v in map.items():
        if v not in group:
            group[v]=[k]
        else:
            group[v].append(k)

    return group
print(group_by_wordLen(l))

