from collections import defaultdict
d = defaultdict()
# d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d.__missing__('x'))
print(d.__missing__('d'))

# Normal access to existing key
print(d['a'])