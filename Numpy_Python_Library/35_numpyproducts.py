# products: use prod() function.
# Here we will find the product of the element of the below array:
import numpy as np
pb = np.array([1,2,3,4]) # 1*2*3*4 = 24
pbnew = np.prod(pb)
print(pbnew)

# Here we will find the product of elements in 2 different array:
import numpy as np
pb1 = np.array([1,2,3,4])
pb2 = np.array([5,6,7,8])
pbnew = np.prod([pb1, pb2]) # 1*2*3*4*5*6*7*8 =40320 
print(pbnew)

# Prod over on axis
import numpy as np
pb1 = np.array([1,2,3,4])
pb2 = np.array([5,6,7,8])
pbnew = np.prod([pb1, pb2],axis=1) # 1*2*3*4*5*6*7*8 =40320 
print(pbnew) # single answer in array

# cummulative prod: means partialy product of [1,2,3,4] is [1.1*2,1*2*3,1*2*3*4]=[1,2,6,24] reprensted by cumprod().
import numpy as np 
pb = np.array([5,6,7,8])
pbnew = np.cumprod(pb)
print(pbnew)