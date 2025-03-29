'''Syntax Errors-caused by human errors
Exception- known errors need to be handled
'''

# Error type=Syntax error
greeting='hello'
# if greeting=='hello'   -- missing colon
print('Hello, How are you ?')

# Indentation error

# Exceptions
# a=5/0
# ZeroDivionError :division by zero


# IndexError
# Starter code
items = [1,2,3,4,5]
item = items[6]
print(item)

# ZeroDivisionError
# Starter code
def divide_by(a, b):
    return a / b
ans = divide_by(40, 0)
print(ans)

# FileNotFoundError
# Starter code
with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())





