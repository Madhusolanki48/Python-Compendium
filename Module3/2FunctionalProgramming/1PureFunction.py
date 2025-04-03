# Pure functions are used in functional programming to assure the integrity of data outside the scope of the pure function. 
# global scope
global_list=[1,2,3]
def add_to(item):
    return global_list.append(item)
add_to(4)
print(global_list)

# to change it in pure function we need to extend the func to accept list as argument,add the item to the list without modifying the original list
# and how to return a new list with the newly added item

# solution: create a new list, copy or clone the data from the original list

def add_to_list(lst,item):
    n1=lst.copy()
    n1.append(item)
    return n1

# my_list=[1,2,3]
# def add_to_list1(item):
#     my_list.append(item)
#     return my_list
#     return my_list.append(item)
# # add_to_list1(4)
# # print(my_list)

# new_list=add_to_list1(4)
# print(my_list)
# print(new_list)

# NOT A PURE FUNCTION
my_list=[1,2,3]
def add_to_list1(lst1,item):
    nl=lst1.copy()
    nl.append(item)
    return nl
new_list=add_to_list1(my_list,4)
print(my_list)
print(new_list)

    

