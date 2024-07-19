# difference between numpy array copy and view

# we will make a copy, change in original array and display both but not depend 
import numpy as np
pb=np.array([1,2,3,4,5])
pb_copy=pb.copy()
pb_copy[0]=12
print(pb)
print(pb_copy)

# Now we will make a view , change original, display both view means both depend
import numpy as np
pb=np.array([1,2,3,4,5])
# for changeg always new array
pb1=pb.view()
pb[0]=42
print(pb)
print(pb1)

