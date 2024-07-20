#Searching array-you can search an array for a certain value and return the index that get the match.by using where() bye index ke hisab se
import numpy as np
pb=np.array([1,2,3,4,5,4,4])
pbnew=np.where(pb == 4)
print(pbnew)

# now we will find the indexes where the values are even:
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8])
pbnew=np.where(pb%2==0) #remainder 0 
print(pbnew) #print index of array elements

# now we will find the indexes where the values are odd:
import numpy as np
pb=np.array([1,2,3,4,5,6,7,8])
# pbnew=np.where(pb%2!=0) 
# print(pbnew) 
pbnew=np.where(pb%2==1) 
print(pbnew) 

# Searchsorted()- perform binary search in array.
# we will find the index where value 7 should be inserted left side:- by default search left side
import numpy as np
pb=np.array([6,7,8,9])
pb1=np.searchsorted(pb,7)
print(pb1) 

# now we will search from right side:-
import numpy as np
pb=np.array([6,7,8,9])
pb1=np.searchsorted(pb,7,side='right')
print(pb1) 

# # How to search multiple values:-
# import numpy as np 
# pb=np.array([1,3,5,7])
# pb1=np.searchsorted(pb,[2,4,6])
# print(pb1) 
