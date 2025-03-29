# Global Scope
my_global=10
def fn1():
    enclosed_v=8

    def fn2():
     local_v=5
     print('Access to Global', my_global)
     print('Access to enclosed',enclosed_v)
    fn2()
fn1()
# print('Cant access local',local_v)--produces error
# print(enclosed_v)--can't be accessed outside fn2()


# LOCAL SCOPE
def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2))

# Accessing variable outside of the function:
# print(total)
# NameError: name 'total' is not defined

# ENCLOSING SCOPE
def get_total1(a, b):
    #enclosed variable declared inside a function
    total1 = a + b

    def double_it():
        #local variable
        double = total1 * 2
        print(double)

    double_it()
    #double variable will not be accessible
    # print(double)

    # return total


# GLOBAL SCOPE
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total2 = a + b
    print(special)

    def double_it():
        #local variable
        double = total2 * 2
        print(special)

    double_it()

    return total
