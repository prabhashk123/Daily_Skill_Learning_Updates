# random arrangement
# Permutaion- refers to an arrangement of elements like [3,2,1] is permutation of [1,2,3] and vice versa.
# The numpy random module provide 2 methods: shuffle() and permutation().
# shuffle() make changeg to original array.

# Now we will randomly shuffle elements of the below arrays:-
from numpy import random
import numpy as np
pb = np.array([1,2,3,4,5])
random.shuffle(pb)
print(pb)

# Now we will generate a permutation of elements for the below array:-
# The permutatrion() not change on original array means leaves the original array unchanged.
# Note:- This use when trail ya see the result. otherwise use shuffle()
from numpy import random 
import numpy as np
pb = np.array([1,2,3,4,5])
random.permutation(pb)
print(pb)

# Change if not give new variable.
from numpy import random 
import numpy as np
pb = np.array([1,2,3,4,5])
print(random.permutation(pb))