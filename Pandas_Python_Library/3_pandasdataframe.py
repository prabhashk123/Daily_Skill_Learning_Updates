# DataFrame:-It is a 2-D data strcture like a 2-D array with table including,rows and columns.
import pandas as pd
data = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(data)
print(pbnew)
"""
o/p are:-
   cal  duration
0  420        50
1  380        40
2  390        45
"""

## Locate row:- pandas use the loc attribute to return one or more specified row:-
import pandas as pd
data = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(data)
print(pbnew.loc[0]) #o/p zero index wala
# its o/p is series form me

##Q.example of returning(any program me o/p hoti hai) row 0 and 1
import pandas as pd
data = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(data)
print(pbnew.loc[[0,1]]) #yeha 2-D use because 2 alag-alag array hai so ye 2-D hai
# eska o/p datafram me

##** named Index:- with the index argumts, you can name your own index:-esme index replace
import pandas as pd
data = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(data, index=['Day1', 'Day2', 'Day3'])
print(pbnew) 

##**##** located named Index:-o/p series
import pandas as pd
data = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(data, index=['Day1', 'Day2', 'Day3'])
print(pbnew.loc["Day2"])  

## o/p in dataframe:- for 2-D
import pandas as pd
data = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(data, index=['Day1', 'Day2', 'Day3'])
print(pbnew.loc[["Day1","Day2"]]) 

## Load the data from the csv file into dataframe:-i.e data.csv file name
import pandas as pd
fileloaad = pd.read_csv('data.csv')
print(fileloaad)
