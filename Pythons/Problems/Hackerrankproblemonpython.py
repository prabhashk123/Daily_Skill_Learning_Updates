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
def design(n, m):
    for i in range(n//2):
        print((((2*i)+1)*(".|.")).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n//2):
        print((((2*(n//2-i))-1)*(".|.")).center(m, "-"))
if __name__ == "__main__":
    n, m = input().split()
    design(int(n), int(m))

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
def print_formatted(number):
    # Determine the width needed for padding (width of the binary representation of `number`)
    width = len(bin(number)) - 2
 
    for i in range(1, number + 1):
        # Decimal
        dec = str(i)
        # Octal
        octal = oct(i)[2:]
        # Hexadecimal (capitalized)
        hexa = hex(i)[2:].upper()
        # Binary
        binary = bin(i)[2:]
 
        # Print each value right-aligned with the calculated width
        print(f"{dec:>{width}} {octal:>{width}} {hexa:>{width}} {binary:>{width}}")
 
# Input handling and function call
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


## Python Basic certificat of Hacker ranks
# Q1.
import math
import os
import random
import re
import sys


class Multiset:
    def __init__(self):
        self.elements = {}
        
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elements
    
    def __len__(self):
        # returns the number of elements in the multiset
        return sum(self.elements.values())
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

##Q2.
#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius*self.radius
    
if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
  