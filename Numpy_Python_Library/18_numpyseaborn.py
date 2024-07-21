# python poweful libraray "MATPLOTLIB" for data visualization for Data analaytic role use.
# Sublibray of matplotlib(pyplot -libray of inside matplotlib)-->seaborn 
# seaborn is the libray that uses matplotlib to plot graph that is "pyplot".
# pyplot is submodule.
# Distplot:- distribution plot(curve plot - histogram)
import matplotlib.pyplot as plt
import seaborn as sns
# sns.displot([0,1,2,3,4,5])
sns.distplot([0,1,2,3,4,5])
plt.show()

# ploting a displot without the histogram.matlab color shadow remove
import matplotlib.pyplot as plt
import seaborn as sns
# array ko var me bhi pass kar sakte hai
x=[0,1,2,3,4,5]
sns.distplot(x,hist=False)
plt.show()

