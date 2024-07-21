# Normal Distribution(Gaussian Distribution):-very important.
# random.normal() method- loc, scale, size 
# the curve of a normal distr is also called as bell curve.

# We are generating a random normal distribution of size.
from numpy import random
pb = random.normal(size=(2,3)) 
print(pb)

# Here we will generate a random normal distribution of size 2*3 with mean(loc) at 1 and standard deviation(scale) of 2.
from numpy import random
pb = random.normal(loc=1,scale=2,size=(2,3)) 
print(pb) 

# Visualization of normal distribution 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# size matlab value pas kiye hist matlab only curve chaiye
sns.distplot(random.normal(size=1000),hist=False)
plt.show()





