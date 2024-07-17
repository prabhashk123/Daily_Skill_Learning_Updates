# Data types in python: string,Integer,float,boolean,complex
# Data types in Numpy:-
# i fo integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string 
# U for unicode string
# V for memory

# checking the Data Type of numpy array use -dtype
import numpy as np
pb=np.array([1,2,3,4])
print(pb.dtype) #int32 means byte bhi le liya

# checking the Data Type of numpy array use -dtype
import numpy as np
pb=np.array(["apple", "banana", 'cherry'])
print(pb.dtype)

# Creating array with a defined data type(dtype):
import numpy as np
pb=np.array([1,2,3,4],dtype='S')
print(pb)
print(pb.dtype) 

# now we will create an arary with data type of 4 byte int: 
import numpy as np
pb=np.array([1,2,3,4],dtype='i4')
print(pb)
print(pb.dtype)

# if a type is given in which the elements cannot be casted then numpy 
# will rase error what if a value cannot be converted?
# import numpy as np
# pb=np.array(['a','2','3'],dtype='i') #Here 'a' not convert in integer so give error
# print(pb.dtype)

# Converting data type in existing array - astype() means astype function jo ki copy bana deta hai array ka
import numpy as np
pb=np.array([1.1,2.1,3.1]) #float type 
pb1=pb.astype('i')
print(pb1)
print(pb1.dtype)

# Converting data type from int to boolean
import numpy as np
pb=np.array([1,0,3]) #boolean type 
pb1=pb.astype(bool)
print(pb1)
print(pb1.dtype)



