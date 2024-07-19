# Iterating Array - means going through the elements one by one or step by step. like for loop.

# Iterate the element of 1-D 
import numpy as np
pb=np.array([1,2,3])
for i in pb:
    print(i)

# Iterate the element of 2-D  here 2-index 0,1
import numpy as np
pb=np.array([[1,2,3],[4,5,6]])
for i in pb:
    print(i)

# Iterate on each scalar element of the 2-D
import numpy as np
pb=np.array([[1,2,3],[4,5,6]])
# nested loop because index inside index
for i in pb:
    for a in i:
        print(a)

# Iterate 3-D
import numpy as np
pb=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in pb:
    for a in i:
        for b in a:
            print(b)

# Iterating arrays the nditer() function.use multiple array ke liye complex array
# Now we will Iterate on each scalar element.
import numpy as np
pb=np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(pb):
    print(i)

# now we will Iterate with different stap size
import numpy as np
pb=np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(pb[:, ::2]):
    print(i)
    

 