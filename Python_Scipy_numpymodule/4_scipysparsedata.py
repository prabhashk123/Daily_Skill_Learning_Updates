# waste data, unused data hota hai sabse jada zero data hota hai to use "sparse" data kahte hai. zero nhi to "dense data".
# What is sparse data: Sparse data is the data that has mostly unused elements. like the elements that dont carry any info. [1,0,2,0,4,5,6,9,2,4]
# sparse data example [1,0,2,0,0,3,0,0,0,0,0,4]
# Dense Array: [2,5,6,8,9,7,1,2,3,6]
# How to work with Sparse Data.
# scipy has a module "scipy.sparse" function. there are 2 matrics in this sparse: CSC(Compressed sparse Column) and CSR(Commpresses Sparse Row)

# CSR Matrics: here we will create a CSR matrics from an array:

## CSR Matrics: here we will create a csr matrics from an array:
import numpy as np
from scipy.sparse import csr_matrix 
pb = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(pb))
"""
O/P:-index ke hisab se
<Compressed Sparse Row sparse matrix of dtype 'int32'
        with 3 stored elements and shape (1, 9)>
  Coords        Values
  (0, 5)        1
  (0, 6)        1
  (0, 8)        2
"""
# Spare matrix Method 
import numpy as np
from scipy.sparse import csr_matrix
pb = np.array([[0,0,0],[0,0,1],[1,0,2]])
# show only "data" jo waste nhi hota dot data ke through
print(csr_matrix(pb).data)

# What if we want to count nonezeros, we can do this via "count_nonzero()" method.
import numpy as np
from scipy.sparse import csr_matrix
pb = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(pb).count_nonzero()) # 3

# For removing the zero elements from the matrix we will use "eliminate_zeros()" method.
import numpy as np
from scipy.sparse import csr_matrix
# 2_D index 0-2 hai yeha 
pb = np.array([[0,0,0],[0,0,1],[1,0,2]])
pbnew = csr_matrix(pb) 
pbnew.eliminate_zeros()
print(pbnew)
""" 
(1, 2)        1 (here 1 is array 2d index and 2 is position of array element of array other 1 is array value)
(2, 0)        1
(2, 2)        2
"""

## Eliminate duplicate entities with the sum_duplicates() method:
import numpy as np
from scipy.sparse import csr_matrix
# 2_D index 0-2 hai yeha 
pb = np.array([[0,0,0],[0,0,1],[1,0,2]])
pbnew = csr_matrix(pb) 
pbnew.sum_duplicates()
print(pbnew)

##  Here we will convert csr to csc method csc with the "tocsc()" method.
import numpy as np
from scipy.sparse import csr_matrix
# 2_D index 0-2 hai yeha 
pb = np.array([[0,0,0],[0,0,1],[1,0,2]])
pbnew = csr_matrix(pb).tocsc() 
print(pbnew)

# both me same waste value nikalna same and sum_duplicate value non zero value basically add sabhi value ko.