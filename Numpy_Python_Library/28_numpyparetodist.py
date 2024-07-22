# Pareto Dist :- 80:20 ratio.(20% factors Cause 80% Outcoume of result deti hai)
# param- a(shape), size

# sample for paretodist with shape 2 with size 2*3
from numpy import random
pb= random.pareto(a=2, size=(2,3))
print(pb)

# visualization of logistic dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2,size=1000),hist=True,kde=False)
plt.show()