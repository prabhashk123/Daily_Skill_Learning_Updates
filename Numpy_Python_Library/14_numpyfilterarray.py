# Geting some elements out of an existing array and creating a new array is called filtering.
# A boolean index list is a list of boolean corresponding to indexes in the array:(True and False) by defalut filter True

# create an array from the element on index 0 to 2:
import numpy as np
pb=np.array([41,42,43,44])
pb1=[True,False,True,False]
pb2=pb[pb1]
print(pb2) 

# Now we will create a filter array that will return only value higher than 42
import numpy as np
pb=np.array([41,42,43,44])
filter_pb_or_empty_pb=[]
for element in pb:
    if element>42:
        filter_pb_or_empty_pb.append(True) 
    else:
        filter_pb_or_empty_pb.append(False)
pb1=pb[filter_pb_or_empty_pb]
print(filter_pb_or_empty_pb)
print(pb1)

# Create a filter array will return only even elements from the original array
import numpy as np
pb=np.array([1,2,3,4,5,6,7])
pbempty=[]
for i in pb:
    if i%2==0:
        pbempty.append(True)
    else:
        pbempty.append(False)
pbnew=pb[pbempty]
print(pbempty)
print(pbnew)

"""Alternate Method"""
# yes you can also create filter directly from array:-  
#METHOD-2 ALTERNATE soln Now we will create a filter array that will return only value higher than 42
import numpy as np
pb=np.array([41,42,43,44])
pbempty=pb>42
pbnew = pb[pbempty]
print(pbempty)
print(pbnew)

# # yes you can also create filter directly from array:-
# Create a filter array that will return only even elements from the original array
import numpy as np
pb=np.array([1,2,3,4,5,6,7])
pbempty=pb % 2==0
pbnew=pb[pbempty]
print(pbempty)
print(pbnew)