# spliting array in numpy- It is reverse to joining means breaking the array matlab torna.
"""Spliting the 1-D"""
# Split the array in 3 parts
import numpy as np
pb = np.array([1,2,3,4,5,6])
pbnew=np.array_split(pb,3)
print(pbnew)

# Split the array in 4 parts
import numpy as np
pb = np.array([1,2,3,4,5,6])
pbnew=np.array_split(pb,4)
print(pbnew)

# split into array with index
import numpy as np
pb = np.array([1,2,3,4,5,6])
pbnew=np.array_split(pb,3)
print(pbnew[0])
print(pbnew[1])
print(pbnew[2])

"""Spliting the 2-D"""
import numpy as np
pb = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
pbnew=np.array_split(pb,3)
print(pbnew)

# split the 2-D array into 2-D arrays into three 2-D arrays
import numpy as np
pb = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
pbnew=np.array_split(pb,3)
print(pbnew)

# spliting the 2-D into three 2-D along with rows
import numpy as np
pb = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
pbnew=np.array_split(pb,3,axis=1)
print(pbnew)

# alternate solution is using the hsplit(), opposite hstack(),vsplit()
import numpy as np
pb = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
pbnew=np.hsplit(pb,3)
print(pbnew)


