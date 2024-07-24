# pandasseries:- A pandas series as like a column in a table. or It is 1-D array which holds of any type.

#Q. here we will create a simple pandas series:-
import pandas as pd
pb = [1, 7, 2]
pbnew = pd.Series(pb)
print(pbnew)
"""
O/P is as like table form according to index 
index_no| array_data_value
0       |   1
1       |    7
2       |    2
        |
"""

##Q. Labeling:- label can be used to access a specified value.
import pandas as pd
pb = [1, 7, 2] 
pbnew = pd.Series(pb)
# access acording to index here print 1 than give input index as 0.
print(pbnew[0]) 

## With Create lable you can create your name labels:-
import pandas as pd
pb = [1, 7, 2] 
pbnew = pd.Series(pb, index=["x", "y", "z"] )
print(pbnew) 

##Q. Labeling:- label can be used to access a specified value.(after creating own label)
import pandas as pd
pb = [1, 7, 2] 
pbnew = pd.Series(pb, index=["x", "y", "z"] )
print(pbnew["x"]) 

##Q. You can also use a key ar value object like a dictonary.when creating series.
# Here we will create a simple pandas series from a dictonary
import pandas as pd
cal = {"day1":420, "day2":380, "day3":390} 
pbnew = pd.Series(cal)
print(pbnew)
"""
o/p are:-
day1    420
day2    380
day3    390
dtype: int64
""" 

##Q. Now we will create a series using only data from day1 and day2:-
import pandas as pd
cal = {"day1":420, "day2":380, "day3":390} 
pbnew = pd.Series(cal, index=["day1","day2"])
print(pbnew) 

### For multidiemensional array:-
# Use DataFrame(df):- Data set in pandas are usually multidiemensional tables, and they are called dataframes. 
# series are like "columns" and dataframes is the "whole table".
# do series se df banta hai:-
#Q. we will create a dataframe from 2 series:-
import pandas as pd
pb = {"cal": [420, 380, 390], "duration": [50, 40, 45]} 
pbnew = pd.DataFrame(pb)
print(pbnew) 
