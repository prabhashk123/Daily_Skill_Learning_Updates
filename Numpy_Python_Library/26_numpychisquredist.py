# chi square dist :->it is basically used as a basis to verify the hypothesis.
# param - df(degree of freedom), size

# sample for chi square dist with 2 with size 2*3
from numpy import random 
pb = random.chisquare(df=2, size=(2,3))
print(pb)

# visualization of chi square ye sab data science
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1,size=100),hist=False)
plt.show()