# logistic dist - describe growth(Machine learning and neuration network me bahut use hota because har business me growth chaiye)
# -> it is basically imp in regression and neural network.
# parameter - loc(mean- default val 0), scale(standard deviation, 1), size

# draw 2*2 sample of logistic with mean 1 and stndv 2.
from numpy import random
pb=random.logistic(loc=1,scale=2,size=(2,3))
print(pb)

# visualization of logistic dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000),hist=False)
plt.show()

# logistic or normal dist same but area jada hoti hasi normal se matlab probabilit or posibility jada hota hai 
# antar only loc matlab mean pr not scale pr