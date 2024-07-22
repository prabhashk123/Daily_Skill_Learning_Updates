# Arithematic operator : +, -, /, *
# by using ufunc additional arguments like, where, dtype and out.

# Here now we will use add() not use operator:-
import numpy as np
pb1 = np.array([10,11,12,13,14,15])
pb2 = np.array([10,11,12,13,14,15])
pbnew = np.add(pb1, pb2)
print(pbnew)

# Example of sustracting the value using array use itration like loop use but numpy se esily
import numpy as np
pb1 = np.array([10,11,12,13,14,15])
pb2 = np.array([10,11,12,13,14,15])
pbnew = np.subtract(pb1, pb2)
print(pbnew)

# for multiplication
import numpy as np
pb1 = np.array([10,11,12,13,14,15])
pb2 = np.array([10,11,12,13,14,15])
pbnew = np.multiply(pb1, pb2)
print(pbnew)

# for divide
import numpy as np
pb1 = np.array([10,11,12,13,14,15])
pb2 = np.array([10,11,12,13,14,15])
pbnew = np.divide(pb1, pb2)
print(pbnew)

# power() func raises the value from ist array to the power of the values of the 2nd array and return the result in a new array.
import numpy as np
pb1 = np.array([10,20,30,40,50,60])
pb2 = np.array([3,5,6,8,2,33])
pbnew = np.power(pb1, pb2)
print(pbnew)

# Remainder- mod() and reminder() functions returns the reminder of the first array corrosponding  to the 2nd array and result in the new array.
# By using mod() recomendation.
import numpy as np
pb1 = np.array([10,20,30,40,50,60])
pb2 = np.array([3,7,9,8,2,33])
pbnew = np.mod(pb1, pb2)
print(pbnew)

# By using reminder()
import numpy as np
pb1 = np.array([10,20,30,40,50,60])
pb2 = np.array([3,7,9,8,2,33])
pbnew = np.remainder(pb1, pb2)
print(pbnew)

# # quotitent and mod(reminder) means bhagfal
# the divmod() function return both the quotient and mod.
import numpy as np
pb1 = np.array([10,20,30,40,50,60])
pb2 = np.array([3,7,9,8,2,33])
pbnew = np.divmod(pb1, pb2)
print(pbnew)

# #Absolute() and abs() - do the same operation but here should use absolute() to avoide confusion with Python inbuilt function math.abs()
import numpy as np
pb = np.array([-1,-2,-3,-4,-5])
pbnew = np.absolute(pb)
print(pbnew)


