# Cheat in Df:- Q like real life project matrix in df:-use

# Method-1 for matrix:- We specify value for each column
import pandas as pd
# Dictonary form me dataframe
df = pd.DataFrame({"a":[4,5,6], "b":[7,8,9], "c":[10,11,12]},index=[1,2,3])
print(df)
"""
   a  b   c
1  4  7  10
2  5  8  11
3  6  9  12
"""

## method-2 Specify value for rows
import pandas as pd
df = pd.DataFrame([[4,5,6],[7,8,9],[10,11,12]],index=[1,2,3], columns = ['a', 'b', 'c'])
print(df) 
"""
    a   b   c
1   4   5   6
2   7   8   9
3  10  11  12
"""

##Q) creating a df with multiindex
import pandas as pd
df = pd.DataFrame({"a":[4,5,6], "b":[7,8,9], "c":[10,11,12]},index=pd.MultiIndex.from_tuples([('d',1),('d',2),('e',2)],names=['N','v']))
print(df) 
# o/p
"""
     a  b   c
N v
d 1  4  7  10
  2  5  8  11
e 2  6  9  12
"""