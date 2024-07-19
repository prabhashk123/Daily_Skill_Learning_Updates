# shap of an array - the shap of array is the number of elements in wach diemension.

# now we will try to get the shap of an arrary. shape menas number of elements
import numpy as np
pb=np.array([[1,2,3,4] ,[5,6,7,8]])
print(pb.shape)
# o/p=(2,4) which means array has 2 diemension and it has 4 elements.

# now we will create a 5-d array using ndmin
import numpy as np
pb=np.array([1,2,3,4],ndmin=5)
print(pb)
print(pb.ndim)
print("Shape of array is ",pb.shape)
# o/p Shape of array is  (1, 1, 1, 1, 4) means [ [ [ [ [1,2,3,4]]]]]
# ---------------------------------------------1 1 1 1 4--elements
# try for same 2d,3d,4d on problems