# integer location function via "iloc()":-
# dataframe.iloc[row_ind, column]

## selecting a single elements
# val = dataframe.iloc[row,column]
## Selecting a specific row
# val = dataframe.iloc[row_index]
## selecting a multiple row element
# val = dataframe.iloc[startrow:endrow]
## selecting a specific row and column 
# val = dataframe.iloc[[row1, row2],[col1,col2]]
## selecting a all row for specific column
# val = dataframe.iloc[:, [col1, col2]]

#Q)Example-
import pandas as pd 
data = {'name': ['shared', 'sanjay', 'piyush', 'dhanraj'],'age':[25, 30, 22, 28], 'country':["dubai","canada","uk","australlia"]}
df = pd.DataFrame(data)
print(df)
# o/p
""" 
      name  age     country
0   shared   25       dubai
1   sanjay   30      canada
2   piyush   22          uk
3  dhanraj   28  australlia
"""
# Now selecting 'canada
element = df.iloc[1,2]
# selecting specific rows and columns
subset = df.iloc[1:3, 0:2]
print(element)
print(subset)
# 