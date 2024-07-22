# Rounding Decimals:-There are 5 ways of rounding off the decimals in numpy: truncation, fix, rounding, floor, ceil,

# truncation: trunc() and fix()
# here we are truncating the below array,these command remove the decimals and return the float number closest to zero.
import numpy as np
# pb = np.array([-3.1666, 3.6667])
pb = np.trunc([-3.1666, 3.6667])
print(pb) # o/p float me aata hai just integer banya but hai float

# for use fix()
import numpy as np
pb = np.trunc([-3.1666, 3.6667])
print(pb) 

"""Note:-Here both use same like remove decimals and return float but mostily use trunc """

# # Rounding:-the around() function increments preceding digits or decimal by nearest to 1: if n>5=1 or n<5=0.
import numpy as np
pb = np.around(3.1666, 2)
print(pb) 

# floor() - round off decimals to the lower integer.
import numpy as np
pb = np.floor([-3.1666, 3.6667])
print(pb) 

# ceil(): round off decimals to the upper integer.just opposite of floor.
import numpy as np
pb = np.ceil([-3.1666, 3.6667])
print(pb) 

"""Notes floor and trunc and ceil ka value always float me aata hai """
