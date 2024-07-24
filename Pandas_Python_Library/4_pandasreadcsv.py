# read csv files:(comma seperated file) it is a simple way to store the big and biggest data sets.
# csv files containts plain text par.

## Q1.)loading the csv into a dataframe with "to_string()"
import pandas as pd
df = pd.read_csv('Pandas_Python_Library\data.csv')
print(df.to_string())
# Here to_string matlab pura data frame ko print karna chate hai.

## Q2.)loading the csv into a dataframe without "to_string()"
import pandas as pd
df = pd.read_csv('Pandas_Python_Library\data.csv')
print(df) # show only start and ending five data.

## max_rows: you can check your system's maximum rows with:-
import pandas as pd
print(pd.options.display.max_rows)#o/p 60 rows only jada to use tostring() in df.

## yes, we can increase the maximum number of rows to display the entire dataframe:-hack tacnique
import pandas as pd
pd.options.display.max_rows=9999
df = pd.read_csv('Pandas_Python_Library\data.csv')
print(df)
# so use to_string() method