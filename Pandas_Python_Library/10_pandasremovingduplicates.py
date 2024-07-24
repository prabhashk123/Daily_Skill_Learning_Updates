# Removing the Duplicate data values:-
# if first you need to discover the duplicate values via "duplicate()" method.

##Q. loading and reading the original dataframe
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
print(pb.to_string())

##Q. Returns "True" for every row that is duplicate otherwise return "false":-
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
print(pb.duplicated()) 

## Removing the dplicate from data set. via drop_dplicates().
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
pb.drop_duplicates(inplace=True) 
# Here "inplace" tab use karte jab original data me koe change karna rahta hai lekin wo koe naya dataframe nhi banata matlab new var nhi banana parta hai sabcheej original data par modification karega
print(pb.to_string()) # remove 12 rows
