# Wrong Data:-its only a wrong dsta.


##Q. loading and reading the original dataframe
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
print(pb.to_string())

## Here we will set "Duration" = 45 in row 7.
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
pb.loc[7, 'Duration'] = 45
print(pb.to_string()) 

## for larger data set: now here we will loop through all the values in "Duration" column if the value is higher than 120 than set it to 120.(VVI)
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
for i in pb.index:
    if pb.loc[i, "Duration"] > 120:
        pb.loc[i,"Duration"] = 120
print(pb.to_string())

## you can also remove the rows for wrong data in larger dataset. 
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
for i in pb.index: #check indexing one by one
    if pb.loc[i, "Duration"] > 120:
        pb.drop(i, inplace=True)
print(pb.to_string())
