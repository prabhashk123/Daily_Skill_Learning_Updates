# Trigonometric func:->numpy provide the universal function like sin(), cos(), and tan() that takes values in radian and produce the corresponding sin, cos and tan values.
# Here now we will find the sin value of p1/2.
# here convert radian to degree radians*180/pi=pi/2*180/pi=90 so sin90=1.
import numpy as np
pb = np.sin(np.pi/2)
print(pb) # so ans is 1.0

# We will now find the sin value of an array.
import numpy as np
pb = np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
pbnew = np.sin(pb)
print(pbnew)

# Convert Degree into radians:-By default all of the trigonometric function  takes radians as parameter.
# radians value are pi/180* degree value

#Q. here we will convert all the array values degree to radians.
pb = np.array([90, 180, 270, 360])
pbnew = np.deg2rad(pb)
print(pbnew)

#Q. here we will convert all the array values radians into degree.
pb = np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
pbnew = np.rad2deg(pb)
print(pbnew)

#Q. here we can also find angles:- arcsin(), arccos() and arctan() that takes value in radians and produce the corresponding sin, cos and tan values.

# we will now find the angle of 1.0
import numpy as np
pb = np.arcsin(1.0)
print(pb)

# we will now find the angle of each value in array. o/p is angle is in degree.
import numpy as np
pb = np.array([1, -1, 0.1])
pbnew = np.arcsin(pb)
print(pbnew)

# here we can also find the hypoteneous using the pythagoras theorem in numpy.
# hypo() function tahat takes value in radians and produce the corresponding sin, cos and tan values.
# example- here we eill find the hypo for 3 base and 4 perpendicular.
# read hypothenios and pythogores theorem.
import numpy as np
base = 3
perpendicular = 4
pb = np.hypot(base, perpendicular)
print(pb)





