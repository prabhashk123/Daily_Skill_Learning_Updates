# Reshaping-means changing the shape of an array like adding or removing the elements.

# reshaping from 1-D to 2-D
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9,10,11,12]) 
# ham original array par change nhi kar sate so array ka copy but yeha use reshaping krenge
pb1=pb.reshape(4,3) # four array using each three elements.
print(pb1)
print(pb1.ndim)

# reshaping from 1-D to 3-D 3-D me 2 index
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9,10,11,12]) 
pb1=pb.reshape(2,3,2) #first 2 is index,3 is array ,last 2 elements contain 2 each
print(pb1)
print(pb1.ndim)

# length ke through factorise karna hai same element in each array
# view original document ko show karta hai
# Return copy or view
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8]) 
print(pb.reshape(2,4).base) #this is view matlab o/p tuta nahi hai

# unknown diemension - you are only allowed to have one unknowen diemension.pass -1
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8]) 
pb1=pb.reshape(2,2,-1) # -1 ka bhi matalb 2 element here arguement nhi pata tab use mens value nhi pata tab use
print(pb1)

# Flattening the array by converting multidiemensional array in 1-D.
# basic starting array is in List.
import numpy as np
pb=np.array([[1,2,3],[4,5,6]])
pb1=pb.reshape(-1) #change 1-diemension
print(pb1)

# There are a lot of function for changing the shape of an array in numpy. like flatten, reval and also 
# rearranging the element route90, flip,fliplr,flippud. they all are actually comes under advanced numpy.

