# summations: differencea: addition is done between 2 arguments whereas summation happens over n elements.

# Adding 2 array.
import numpy as np
pb1=np.array([1,2,3])
pb2=np.array([1,2,3])
pbnew= np.add(pb1,pb2)
print(pbnew)

# Sum the values in 2 array:-
import numpy as np
pb1=np.array([1,2,3])
pb2=np.array([1,2,3])
pbnew= np.sum([pb1,pb2])
print(pbnew) #give sum of array elements in sinle elements. 12

# summation over on axis if you specify axis=1, numpy will sum the number in each array.
import numpy as np
pb1=np.array([1,2,3])
pb2=np.array([1,2,3])
pbnew= np.sum([pb1,pb2],axis=1)
print(pbnew) #o/p ak array me [6 6]

# cummulative sum - means partially adding the elements array.
# examp:- [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4]
import numpy as np
pb = np.array([1,2,3,4])
pbnew = np.cumsum(pb)
print(pbnew) 