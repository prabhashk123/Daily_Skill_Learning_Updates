import matplotlib.pyplot as plt #now the pyplot package can be reffered as plt
import numpy as np
# ploting a and y
# plot() function is used to draw points or markers in a digram.
# there are two parameters for specifying points in the digram i.e x-axis and y-axis.
# the  x-axis is the horizental axis
# the y-axis is the vertical axis
xpont=np.array([1,8])
ypoint=np.array([3,10])
# plt.plot(xpont,ypoint)
# plt.show()

# Q2 ploting without line
import matplotlib.pyplot as plt
import numpy as np
xponts=np.array([1,8])
ypoints=np.array([3,10])
# plt.plot(xponts,ypoints,'o')
# plt.show()

# Q3 
import matplotlib.pyplot as plt
import numpy as np
xponts=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10,5,7])
# plt.plot(xponts,ypoints)
# plt.show()

# Default x -Points
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints)
# here by default x value according to y-axis like here 0,1,2,3,4,5
plt.show()