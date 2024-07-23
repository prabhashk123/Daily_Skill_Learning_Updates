import matplotlib
print(matplotlib.__version__)

# pyplot submodule
# Now we will draw a line a diagram from a certain position.
import matplotlib.pyplot as plt
import numpy as np
# draw x and y axis in array x is group of value
xpont=np.array([0,6])
ypoint=np.array([0,250])
plt.plot(xpont,ypoint)
plt.show()
