# Hyperbolic func:-numpy provide the universal function like sinh(), cosh(), and tanh() that takes values in radian and produce the corresponding sin, cos and tan values.like inverse function
# Example-here we will find the value of sinh(pi/2) 
import numpy as np
pb = np.sinh(np.pi/2)
print(pb) # so ans is 2.3012989023072947

# Q. we will now find cosh() values in array.
import numpy as np
pb = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
pbnew = np.cosh(pb)
print(pbnew) # o/p difference b/w .2 ka

# Finding angles:-
#Q. here we can also find angles:- arcsinh(), arccosh() and arctanh() that takes value in radians and produce the corresponding sin, cos and tan values.

# we will now find the angle of 1.0
import numpy as np
pb = np.arcsinh(1.0)
print(pb)

# we will now find the angle of each value in array. o/p is angle is in degree.
import numpy as np
pb = np.array([0.1, 0.2, 0.5])
pbnew = np.arctanh(pb)
print(pbnew)