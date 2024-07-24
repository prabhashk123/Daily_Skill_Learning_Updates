# Creating the pie chart.
# pie() function use.
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])

plt.pie(y)
plt.show()
# move anticlock wise time 3 baje se like yeha se start zero.

# Now we label the pie chart:-
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
# make var of label
mylabels = ["Apple", "Banana", "Cherry", "mango"]

plt.pie(y, labels=mylabels)
plt.show()

# Startangle parameter- The default start angle is at the x-axis but you can change start angle by specifying startangle parameter.
# default angle=0* antilcolck wise move right to left
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
plt.pie(y,labels=mylabels, startangle=90)
plt.show()

# How to explode the pichart by a value:cutting pie chart:-
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
# make a var any name 
myexplode = [0.2, 0, 0, 0] # fridge center se .2 pe catna hai cuting pichart
plt.pie(y,labels=mylabels,explode=myexplode)
plt.show()

## The shadow parameter for creativity:- use shadow for sundar dikhne 3-d jeasa image
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y,labels=mylabels,explode=myexplode, shadow=True)
plt.show()

## you can also specify the color for each wedge of piechart.
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
mycolor = ["black", "hotpink", "blue", "green"]
plt.pie(y,labels=mylabels,colors=mycolor)
plt.show()

## We can also add the legend-list of explaination
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
plt.pie(y,labels=mylabels)
plt.legend() #side me descipition aa jata pi chart me
plt.show()

## Now we will add legend with header on legend:-
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 20, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
plt.pie(y,labels=mylabels) # esme bhi alag alge chart de sakte hai
plt.legend(title = "Fruits")
plt.show()