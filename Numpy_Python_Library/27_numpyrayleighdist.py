# Rayleightdist(use signal processing for ml and ds)
# param- scale(standard deviation, how flat the distribution is .. default 1.0), size

# Sample for Rl with of 2.0 with size of 2*3
from numpy import random
pb = random.rayleigh(scale=2,size=(2,3))
print(pb)

# visualization of rayleigh dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()
