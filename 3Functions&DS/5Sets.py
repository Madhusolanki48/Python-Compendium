#Contains unordered items but does not contain duplicates
set_a={1,2,3,4,5}
print(set_a)

# print(set_a[0]) ---error because set is not a sequence

set_a.add(6)
print(set_a)

set_a.remove(2)
# set_a.discard(2)
print(set_a)

# Some mathematical operations on set
set_b={4,6,8,9,3}

print('Union Operation: ',set_a.union(set_b))

print('Or Operation:',set_a|set_b)

print('Intersection: ',set_a.intersection(set_b))

print('Difference: ',set_a.difference(set_b))
print(set_a-set_b)

print('Symmetrical Difference: ',set_a.symmetric_difference(set_b))
print(set_a^set_b)





