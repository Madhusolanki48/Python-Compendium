sample_dict={1:'Coffee', 2:'Tea', 3:'Juice'}
print(sample_dict[1])

# To update a key
sample_dict[2]='Mint Tea'

# sample_dict={1:'Coffee', 2:'Tea', 3:'Juice', 1:'Soda} --error because two keys cannot be present


# To delete a key
del sample_dict[3]

print(sample_dict)


my_d={}
print(type(my_d))
my_d={1:'Test','Name':'Jim'}
print(my_d[1])

for x in my_d:
    print(x)

for key,value in my_d.items():
    print(str(key)+' : '+value)    

