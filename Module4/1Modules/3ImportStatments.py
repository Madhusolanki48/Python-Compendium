import json
import numpy
# import seaborn

import sys
sys.path.insert(1,r'C:\Users\msmad\OneDrive\Desktop\Python\Module1')

# import trial
# print(trial.Module1)

# from math import sqrt  ---error
import math
print('importing the math module')
root=math.sqrt(9)
print(root)


from math import sqrt
root=sqrt(9)
print(root)


import math as m
# cosine=math.cos(0)  ---error cuz the math module is now recognized as m
cosine=m.cos(0)
print(cosine)

from math import factorial as f
factorial_10=f(10)
print(factorial_10)

from math import factorial,log10,sqrt
x=log10(50)
print(x)

from math import *   #import all functions