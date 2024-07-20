# Random meaning - Something that cannot be predicted logically.
# Now we will generate a random number from 0 to 100.
from numpy import random
pb = random.randint(100)
print(pb)

# You can also generate float() via rand() from 0 to 1
from numpy import random
pb = random.rand()
print(pb)

# You can also generate random Array.
# We will generate a 1-D array containing 5 random int from 0 to 100.
from numpy import random
pb=random.randint(100, size=(5))
print(pb)

# You can also generate random Array.
# We will generate a 2-D array with 3 rows, each row containing 5 random int from 0 to 100.
from numpy import random
pb=random.randint(100, size=(3,5))
print(pb)

# You can also generate random Array.
# We will generate a 1-D array containing 5 random float.
from numpy import random
pb=random.rand(5)
print(pb)

# You can also generate random Array.
# We will generate a 2-D array with 3 rows each  containing 5 random float.
from numpy import random
pb=random.rand(3,5)
print(pb)

# you can also generate random number from array.
# choice()
from numpy import random
pb=random.choice([3,5,7,9,1,4,6])
print(pb)

# # you can also generate random number froman 2-D array.
# choice()
from numpy import random
pb=random.choice([3,5,7,9,1,4,6],size=(3,5)) # 3 row and 5 values.
print(pb)
print(pb.ndim)