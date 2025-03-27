list1=[1,2,3,4,5]
print(list1[2])

list2=['A','B','C']
list3=['Hello',1,True,40.22]
list4=[1,[2,3,4],5,6]

print(*list1)
print([list1],sep=' ')

list1.insert(len(list1),6)
print([list1],sep=' ')

list1.append(6)

list1.extend([6,7,8,9])

list1.pop(4)

del list1[2]

# To iterate
for x in list1:
    print('Value: ',x)
