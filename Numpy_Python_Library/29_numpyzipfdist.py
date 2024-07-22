# Zipf Dist:- its defination is like.. common word in English has occurs nearly 1/5 time as of the most hindi words
# param - a(dist), size

# sample for zip dist with a as 2 with size 2*3
# visualization of logistic dist
from numpy import random
pb = random.zipf(a=2,size=(2,3))
print(pb)

# visualization of Zipf dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
pb = random.zipf(a=2,size=(1000))
# yeha varaiable me asin dist ko yani random. use ke liye.es trah se bhi kar sakte hai
sns.distplot(pb[pb<10],kde=False,color='green')
plt.show()

# ----------------End random data distribution-----------------