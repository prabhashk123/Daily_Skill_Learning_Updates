# Display the multiple plots:- with subplot() you can draw multiple plots in one figure.
"""import matplotlib.pyplot as plt
import numpy as np

# plot1:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1) # the figure has 1 for row, 2 for column, 1 for plot 1.
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()"""

## Now we will draw 2 plot on top of each other
"""import matplotlib.pyplot as plt
import numpy as np

# plot1:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1) 
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x,y)
plt.show()"""

## Now we will draw challenging of 6 plot:-
import matplotlib.pyplot as plt
import numpy as np

# plot1:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1) 
plt.plot(x,y)
plt.title(1)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.plot(x,y)
plt.title(2)

# plot3:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,3) 
plt.plot(x,y)
plt.title(3)

#plot4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title(4)

# plot5:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,5) 
plt.plot(x,y)
plt.title(5)

#plot6
x = np.array([0,1,2,3])
y = np.array([10,20,30,60])
plt.subplot(2,3,6)
plt.plot(x,y)
plt.title(6)

plt.show() 

## Now we will give supertitle()-sup for plot:-
import matplotlib.pyplot as plt
import numpy as np

# plot1:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1) 
plt.plot(x,y)
plt.title(1)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.plot(x,y)
plt.title(2)

# plot3:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,3) 
plt.plot(x,y)
plt.title(3)

#plot4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title(4)

# plot5:-
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,5) 
plt.plot(x,y)
plt.title(5)

#plot6
x = np.array([0,1,2,3])
y = np.array([10,20,30,60])
plt.subplot(2,3,6)
plt.plot(x,y)
plt.title(6)

plt.suptitle("My Shop")
plt.show() 

"""Note:-#plt.subplot(1,2,1)- the figure has 1 for row, 2 for column, 1 for plot 1."""