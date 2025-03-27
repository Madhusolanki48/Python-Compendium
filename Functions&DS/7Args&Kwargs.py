# def sum_of(a,b):
#   return a+b
def sum_of(*args):
    total = 0
    for x in args:
        total += x
    return total
   

print(sum_of(4,5,6)) #--error because int the above function only two arguments taken i.e. a & b
# so here args works

def sum_of_kwargs(**kwargs):
    total=0
    for k,v in kwargs.items():
        total += v
    return round(total,2)

print(sum_of_kwargs(coffee=2.99,cake=4.55,juice=2.99))
