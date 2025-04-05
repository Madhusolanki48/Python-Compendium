# Create a class, instantiate it, & access its variables & methods
class MyClass:
    a=5
    print('Hello')

    def hello(self):
        print('Hello, World !')

myClass=MyClass()
print(MyClass.a)
print(myClass.a)
print(myClass.hello())   #Print none also, as there is no return value