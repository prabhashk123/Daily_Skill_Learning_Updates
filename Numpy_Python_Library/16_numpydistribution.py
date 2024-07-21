# data distribution is a list of all possible value and how often each value occur.
# such list are important when working with statistics and data science.

# Random distribution: probability function.

# Now we will generate 1-D with 100 values where each value has to be 3,5,7,9
# The probability for the value is set to be 0.1
# The probability for the value is set to be 0.3
# The probability for the value is set to be 0.6
# The probability for the value is set to be 0
# The sum of all probility number should be "1".

from numpy import random
pb = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print(pb)

# now we will return 2-D with 3 rows each containing 5 values:
from numpy import random
pb = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(pb)

