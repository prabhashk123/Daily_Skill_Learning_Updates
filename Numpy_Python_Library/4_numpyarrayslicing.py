"""Slicing Array - slicing in python means taking element from one given index to another index. """
# [start:end], [start:end:step]
# This is based on index because start from 0 to 1...
# Always skip end value of array during slice

# Now we will slice an element from 1 to 5
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9])
print(pb[1:5])

# Now we will slice from index 4 to end value here after colon means blank value is the end value of array same as start value
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9])
print(pb[4:])

# Now we will slice from the element from the begining to index 4 same as above reverse
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9])
print(pb[:4])

# Negative slicing- index 3 to end start from -1 se here -1 is not include means skip
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9])
print(pb[-6:-1])

# Step: You will use step value to determine the step of the slicing retur every
# Other value from 1 to 5 for Alternate use
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9])
print(pb[1:5:2])

# Now return every oter number from the entire array means blanck than start from index 0 se har dusra element
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8,9])
print(pb[::2])

# Slicing 2-D Array
import numpy as np
pb=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("print 7,8,9 is",pb[1,1:4])

# Anothher example dono element
import numpy as np
pb=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("print 3,8 is",pb[0:2,2])

# Anothher example through 2-D print from both, index 1:4
import numpy as np
pb=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# Here 0:2 is first and 2nd array consider last array so 0,1,2
print(pb[0:2,1:4])
