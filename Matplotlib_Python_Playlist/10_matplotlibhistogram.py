# Jab koe pattern janna rahta ya koe distribution karna rahta hai tab.
# define:-a histogram is the graph showing the frequency distribution.

# Q.)say you ask for height of 250 people then how we will make a histogram.
# hist() function
import matplotlib.pyplot as plt
import numpy as np
# numpy generate randomly array use normal distribution.
x = np.random.normal(170,10,250)
print(x)

"""Note:- the hist() function will read the array and produce the histogram"""
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170,10,250)
plt.hist(x, width=0.7,color='r')
plt.show()

# same as bar() like color width ...etc.
