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
