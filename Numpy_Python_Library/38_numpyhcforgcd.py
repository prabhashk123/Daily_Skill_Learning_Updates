# HCF(Higest Common Factor) or GCD(Greates common Denominator) both same:-

# Here we will find th HCF of the below 2 numbers:-
import numpy as np
pb1 = 6
pb2 = 9
pbnew = np.gcd(pb1, pb2)
print(pbnew) # answer will be 3 because that is the highest number and both number can be divided by (6/3=2 and 9/3=3)

# find the HCF or GCD in an Array:-
# the reduce() method will use the ufunc, in this case the gcd() function on each element and it will reduce array by 1 diemension.
import numpy as np
pb = np.array([20,8,32,16,36])
pbnew = np.gcd.reduce(pb)
print(pbnew)
