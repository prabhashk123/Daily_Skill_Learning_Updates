# What is set? : a set is a collection of unique elements

# For creating the set we use numpy as unique() method to find the unique elements from and array:

# Q. here we will cinvert the array with repeted elements to a set.
# we will now find the angle of each value in array. o/p is angle is in degree.
# unique matlab one time if repeated elements that covert in common ans
import numpy as np
pb = np.array([1,1,1,2,3,4,5,5,6,7])
pbnew = np.unique(pb)
print(pbnew) 

# Q. to find the unique value of 2 1-D array, we will use union1d() method.
import numpy as np
pb1 = np.array([1,2,3,4])
pb2 = np.array([3,4,5,6])
pbnew = np.union1d(pb1,pb2)
print(pbnew) 

# Q.To find the only value that are present in both array, we are use intersect1d() method.
import numpy as np
pb1 = np.array([1,2,3,4])
pb2 = np.array([3,4,5,6])
pbnew = np.intersect1d(pb1,pb2,assume_unique=True)
print(pbnew) # o/p [3 4]
# Note:- here above pass assume_unique paramete is passes because this is increases the comptation speed fast means compare fast and return. always assume_unique=True used. 

# Q. To find the only value that are in first set  and Not present in the 2nd set: use setfdiff1d()
import numpy as np
pb1 = np.array([1,2,3,4])
pb2 = np.array([3,4,5,6])
pbnew = np.setdiff1d(pb1,pb2,assume_unique=True)
print(pbnew) # o/p [1 2]

# Q. To find the only value that are Not present in both set:  use setxorid() method.
pb1 = np.array([1,2,3,4])
pb2 = np.array([3,4,5,6])
pbnew = np.setxor1d(pb1,pb2,assume_unique=True)
print(pbnew) # o/p [1 2 5 6]