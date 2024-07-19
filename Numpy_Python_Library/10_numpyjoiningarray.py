# Joining the numpy array- Here for this we will pass concatenate()
# coloum wise
import numpy as np
pb = np.array([1,2,3])
pb1= np.array([4,5,6])
# add two 1-D
pb2=np.concatenate((pb,pb1))
print(pb2)

# Joining of 2-D arrays along with rows(axis = 1)
import numpy as np
pb = np.array([[1,2,3],[4,5,6]])
pb1= np.array([[7,8,9],[10,11,12]])
pb2=np.concatenate((pb,pb1),axis=1)
print(pb2)

# Joining array using the stack function
import numpy as np
pb = np.array([1,2,3])
pb1= np.array([4,5,6])
pb2=np.stack((pb,pb1),axis=1)
print(pb2)

# Stacking along with rows: hstack() means does not matter on index
import numpy as np
pb = np.array([1,2,3])
pb1= np.array([4,5,6])
pb2=np.hstack((pb,pb1))
print(pb2)

# Stacking alon with column using vstack:
import numpy as np
pb = np.array([1,2,3])
pb1= np.array([4,5,6])
pb2=np.vstack((pb,pb1))
print(pb2) 

# Stacking alon with height(depth):
import numpy as np
pb = np.array([1,2,3])
pb1= np.array([4,5,6])
pb2=np.dstack((pb,pb1))
print(pb2) 
# but use concating 1-d but 2-d ke liye axis