list1 = [12,13,14]
print(list1)

list1.append(15)
print(list1)

list2 = list1 + [16]

list3 = list1 + list2
print(list3)

n = 15
ownership = n in list3
print(ownership)

print(list3)

del list3[0]
print(list3)

list3.remove(16)
print(list3)