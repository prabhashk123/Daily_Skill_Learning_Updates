# Create your own ufunc, you have to define a function, like you do in normal function in python, then you add it to the numpy function in python, then you add it to the numpy function with "frompyfunc()" method.

# arguments of frompyfunc(): function, inputs, outputs

# Create your own ufunc for addition:-
import numpy as np
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd, 2, 1) #here 2 is 2- diemension of array and value in one 1 array
print(myadd([1,2,3,4],[5,6,7,8]))

# checking if this function in ufunc or not: khud ka func or ye error nhi deta
import numpy as np
print(type(np.add))

# concatenate() func use numpy or python inbuilt me
import numpy as np
print(type(np.concatenate))

# what if ufunc does not exist: usfunc error nhi deta
"""
import numpy as np
print(type(np.sjafhadk))
"""

# use an if statement to check if the functions is a ufunc or not?
import numpy as np
if type(np.add)==np.ufunc:
    print("yes, this function is an ufun")
else:
    print("this function is not an ufun")