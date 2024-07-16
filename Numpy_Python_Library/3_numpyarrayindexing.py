# Array indexing is the same as accessing an array element atart with Zero, second 1
import numpy as np
pb=np.array([1,2,3,4])
print(pb[0])

# We can get the 3rd and forth elements from adding them use + operator
import numpy as np
pb=np.array([1,2,3,4])
print(pb[2] + pb[3])

# Accesing the 2-D -it is like a rows and columns.
import numpy as np
pb=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd elements on the first rows is",pb[0,1])
print("5th elements on the 2nd rows is",pb[1,4])

# Accessing the 3-D same as accessing 2-D se 3-d and 4-d and 5-d
# Access index from aray
import numpy as np
pb=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Print 6 from ist2-d element is",pb[0,1,2])
print("Print 12 from 2nd2-d element is",pb[1,1,2])



 

