# Now we will create a numpy ndarray object
# The array object in numpy is call ndarray
# use array function for create array()

# Here use list inside array function
import numpy as np
x=np.array([1,2,3,4,5,6])
print(x)
print(type(x))

# we can also pass a list , tuple or any array like object with 
# array(). and it will be converted to ndarray.

# here use tuple inside array()
import numpy as np
y=np.array((1,2,3,4,5))
print(y)
print(type(y))

# Dimension in Arrays - a dimensions in array is one level of aray depth(nested array)
# 0-D Arrays - scalars, are the elements in an array, each value in an array is a 0-D arary.

# Now we will create 0_d arary with value 42
import numpy as np 
z=np.array(42)
print(z) # normally use as it is print value that is 0_d arary means jo bhi output aata hai use 0_d array kahte hai

# 1-D Arrays - an ararys that has 0-D arays as its element is called uni directional or 1-D here list is element nrmally use
import numpy as np
p=np.array([1,2,3,4,5])
print(p)

# Create a 2-D array containing 2 arrays with certain values.
import numpy as np
k=np.array([[1,2,3], [4,5,6]])
print(k)

# Now we will create 3-D array with two 2-D array.
import numpy as np
l=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(l)

# Check how many diemensions the array have "ndim" attribute
import numpy as np
a=np.array(43)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Create an array with 5 diemension and verify that it has 5 diemension use "ndmin=5"
import numpy as np
m=np.array([1,2,3,4,5],ndmin=5)
print(m)
print("Number of diemension is",m.ndim)
# O/P=[[[[[1 2 3 4 5]]]]]


