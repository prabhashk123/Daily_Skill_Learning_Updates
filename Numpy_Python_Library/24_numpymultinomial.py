# multinomial dist.->It is a generalization of binomial dist.
# parameter - n(number of outcome),pvals(list of possibilty or outcome),size(shap of returned array)

# Draw out a sample for dice roll
from numpy import random
pb = random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(pb)

# Multinomial sample will not produce single value. they will produce one value for each pvals.

# Not basically use visualization