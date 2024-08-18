# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

"""string = "abracadabra"
You can access an index by:
print string[5]
a

What if you would like to assign a value?
string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?

1)One solution is to convert the string to a list and then change the value.
Example:-
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print string
abrackdabra
Another approach is to slice the string and join it back.
Example

string = string[:5] + "k" + string[6:]
print string
abrackdabra
"""
## 
"""Q.Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M  is 3 times N .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters."""
# def design(n, m):
#     for i in range(n//2):
#         print((((2*i)+1)*(".|.")).center(m, "-"))
#     print("WELCOME".center(m, "-"))
#     for i in range(n//2):
#         print((((2*(n//2-i))-1)*(".|.")).center(m, "-"))
# if __name__ == "__main__":
#     n, m = input().split()
#     design(int(n), int(m))

##
"""Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space."""
# def print_formatted(number):
#     # Determine the width needed for padding (width of the binary representation of `number`)
#     width = len(bin(number)) - 2
 
#     for i in range(1, number + 1):
#         # Decimal
#         dec = str(i)
#         # Octal
#         octal = oct(i)[2:]
#         # Hexadecimal (capitalized)
#         hexa = hex(i)[2:].upper()
#         # Binary
#         binary = bin(i)[2:]
 
#         # Print each value right-aligned with the calculated width
#         print(f"{dec:>{width}} {octal:>{width}} {hexa:>{width}} {binary:>{width}}")
 
# # Input handling and function call
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


## Python Basic certificat of Hacker ranks
# Q1.
# import math
# import os
# import random
# import re
# import sys


# class Multiset:
#     def __init__(self):
#         self.elements = {}
        
#     def add(self, val):
#         # adds one occurrence of val from the multiset, if any
#         if val in self.elements:
#             self.elements[val] += 1
#         else:
#             self.elements[val] = 1

#     def remove(self, val):
#         # removes one occurrence of val from the multiset, if any
#         if val in self.elements:
#             if self.elements[val] > 1:
#                 self.elements[val] -= 1
#             else:
#                 del self.elements[val]

#     def __contains__(self, val):
#         # returns True when val is in the multiset, else returns False
#         return val in self.elements
    
#     def __len__(self):
#         # returns the number of elements in the multiset
#         return sum(self.elements.values())
# if __name__ == '__main__':
#     def performOperations(operations):
#         m = Multiset()
#         result = []
#         for op_str in operations:
#             elems = op_str.split()
#             if elems[0] == 'size':
#                 result.append(len(m))
#             else:
#                 op, val = elems[0], int(elems[1])
#                 if op == 'query':
#                     result.append(val in m)
#                 elif op == 'add':
#                     m.add(val)
#                 elif op == 'remove':
#                     m.remove(val)
#         return result

#     q = int(input())
#     operations = []
#     for _ in range(q):
#         operations.append(input())

#     result = performOperations(operations)
    
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#     fptr.close()

##Q2.
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi*self.radius*self.radius
    
# if __name__ == '__main__':  
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input())
#     queries = []
#     for _ in range(q):
#         args = input().split()
#         shape_name, params = args[0], tuple(map(int, args[1:]))
#         if shape_name == "rectangle":
#             a, b = params[0], params[1]
#             shape = Rectangle(a, b)
#         elif shape_name == "circle":
#             r = params[0]
#             shape = Circle(r)
#         else:
#             raise ValueError("invalid shape type")
#         fptr.write("%.2f\n" % shape.area())
#     fptr.close()


##Set   
"""Set questions on hackerranks"""
"""
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
Notes:-Basically, sets are used for membership testing and eliminating duplicate entries.
Example
"""
s=set()
print(type(s))
print (set('HackerRank')) #o/p {'c', 'e', 'a', 'R', 'r', 'n', 'k', 'H'}
# Not contains duplicate entity means repition not allowed autommatic
print(set([1,2,1,2,3,4,5,6,0,9,12,22,3])) # o/p {0, 1, 2, 3, 4, 5, 6, 9, 12, 22}
print(set(set(['H','a','c','k','e','r','r','a','n','k']))) # {'H', 'a', 'e', 'r', 'c', 'n', 'k'}
print(set({'Hacker' : 'DOSHI', 'Rank' : 616 })) # {'Hacker', 'Rank'}
print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
# set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
s=set([1,2,34,4,5,5,6,6,6,7,2,1,3,8,9])
print(s) #{1, 2, 34, 4, 5, 6, 7, 3, 8, 9} remove repat element in uiquely remove duplicates.
# Q1) average find set of list input
def average(array):
    # your code goes here
    arr = set(array)
    result= sum(arr)/len(arr)
    return result

if __name__ == '__main__':
    n = int(input("Enter number")) # 10
    # map method convert all the list value to string
    arr = list(map(int, input("Enter the elements ").split())) # 161 182 161 154 176 170 167 171 170 174
    result = average(arr)
    print(result) #169.375

# If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. 
a= input("Enter a ") # 6 7 8 9 6
lis = a.split()
print (lis) # ['6', '7', '8', '9', '6']
# If the list values are all integer types, use the map() method to convert all the strings to integers.
lis = ['5', '4', '3', '2']
newlis = list(map(int, lis))
print (newlis) #[5, 4, 3, 2]

#Q Creating a set:-
myset = {1, 2} # Directly assigning values to a set
myset = set()  # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
print(myset) #{'a', 'b'}

# MODIFYING SETS
# Using the add() function:
myset.add('c')
myset.add('c')
myset.add('a') # As 'a' already exists in the set, nothing happens
myset.add((5, 4)) # {'a', 'c', 'b', (5, 4)}
#  Directly assigning values to a set
myset={'a', 'c', 'b', (5, 4)}

# Using the update() function:
myset.update([1, 2, 3, 4]) # update() only works for iterable objects
myset={'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
myset.update({1, 7, 8})
myset={'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
myset.update({1, 6}, [5, 13])
myset={'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}

# REMOVING ITEMS
# Both the discard() and remove() functions take a single value as an argument and removes that value from the set. If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.
myset.discard(10)
myset ={'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
myset.remove(13)
print(myset)
myset={'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}

# COMMON SET OPERATIONS Using union(), intersection() and difference() functions.
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
c=a.union(b) # Values which exist in a or b
print(c) #{2, 4, 5, 9, 11, 12}
d=a.intersection(b) # Values which exist in a and b
print(d) #{2, 4}
e = a.difference(b) # Values which exist in a but not in b
print(e) #{9, 5}

# The union() and intersection() functions are symmetric methods:
f=a.union(b) == b.union(a)
print(f) #True
g=a.intersection(b) == b.intersection(a)
print(g) #True
h=a.difference(b) == b.difference(a)
print(h) #False

#Q.Task Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
# Input Format
# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.
# Output Format Output the symmetric difference integers in ascending order, one per line.

# Ans-> Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def symmetric_difference():
    input = sys.stdin.read
    data = input().splitlines()

    # Read inputs
    # 'M', The size of the first set.
    M = int(data[0])
    # This contains 'M' space-seperated integers.
    set_M = set(map(int, data[1].split()))
    # 'N', The size of the second set.
    N = int(data[2])
    # This contains 'N' space-seperated integers.
    # The input lines are split and converted to set using
    set_N = set(map(int, data[3].split()))
    
    # Calculte symmetric difference using the ^ operator
    sym_diff = set_M ^ set_N
    
    # Sort the symmetric difference
    sorted_sym_diff = sorted(sym_diff)
    
    # Print the results
    for num in sorted_sym_diff:
        print(num)
        
if __name__ == '__main__':
    symmetric_difference()

#Q)sets
"""# The first line contains integers M and N separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B , respectively.
Output Format
Output a single integer, your total happiness.
Sample Input
3 2
1 5 3
3 1
5 7
Sample Output
Explanation
You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.
Hence, the total happiness is . """
# Ans->
# Read the input values.
# Use sets to store the elements of A and B.
# Iterate through the array and adjust the happiness based on the presence of elements in A or B.
# Output the final happiness.
# Here is a sample implementation:
 
# Explanation:
# Input Reading:

# n and m are read from the first line.
# The array of n integers is read from the second line.
# The sets A and B of m integers are read from the third and fourth lines respectively.
# Processing: 
# Initialize happiness to 0.
# For each integer in the array, check if it is in set A or set B and adjust the happiness accordingly.
if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    happiness = 0
    for i in array:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)

# If we want to add a single element to an existing set, we can use the .add() operation.
# It adds the element to the set and returns 'None'.
s = set('HackerRank')
s.add('H')
print(s)
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
print(s).add('HackerRank')
None
print(s)
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

"""Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of 
distinct N country stamps in her collection.
She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps.
Input Format
The first line contains an integer N , the total number of country stamps.
The next N  lines contains the name of the country where the stamp is from.
"""
# Soln=>Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
# Number of stamps
N = int(data[0]) 
# Set to store distinct country stamps
country_stamps = set()
# Iterate over the next N lines to collect country names
for i in range(1, N + 1):
    country_stamps.add(data[i])
# Output the number of distinct country stamps
print(len(country_stamps))

"""
.remove(x)
This operation removes element  from the set.
If element  does not exist, it raises a KeyError.
The .remove(x) operation returns None."""
# Example
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(5)
print(s) # set([1, 2, 3, 4, 6, 7, 8, 9])
s.remove(4)
print(s) # set([1, 2, 3, 6, 7, 8, 9])
s.remove(0)
KeyError: 0

"""
.discard(x)
This operation also removes element  from the set.
If element  does not exist, it does not raise a KeyError.
The .discard(x) operation returns None."""
# Example
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.discard(5)
print(s) # set([1, 2, 3, 4, 6, 7, 8, 9])
s.discard(4)
print(s) # set([1, 2, 3, 6, 7, 8, 9])
s.discard(0)
print(s) # None #set([1, 2, 3, 6, 7, 8, 9])
"""
.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError."""
# Example
s = set([1])
print(s.pop()) #1
print(s)
set([])
print(s.pop())
# KeyError: pop from an empty set
"""
Q.You have a non-empty set s , and you have to execute N  commands given in N lines.
The commands will be pop, remove and discard.
Input Format
The first line contains integer n , the number of elements in the set .
The second line contains n space separated elements of set . 
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N  lines contains either pop, remove and/or discard commands 
followed by their associated value.
"""
n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    d = list(input().split())
    try:
        if d[0] == 'pop':
            s.pop()
        elif d[0] == 'discard':
            s.discard(int(d[1]))
        else :
            s.remove(int(d[1]))
    except(KeyError):
        pass  
print(sum(s))

"""
.union()
The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on 
the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Task
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and 
some have subscribed to both newspapers.You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and the other set is subscribed to the 
French newspaper. The same student could be in both sets. Your task is to find the total 
number of students who have subscribed to at least one newspaper.
Input Format
The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.
Constraints
Output Format
Output the total number of students who have at least one subscription.
Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
13
Explanation:
set(map(int, input().strip().split())):
This reads the roll numbers as integers and stores them in a set, ensuring each roll number is unique.
Union Operation:
english_subscribers.union(french_subscribers) combines the two sets, giving us a set of all students who have subscribed to at least one newspaper.
Print the Result:
len(all_subscribers) gives the total count of unique students, which is then printed
"""
# Read input from stdin
n = int(input().strip())  # Number of students who have subscribed to English newspaper
english_subscribers = set(map(int, input().strip().split())) 
b = int(input().strip())  # Number of students who have subscribed to French newspaper
french_subscribers = set(map(int, input().strip().split()))
# Calculate the union of both sets
all_subscribers = english_subscribers.union(french_subscribers)
# Output the number of students who have subscribed to at least one newspaper
print(len(all_subscribers))
"""
Q. intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only
operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

"""
s = set("Hacker")
print(s.intersection("Rank"))
set(['a', 'k'])
# Enter your code here. Read input from STDIN. Print output to STD
# Read input from stdin
n = int(input().strip())  # Number of students who have subscribed to English newspaper
english_subscribers = set(map(int, input().strip().split())) 
b = int(input().strip())  # Number of students who have subscribed to French newspaper
french_subscribers = set(map(int, input().strip().split()))
# Calculate the intersetion of both sets
both_subscribers = english_subscribers.intersection(french_subscribers)
# Output the number of students who have subscribed to both
print(len(both_subscribers))

"""Q.difference()
The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).
s = set("Hacker")
print(s.difference("Rank"))
set(['c', 'r', 'e', 'H'])
"""
# Read input from stdin
n = int(input().strip())  # Number of students who have subscribed to English newspaper
english_subscribers = set(map(int, input().strip().split())) 
b = int(input().strip())  # Number of students who have subscribed to French newspaper
french_subscribers = set(map(int, input().strip().split()))
# Calculate the difference of both
both_subscribers = english_subscribers.difference(french_subscribers)
# Output the number of students who have subscribe only english subscriber
# Output the total number of students who are subscribed to the English newspaper only.
print(len(both_subscribers))

"""Q. symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and
the iterable but not both.Sometimes, a ^ operator is used in place of the .symmetric_difference() 
tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).
s = set("Hacker")
print(s.symmetric_difference("Rank"))
# set(['c', 'e', 'H', 'n', 'R', 'r'])
print(s ^ set("Rank"))
# set(['c', 'e', 'H', 'n', 'R', 'r'])
"""
# Read input from stdin
n = int(input().strip())  # Number of students who have subscribed to English newspaper
english_subscribers = set(map(int, input().strip().split())) 
b = int(input().strip())  # Number of students who have subscribed to French newspaper
french_subscribers = set(map(int, input().strip().split()))
# Calculate the difference of both
both_subscribers = english_subscribers.symmetric_difference(french_subscribers)
# Output total number of students who have subscriptions to the English or 
# the French newspaper but not both.
print(len(both_subscribers))

"""
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some
specific mutation operations on set A .
Your task is to execute those operations and print the sum of elements from set A .
Input Format
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

Output Format
Output the sum of elements in set A.
Sample Input
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output
38
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of elements in set A
num_elements_A = int(input().strip())
 
# Read the elements of set A
A = set(map(int, input().strip().split()))
 
# Read the number of other sets
N = int(input().strip())
 
# Perform the operations
for _ in range(N):
    # Read the operation and length of the other set (length is not needed)
    operation, _ = input().strip().split()
    # Read the elements of the other set
    other_set = set(map(int, input().strip().split()))
    # Perform the appropriate operation
    if operation == 'update':
        A.update(other_set)
    elif operation == 'intersection_update':
        A.intersection_update(other_set)
    elif operation == 'difference_update':
        A.difference_update(other_set)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
 
# Output the sum of elements in set A
print(sum(A))

""" 
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format
The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.
"""
#Q. Enter your code here. Read input from STDIN. Print output to ST
T = int(input().strip())
for _ in range(T):
    # Read Set A
    n = int(input().strip())
    set_A = set(map(int, input().strip().split()))
    # Read Set B
    m = int(input().strip())
    set_B = set(map(int, input().strip().split()))
    # check if A is a subset of B and print the result
    print(set_A.issubset(set_B))
    
#Q. Enter your code here. Read input from STDIN. Print output to S
# Read the element of set A
A = set(map(int, input().strip().split()))
# Read the number of set
n = int(input().strip())
# Initialize a flag to True
is_strict_subset = True
# check for strict superset codition for each set 
for _ in range(n):
    other_set = set(map(int, input().strip().split()))
    # check if A is a strict superset of this set
    if not (A.issuperset(other_set) and A != other_set):
        is_strict_subset = False
        break
# print the result
print(is_strict_subset)

# -------------------------------------------------------------Collections Basic Easy--------------------------------------
"""
Collections refers to module in standard library that provides specialized container data types.
These data types bulit containers like lists dictonaries, tuples, and sets. three main categry are 
sequences map and sets.
Counters,OrderedDict,DefaultDict,ChainMap,NamedTuple,DeQue,UserDict,UserList,UserString are content of collections
# A Python program to show different 
# ways to create Counter 
from collections import Counter  
# With sequence of items  
print(Counter(['B','B','A','B','C','A','B','B','A','C'])) 
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2})) 
# with keyword arguments 
print(Counter(A=3, B=5, C=2))

collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored
as dictionary values.
from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))
# o/p = ({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
print(Counter(myList).items())
# o/p = [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
print Counter(myList).keys()
# o/p = [1, 2, 3, 4, 5]
print(Counter(myList).values())
# o/p = [3, 4, 4, 2, 1]

Q.Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size
desired by the customer and , the price of the shoe.
"""
from collections import Counter
# Read the number of shoes
X = int(input().strip()) 
# Read the shoe sizes and create a Counter (multiset)
shoe_sizes = Counter(map(int, input().strip().split())) 
# Read the number of customers
N = int(input().strip()) 
# Initialize earnings
earnings = 0
# Process each customer
for _ in range(N):
    size, price = map(int, input().strip().split())
    # If the size is available, sell the shoe
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1  # Reduce the stock of this shoe size
# Print the total earnings
print(earnings)

"""
Q.DefaultDict
The first line contains integers,N  and M separated by a space.
The next  lines contains the words belonging to group A.
The next  lines contains the words belonging to group B.
"""
from collections import defaultdict
 
# Read n and m
n, m = map(int, input().strip().split())
 
# Create a defaultdict with list as default factory
a_positions = defaultdict(list)
 
# Read group A and store the positions of each word
for i in range(1, n + 1):
    word = input().strip()
    a_positions[word].append(i)
 
# Read group B and output the corresponding positions
for _ in range(m):
    word = input().strip()
    if word in a_positions:
        print(" ".join(map(str, a_positions[word])))
    else:
        print("-1")
"""
namedtuple()
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.
"""
from collections import namedtuple
 
# Read the number of students
N = int(input().strip())
 
# Read the column names and create a namedtuple
columns = input().strip().split()
Student = namedtuple('Student', columns)
 
# Initialize a variable to hold the total marks
total_marks = 0
 
# Read each student's data, convert it to a namedtuple and accumulate the marks
for _ in range(N):
    student = Student(*input().strip().split())
    total_marks += int(student.MARKS)
 
# Calculate the average marks
average_marks = total_marks / N
 
# Print the average marks rounded to 2 decimal places
print(f"{average_marks:.2f}")

"""without namedtuples """
# Read the number of students
N = int(input().strip())
 
# Read the column names and split into a list
columns = input().strip().split()
 
# Find the index of the "MARKS" column
marks_index = columns.index("MARKS")
 
# Initialize the sum of marks
total_marks = 0
 
# Iterate over each student's data
for _ in range(N):
    data = input().strip().split()
    total_marks += int(data[marks_index])
 
# Calculate the average marks
average_marks = total_marks / N
 
# Print the average marks rounded to 2 decimal places
print(f"{average_marks:.2f}") 

"""
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were 
inserted first. If a new entry overwrites an existing entry, the original insertion 
position is left unchanged.
"""
from collections import OrderedDict
 
# Read the number of items
N = int(input().strip())
 
# Initialize an OrderedDict to store items and their net prices
items = OrderedDict()
 
# Read each item and update the OrderedDict
for _ in range(N):
    # Read the item name and price, split by space
    entry = input().strip().rsplit(' ', 1)
    item_name = entry[0]
    price = int(entry[1])
    
    # If the item already exists, update its net price
    if item_name in items:
        items[item_name] += price
    else:
        # Otherwise, add the item to the OrderedDict
        items[item_name] = price
 
# Print the items and their net prices in the order of their first occurrence
for item_name, net_price in items.items():
    print(item_name, net_price)
"""
A deque is a double-ended queue. It can be used to add or remove elements from both ends.
Deques support thread safe, memory efficient appends and pops from either side of the deque 
with approximately the same  performance in either direction.
Click on the link to learn more about deque() methods O(1).
Click on the link to learn more about various approaches to working with deques: Deque Recipes.
"""
from collections import deque
# Initialize an empty deque
d = deque()
 
# Read the number of operations
N = int(input().strip())
 
# Perform each operation
for _ in range(N):
    operation = input().strip().split()
    method = operation[0]
    
    # Check if the operation has a value and call the respective method
    if len(operation) > 1:
        value = int(operation[1])
        getattr(d, method)(value)
    else:
        getattr(d, method)()
# Print the elements of deque separated by space
print(' '.join(map(str, d)))

# ----------------------------------------------------------------Date and Time------------------------------
"""
Calendar Module
The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
example:-
import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2024))
"""
import calendar

# Read the input
month, day, year = map(int, input().split())
 
# Get the day of the week (0=Monday, 6=Sunday)
day_of_week = calendar.weekday(year, month, day)
 
# Get the corresponding day name and convert it to uppercase
day_name = calendar.day_name[day_of_week].upper()
 
# Print the result
print(day_name) # WEDNESDAY

# _________________________________________Error and Exceptions________________________________
"""
Exceptions
Errors detected during execution are called exceptions.
Examples:
(1)ZeroDivisionError
This error is raised when the second argument of a division or modulo operation is zero.
(2)ValueError
This error is raised when a built-in operation or function receives an argument that has the 
right type but an inappropriate value.
(3)Handling Exceptions
The statements try and except can be used to handle selected exceptions. A try statement may 
have more than one except clause to specify handlers for different exceptions.
#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
    
Q.Task
You are given two values a and b.
Perform integer division and print a/b.
Input Format
The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.
"""
T = int(input().strip())
for _ in range(T):
    try:
        a, b = map(int, input().strip().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
        
"""Q.You are given a string S.
Your task is to find out whether S is a valid regex or not.
Input Format
The first line contains integer T, the number of test cases.
The next T lines contains the string S.
"""
import re
T = int(input().strip())
for i in range(T):
    S= input().strip()
    if any(op + '+' in S for op in ['*', '+', '?']):
        print("False")
    else:
        try:
            re.compile(S)
            print('True')
        except re.error:
            print('False')

# ------------------------------------------------Buit-ins-------------------------------------------------------
"""zip([iterable, ...])
This function returns a list of tuples. The ith tuple contains the ith element from each of the argument 
sequences or iterables.
If the argument sequences are of unequal lengths, then the returned list is truncated to the length of 
the shortest argument sequence.
print(zip([1,2,3,4,5,6],'Hacker'))
# o/p = [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
"""
"""Q.input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)). 
# Enter your code here. Read input from STDIN. Print output to \
# Read the input values for z and k
x, k = map(int, input().split())
 
# Read the polynomial expression P
P = input().strip()
 
# Evaluate the polynomial expression at x
result = eval(P)
 
# Check if the evaluated result equals k and print the result
print(result == k)
"""
"""Q.The eval() expression is a very powerful built-in function of Python. It helps in evaluating 
an expression. The expression can be a Python statement, or a code object.
For example:
eval("9 + 5")
14
x = 2
eval("x + 3")
5
Here, eval() can also be used to work with Python keywords or defined functions and variables. 
These would normally be stored as strings.
print(type(eval("len")))
<type 'builtin_function_or_method'>
Without eval()
type("len")
<type 'str'>

Q.Task
You are given an expression in a line. 
Read that line as a string variable, such as var, and print the result using eval(var).

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the input expression as a string
expression = input().strip()
 
# Evaluate the expression and print the result
eval(expression)

Q.any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.
Example:-any([1>0,1==0,1<0]) o/p = True

Q.all()
This expression returns True if all of the elements of the iterable are true. 
If the iterable is empty, it will return True.
Code
all(['a'<'b','b'<'c']) o/p = True

Q.You are given a space separated list of integers. If all the integers are positive, 
then you need to check if any integer is a palindromic integer.
Input Format

The first line contains an integer N.N is the total number of integers in the list.
The second line contains the space separated list of N integers.
"""
# Read the number of integers N
N = int(input())
 
# Read the list of integers
numbers = input().split()
 
# Condition 1: Check if all integers are positive
all_positive = all(int(num) > 0 for num in numbers)
 
# Condition 2: Check if any integer is a palindromic integer
any_palindromic = any(num == num[::-1] for num in numbers)
 
# Output the result based on the two conditions
print(all_positive and any_palindromic)

# --------------------------------------------Python Function-------------------------------------------
"""Q.The map() function applies a function to every member of an iterable and returns the result.
It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length 
of each name.
print(list(map(len, ['Tina', 'Raj', 'Tom'])))  
o/p = [4, 3, 3]
Q.Lambda is a single expression anonymous function often used as an inline function.In simple words,
it is a function that has only one line in its body. It proves very handy in functional and GUI programming.
sum = lambda a, b, c: a + b + c
sum(1, 2, 3)
6
Note:
Lambda functions cannot use the return statement and can only have a single expression. Unlike def,
which creates a function and assigns it a name, lambda creates a function and returns the function itself.
Lambda can be used inside lists and dictionaries.
cube = lambda x: x**3
"""

# -----------------------------------------------Regex and Parsing--------------------------------------------
"""
Detect Floating Point Number
re.split(,.)
(Q)group()
A group() expression returns one or more subgroups of the match.
"""
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(0)) # o/p= 'username@hackerrank.com'
"""
(Q)groups()
A groups() expression returns a tuple containing all the subgroups of the match.
"""
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.groups()) # ('username', 'hackerrank', 'com')  
"""
(Q)groupdict()
A groupdict() expression returns a dictionary containing all the named subgroups of the match, 
keyed by the subgroup name.
"""
import re
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict()) # {'user': 'myname', 'website': 'hackerrank', 'extension': 'com'}

"""
(Q)re.findall()
The expression re.findall() returns all the non-overlapping matches of patterns in a string as a
list of strings."""
import re
re.findall(r'\w','http://www.hackerrank.com/') # ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k

"""
(Q)re.finditer()
The expression re.finditer() returns an iterator yielding MatchObject instances over all 
non-overlapping matches for the re pattern in the string.
Code"""
import re
re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

"""
(Q.)start() & end()
These expressions return the indices of the start and end of the substring matched by the group.
"""
import re
m = re.search(r'\d+','1234')
print(m.end())
# 4
print(m.start())
# 0
"""
(Q) A single line of input containing a string of Roman characters
"""
import re
# Roman numeral validation pattern
pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$" 
# Read the input string
S = input().strip()
# Validate the string using the pattern
if re.match(pattern, S):
    print(True)
else:
    print(False)

""")For mobile no start 789"""
import re
# Read the number of inputs
N = int(input().strip())
# Define the regex pattern for a valid mobile number
pattern = r'^[789]\d{9}$'
# Process each input
for _ in range(N):
    number = input().strip()
    # Check if the number matches the pattern
    if re.match(pattern, number):
        print("Yes")
    else:
        print("No")
"""Email"""
import re
import email.utils
# Define the regex pattern for a valid email
pattern = r'^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$' 
# Read the number of email addresses
n = int(input().strip())
# Process each email address
for _ in range(n):
    full_email = input().strip()
    name, email_addr = email.utils.parseaddr(full_email)  
    # Validate the email using regex
    if re.match(pattern, email_addr):
        print(full_email)
 
"""(Q)Task"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
# Read the input string
S = input().strip()
# Define the regex pattern for finding the substrings
pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])' 
# Find all matches in the string S
matches = re.findall(pattern, S)
# If matches were found, print them, otherwise print -1
if matches:
    for match in matches:
        print(match)
else:
    print(-1)
    
# --------------------------------------------------------NUMPY---------------------------------------------
"""
The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data."""
"""Q.Task
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
"""
import numpy as np
def arrays(arr):
    # Convert list of strings to a NumPy array with type float
    array = np.array(arr, dtype=float)
    # Reverse the array
    reversed_array = array[::-1]
    return reversed_array 
# Read input, strip any extra spaces, and split by spaces
arr = input().strip().split()
# Get the result by calling the arrays function
result = arrays(arr)
# Print the result
print(result)

"""(Q)shape
The shape tool gives a tuple of array dimensions and can be used to
change the dimensions of an array.
"""
# (a). Using shape to get array dimensions
import numpy
my__1D_array = numpy.array([1, 2, 3, 4, 5])
print(my__1D_array.shape)     #(5,) -> 1 row and 5 columns
my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(my__2D_array.shape)     #(3, 2) -> 3 rows and 2 columns 

# (b). Using shape to change array dimensions
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print(change_array)  

"""(Q)reshape
The reshape tool gives a new shape to an array without changing its data.
It creates a new array and does not modify the original array itself.
"""
rs=numpy.array([1,2,3,4,5,6])
print(rs.reshape(3,2))
"""(Q)Task
You are given a space separated list of nine integers. Your task is to convert this list into
a 3X3 NumPy array.
Input Format
A single line of input containing  space separated integers."""
import numpy as np
def create_3x3_array(arr):
    # Convert the list of strings to integers and then to a NumPy array
    array = np.array(arr, dtype=int)
    # Reshape the array to a 3x3 matrix
    reshaped_array = array.reshape(3, 3)
    return reshaped_array
# Read input, strip any extra spaces, and split by spaces
input_list = list(map(int, input().strip().split()))
# Get the 3x3 array by calling the create_3x3_array function
result = create_3x3_array(input_list)
# Print the result
print(result)

"""(Q.)Transpose
We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array.
"""
import numpy
my_array = numpy.array([[1,2,3],[4,5,6]])
print(numpy.transpose(my_array))
# #Output
# [[1 4]
#  [2 5]
#  [3 6]]

"""
(Q)Flatten
The tool flatten creates a copy of the input array flattened to one dimension.
"""
import numpy
my_array = numpy.array([[1,2,3],[4,5,6]])
print(my_array.flatten())
#Output=  [1 2 3 4 5 6]

"""Task
You are given a X integer array matrix with space separated elements ( N= rows and M = columns).
Your task is to print the transpose and flatten results.
Input Format
The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of  Mcolumns.
Output Format
First, print the transpose array and then print the flatten.
"""
import numpy as np
 
# Read the dimensions of the matrix
n, m = map(int, input().strip().split())
 
# Read the matrix data
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)
 
# Convert list of lists to NumPy array
array = np.array(matrix)
 
# Print the transpose of the array
transpose = np.transpose(array)
print(transpose)
 
# Print the flattened version of the array
flattened = array.flatten()
print(flattened)

"""Q.Concatenate
Two or more arrays can be concatenated together using the concatenate function with a 
tuple of the arrays to be joined:
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])
print numpy.concatenate((array_1, array_2, array_3))    
#Output
[1 2 3 4 5 6 7 8 9]
"""
import numpy as np
 
# Read the dimensions
N, M, P = map(int, input().strip().split())
 
# Read the first array
array1 = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    array1.append(row)
 
# Read the second array
array2 = []
for _ in range(M):
    row = list(map(int, input().strip().split()))
    array2.append(row)
 
# Convert lists to NumPy arrays
array1_np = np.array(array1)
array2_np = np.array(array2)
 
# Concatenate along axis 0
result = np.concatenate((array1_np, array2_np), axis=0)
 
# Print the result
print(result)

"""(Q)zeros
The zeros tool returns a new array with a given shape and type filled with 0's.
import numpy
print(numpy.zeros((1,2)))                    #Default type is float
#Output : [[ 0.  0.]] 
print(numpy.zeros((1,2), dtype = numpy.int)) #Type changes to int
#Output : [[0 0]]

(Q)ones
The ones tool returns a new array with a given shape and type filled with 1's.
import numpy
print(numpy.ones((1,2)))                    #Default type is float
#Output : [[ 1.  1.]] 
print(numpy.ones((1,2), dtype = numpy.int)) #Type changes to int
#Output : [[1 1]]   
# """

"""
(Q)identity:-
The identity tool returns an identity array. An identity array is a square matrix with all the main 
diagonal elements as 1 and the rest as 0. The default type of elements is float.
import numpy
print(numpy.identity(3)) #3 is for  dimension 3 X 3
#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
 
eye

The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, 
upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative 
is for the lower, and a   (default) is for the main diagonal.

import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.
#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]
"""

"""(Q)Array Mathmatic
Basic mathematical functions operate element-wise on arrays. They are available both as operator 
overloads and as functions in the NumPy module.
import numpy
a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]

print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
"""
import numpy as np
 
# Read dimensions
N, M = map(int, input().strip().split())
 
# Initialize empty arrays for A and B
A = np.array([input().strip().split() for _ in range(N)], dtype=int)
B = np.array([input().strip().split() for _ in range(N)], dtype=int)
 
# Perform operations
addition = np.add(A, B)
subtraction = np.subtract(A, B)
multiplication = np.multiply(A, B)
floor_division = np.floor_divide(A, B)
modulus = np.mod(A, B)
power = np.power(A, B)
 
# Print results
print(addition)
print(subtraction)
print(multiplication)
print(floor_division)
print(modulus)
print(power)

"""
(Q)floor
The tool floor returns the floor of the input element-wise.The floor of  is the largest integer  where .
import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

(Q)ceil
The tool ceil returns the ceiling of the input element-wise.
The ceiling of  is the smallest integer  where .

import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

(Q)rint
The rint tool rounds to the nearest integer of input element-wise.
import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.
"""
# sum
"""(Q)sum
The sum tool returns the sum of array elements over a given axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
By default, the axis value is None. Therefore, it performs a sum over 
all the dimensions of the input array.

(Q)prod
The prod tool returns the product of array elements over a given axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
By default, the axis value is None. Therefore, it performs the product over all the
dimensions of the input array.
"""

# Min & Max
"""(Q)min
The tool min returns the minimum value along a given axis.
import numpy
my_array = numpy.array([[2, 5], [3, 7],[1, 3],[4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

(Q)max
The tool max returns the maximum value along a given axis.
import numpy
my_array = numpy.array([[2, 5], [3, 7],[1, 3],[4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.
"""
# Mean
"""(Q)mean
The mean tool computes the arithmetic mean along the specified axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
By default, the axis is None. Therefore, it computes the mean of the flattened array.

(Q)var
The var tool computes the arithmetic variance along the specified axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
By default, the axis is None. Therefore, it computes the variance of the flattened array.

(Q)std
The std tool computes the arithmetic standard deviation along the specified axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.
"""

# dot and cross
"""(Q)dot
The dot tool returns the dot product of two arrays.
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print(numpy.dot(A, B))       #Output : 11

(Q)cross
The cross tool returns the cross product of two arrays.
import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print(numpy.cross(A, B))     #Output : -2
"""
# Inner
"""(Q)inner
The inner tool returns the inner product of two arrays.
import numpy
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print numpy.inner(A, B)     #Output : 4

(Q)outer
The outer tool returns the outer product of two arrays.
import numpy
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
"""
# ------------------------------------Math and Itertools------------------------------------------------
# Math and itertools
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*((10**i)//9))
"""(Q)Polar coordinates are an alternative way of representing Cartesian 
coordinates or Complex Numbers.
A complex number  z = x + yi

is completely determined by its real part X and imaginary part y.
Here,  is the imaginary unit.
A polar coordinate (r,0)
is completely determined by modulus r and phase angle 0.
r=(x**2+y**2)**1/2
python_module=cmath.phase

(Q)Task
You are given a complex z. Your task is to convert it to polar coordinates.
"""
import cmath
# Read the complex number from input
z = complex(input().strip())
# Calculate the magnitude
r = abs(z)
 # Calculate the phase
p = cmath.phase(z)
# Output the results
print(r)
print(p)

"""Itertools product
itertools.product()
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
"""
import itertools 
# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# Compute Cartesian product
cartesian_product = list(itertools.product(A, B))
# Print the result in tuple  form
print(*cartesian_product) # print each tuple in the cartesian product with tuples seperated by space

"""(Q)itertools.permutations(iterable[, r])
This tool returns successive r length permutations of elements in an iterable.
 print(list(permutations('abc',3)))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
"""
"""(Q)itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable
is sorted, the combination tuples will be produced in sorted order.
from itertools import combinations
print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
"""
