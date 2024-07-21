# Binomial dist(distribution)- discrete dist- binary output. 
# for example sikka me head ya tail.
# param - n(number of trails), p(probability), size(shape-returned array)

# Given 10 trail for coin which will generate 10 data points:
# from numpy import random
# pb = random.binomial(n=10, p=0.5, size=10)
# print(pb)

# visualizatio of binomial dist
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.binomial(n=10, p=0.5,size=1000),hist=True, kde=False)
# plt.show()

# Difference b/w normal and binpmial -
# normal(contineous) and binomial(discrete) --graph

# Q.)I use 500 data point for binomial and under 100 data point for normal dist.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50,scale=5,size=1000),hist=False, label='normal')
sns.distplot(random.binomial(n=100,p=0.5,size=1000),hist=False, label='binomial')
plt.show()