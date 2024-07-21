# Poission Dist - (jhuth) for ex- koe 10 gilas pani to wo 11 gilas kab piyega
# define->it estimates how many time an event can happen. means probability nikala gaya.
# param - lam(number of occurence or rate), size

# Gnerate a random 1*10 dist for the occurance 2
from numpy import random
pb = random.poisson(lam=2, size=10)
print(pb)

# visualization of poisson distribution:-
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

# presenting both the plots in same figure normal and poisson dist.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(loc=50, scale=7, size=1000),hist=False,label='Normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='Poisson')
plt.show()

# Note :n*p==lam haota hai binomial me n-number of occurence or p-probability


