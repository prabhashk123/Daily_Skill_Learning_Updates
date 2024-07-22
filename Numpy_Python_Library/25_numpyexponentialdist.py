# Exponential dist:- It is used for describing the time till next event that is like failure or success.
# param - scale(inverse of rate(see like lam poisson dist.)),size

# Here we will draw a sample for exponential dist with 2.0 scale and 2*3 size.
from numpy import random
pb = random.exponential(scale=2, size=(2,3))
print(pb)

# visualization of exponential dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000),hist=False)
plt.show()