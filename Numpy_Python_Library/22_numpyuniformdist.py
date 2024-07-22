# uniform dist:- it is only made for probability(p)
# param - a(lower bound ka matlab prob - 0.0), b(upper bound last prob 1.0), size

from numpy import random
pb=random.uniform(size=(2,3))
print(pb)

# visualization of uniform dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000),hist=False)
plt.show()

# data analytic use 1 se jada probability nhi hota