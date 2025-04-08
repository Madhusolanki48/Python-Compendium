''' Namespaces & Scopes in Python
- Namespace: A mapping from names to objects (like a dictionary).
Each module is a namespace containing names of variables, functions, etc.
- Scope: The region of code where a namespace is directly accessible.

Types of Scopes (LEGB Rule):
*Local (L) - Inside the current function
*Enclosed (E) - In enclosing (outer) functions (nested functions)
*Global (G) - At the top-level of a script/module
*Built-in (B) - Python's built-in names (e.g., len, range)

- Scope Resolution:
Python searches for variables using the LEGB rule in order.
Use id() to observe different identities (memory locations) of same-named variables in different scopes.

- Variable Behavior:
Variables are implicitly local unless declared global or nonlocal.
Global variables can be accessed using the global keyword.
Nested functions use nonlocal to refer to enclosing function variables.

- Best Practices:
Avoid using too many global variables (leads to messy "spaghetti code").

Use locals() and globals() to inspect current scopes.

Use nonlocal to modify outer function variables in nested functions.


'''


# Local & Global Scope
country ='USA'                      #-----Global scope
print('Country name: '+country)     
print(globals())                    #-----Globals built-in function
print('----------------------')
def b():
    country='Germany'               #-----Local scope
    print('Country name: '+country)
    print(locals())                 #Locals built-in function

b()
print('Country name: '+country)

def d():
    animal='element'
    def e():
        nonlocal animal
        animal='Giraffe'
        print('Inside nested functions: '+animal)
    print('Before calling function: '+animal)
    e()
    print('After nested function: '+animal)

animal='Camel'
d()
print('Global animal: '+animal)
