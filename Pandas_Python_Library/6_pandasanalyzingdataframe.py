# Analyzingdataframe:-
# Viewing the data quickly:- one of the most method for a quick overview of the dataframe is the head() method.
# this method returns the headers and a specified number of rows.

# Here we will print the first 10 rows in the dataframe:-
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\data.csv')
print(pb.head(10)) # 10 is rows by default print 5 rows. without head bhi print 5 rows

## Here we will print the last 10 rows in the dataframe:-
import pandas as pd
pb = pd.read_csv('Pandas_Python_Library\data.csv')
print(pb.tail(10)) # last ka print 10 rows

## What if you want the information about the data in the dataframe via info() function:-
import pandas as pd
df = pd.read_csv('Pandas_Python_Library\data.csv')
print(df.info())

