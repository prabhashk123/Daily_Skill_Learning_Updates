# Cleaining data:-It is mean fixing the bad data in your data set(bahut data collection of data is called set data).

# bad data could be: empty cell, data in a wrong format, duplicat data and wrong data.

# Empty cell:- it will give you wrong result always, we will have to remove rows always that contain the bad data. 

##Q. loading and reading the original dataframe
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
print(pb.to_string())

##Q. Here we will return a new data frame with no empty
#  cell use dropna() function .  
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
# not change original data
pbnew = pb.dropna()
print(pbnew.to_string())

##Q. If in case you want to change the original dataframe,than use the inplace=True argument. 
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
# original data par change
pb.dropna(inplace=True) 
print(pb.to_string())

## Q.Replacing the empty value: we will use the "fillna()" method which will allow us to replace the empty cell with a value.
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
pb.fillna(135, inplace=True)
print(pb.to_string())

##Q. To replace only the empty value for one column, you need to specify the "column name" using fillna() method:-
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
pb["Calories"].fillna(135, inplace=True)
print(pb.to_string())

##Q. Here we can also replace the empty cell using mean(), median() or mode().
# Ex- Calculate the MEAN and replace the empty values with it.
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
# average value nikale first
x = pb["Calories"].mean()
pb["Calories"].fillna(x, inplace=True)
print(pb.to_string())

# Ex- Calculate the MEDIAN and replace the empty values with it.(MOSTLY USED)
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
# average value nikale first
x = pb["Calories"].median()
pb["Calories"].fillna(x, inplace=True)
print(pb.to_string())

# Ex- Calculate the MODE and replace the empty values with it.JO jada use hua usko fill kar deta hai mode:-
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\dirtydata.csv')
# average value nikale first,here index use for example loop used for index according
x = pb["Calories"].mode()[0]
pb["Calories"].fillna(x, inplace=True)
print(pb.to_string())