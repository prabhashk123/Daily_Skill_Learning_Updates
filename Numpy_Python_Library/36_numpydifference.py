# difference :- use diff() function for finding the difference.
# example: [1,2,3,4], the deiscreate difference of this would be [2-1, 3-2, 4-3] = [1,1,1] by using diff()
# apas me two digits ka diiference next-previous 
import numpy as np
pb = np.array([10,15,25,5])
pbnew= np.diff(pb)
print(pbnew)

