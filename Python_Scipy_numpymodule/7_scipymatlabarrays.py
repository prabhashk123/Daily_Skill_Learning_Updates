# sare data ka input array jeasa hota hai esme
# Scipy matlab Arrays: "Exporting" the data in Matlab format
# for converting or export data we use "savemat()". here we have 3 parameters: "filename(jis file me data save krenge), mdict(ak dictonary hote), do_compression(boolean value by default False)".
# example : here now we will export the below array as variable name "vec" to mat file.
from scipy import io 
import numpy as np
pb = np.arange(10)
io.savemat('pb.mat', {"vec": pb})

# here now we will import the existing mat file. it have only 1 parameter that is filename:

from scipy import io 
import numpy as np
pb = np.array([0,1,2,3,4,5,6,7,8,9])
#Export
io.savemat('pb.mat', {"vec": pb})
#import
pbnew = io.loadmat('pb.mat', squeeze_me = True)
# print(pbnew) for open file print terminal
# particular var accesss
print(pbnew['vec'])

# This matfile open in terminal