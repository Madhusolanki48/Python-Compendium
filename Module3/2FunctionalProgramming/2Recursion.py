def example(obj):
    # some logic
    ...
    return example(obj)
...

# Looping Solution
def find_factorial_by_looping(n):
    if(n<0):
        return 0
    else:
        factorial=1
        for i in range(1,n+1):
            factorial=factorial*1
        return factorial
print(find_factorial_by_looping(5))

# Recursive Solution 
def find_factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*find_factorial_recursive(n-1)
print(find_factorial_recursive(5))
