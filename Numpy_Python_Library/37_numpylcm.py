# L.C.M(Lowest common multiple):- here we will find the LCM of 2 number:-
import numpy as np
pb1 = 4
pb2 = 6
pbnew= np.lcm(pb1,pb2)
print(pbnew) 
# ans of the above is 12 because lcm of 4 and 6 is 12.

# Finding the lcm of array:-
import numpy as np
pb = np.array([3,6,9])
pbnew = np.lcm.reduce(pb)
# the reduce() method will use the ufunc, in this case the lcm() function on each element and it will reduce array by 1 diemension.
print(pbnew)

# here we will find the LCM of all of an array where the array contains all integers from 1 to 10.
pb = np.arange(1,11)
pbnew = np.lcm.reduce(pb)
print(pbnew)