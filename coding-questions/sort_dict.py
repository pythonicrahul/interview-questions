dict1 = {575: "A", 876: "Mango", 132: "Grapes", 782: "Banana"}


d = sorted(dict1.keys())
dict2= {}
for i in d:
    dict2[i] = dict1[i]

print(dict2)

