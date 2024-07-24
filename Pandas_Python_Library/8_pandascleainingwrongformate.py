# Data in a wrong formate:-to fix this problem there are 2 ways:-
# removing the rows or convert all the cells in the same formate.

##Q. loading and reading the original dataframe
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
print(pb.to_string())

## Now let's try to convert all the cells in the date column into dates via t0_datetime() function.
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
pb["Date"] = pd.to_datetime(pb['Date'],format='mixed')
print(pb.to_string()) 

## Here now we will remove the rows with a NULL value in the 'Date' column.
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
pb["Date"] = pd.to_datetime(pb['Date'],format='mixed')
pb.dropna(subset=['Date'], inplace=True) 
print(pb.to_string())# remove 22 no rows.  