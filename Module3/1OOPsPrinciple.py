# ENCAPSULATION
# The idea of encapsulation is to have methods and variables within the bounds of a given unit.

class Alpha:
    
    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’

# POLYMORPHISM
# Polymorphism refers to something that can have many forms. In this case, a given object. 
string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)

# Here, '*' operator exhibits polymorphism

string = "poly"
sequence = [1,2,3]
print(len(string))
print(len(sequence))

# Here, 'len()' function is polymorphic.

# INHERITANCE

# class Parent:
#     Members of the parent class

# class Child(Parent):
#     Inherited members from parent class
#     Additional members of the child class

# ABSTRACTION
# Abstraction can be seen both as a means for 
# hiding important information as well as unnecessary information in a block of code

# from abc import ABC,   
# class ClassName(ABC):
#     pass

