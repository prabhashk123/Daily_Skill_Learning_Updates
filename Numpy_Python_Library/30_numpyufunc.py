# ufunc - stand for universal function and they are actually numpy functions that operates on the ndarray objects.
# usfunc also takes additional arguments like, where, dtype and out
# vectorization - converting the itreative stments into a vector base stmt.

# example without ufunc, here we will use python in built zip().
x = [1,2,3,4]
y = [4,5,6,7]
z = []
# for loop itreation ke sath
for i, j in zip(x,y):
    z.append(i+j)
print(z)

# same with ufunc, we will now use add() function
import numpy as np
x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)
print(z)

