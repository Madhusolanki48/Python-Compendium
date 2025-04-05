class A:
    pass
class B(A):
    pass

# MULTIPLE INHERITANCE
# Example 1
class A:
   a = 1   
class B:
   b = 2   
class C(A, B):
   pass
c = C()
print(c.a, c.b)


# MULTI-LEVEL INHERITANCE
class A:
   a = 1
class B(A):
   a = 2
class C(B):
   pass
c = C()
print(c.a)

# BUILT-IN FUNCTIONS
# 1. issublass() function
# issubclass(class A, class B)
print(issubclass(A,B))
print(issubclass(B,A))

# 2. isinstance() function
class A:
	pass
class B(A):
	pass
b = B()
print(isinstance(b,B))
print(isinstance(b,A))


class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)
class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')
apple = FruitFlavour()

# In the code above, if I had commented out the line for super() function, the output is: 
# Apple is sweet
