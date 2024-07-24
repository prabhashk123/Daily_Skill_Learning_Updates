# How to add data value in the bar or line graph using python matplotlib.

import matplotlib.pyplot as plt

# sample data
categories = ['category 1', 'Category 2', 'Category 3']
values = [20, 35, 45]

# create a bar plot
plt.bar(categories,values)
# bar value ko check karke ak ak point pe likhte jao
for i, value in enumerate(values):
    plt.text(i,value +2,str(value),ha='center',va='bottom') # +3 is as like value shift upper like margine style

plt.show()

## Q) Same for line graph:-
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_value = [10,25,13,32,20]
plt.plot(x_values, y_value, marker='o')
plt.show()

## Q) Same for line graph add value in point par:-
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_value = [10,25,13,32,20]
plt.plot(x_values, y_value, marker='o')
for x,y in zip(x_values, y_value): #jaha dono x,y match waha loop chalao esko anoted kahte hai
    plt.text(x,y +2, str(y), ha='center', va='bottom')
    
plt.show()