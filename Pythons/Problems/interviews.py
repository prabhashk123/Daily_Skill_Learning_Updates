"""Q.How to find square root in python"""
# Simple square root
# n=float(input("Enter the number "))
# sqr_root=n ** 0.5
# print(f"Square root of {n} is ", sqr_root) 

# Square root of complex number
# import cmath #import complex math module using sqrt function
# n=float(input("Enter the number "))
# n=1+2j
# sqr_root=cmath.sqrt(n)
# print(f"Square root of {n} is ", sqr_root.real,sqr_root.imag) 

"""Q create list using loops in python """
# lst=[]
# n=int(input("Enter the number of element in List :"))
# for i in range(0,n):
#     element=int(input("Enter element "+str(i+1) + ":"))
#     lst.append(element)
# print("lst =" ,lst)
"""Swap the lst element first and last interchange"""
# lst[0],lst[len(lst)-1]=lst[len(lst)-1],lst[0]
# print("new lst =" ,lst)
# 2nd method
# lst[0],lst[-1]=lst[-1],lst[0]
# print("new lst =" ,lst)

"""How to check leap year in python"""
# divided by 100 is a centuary year.
# divided by 400 is a leap year of centuary year.
# year=int(input("Enter the yaer :"))
# if(year%400==0) and (year%100==0):
#     print("{0} is a leap year.".format(year))
#     # print("This year is a Centuary year")
# elif(year%4==0) and (year%100!=0):
#     print("{0} is a Leap year.".format(year))
# else:
#     print("{0} is not a Leap year.".format(year))

"""Q. How to check for armstrong number in python"""
"""
armstrong number is a number which is equal to the sum of 
the qubes of its own digits.for ex 153 is armostrong number
because 1^3+5^3+3^3 equal to 153.
"""
# num=int(input("Enter the number: "))
# # initialize sum
# sum=0
# # find the sum of the cube of own(each) digits
# temp=num
# while temp>0:
#     digit=temp%10 #Modulus assigns remainder from division
#     sum=sum + (digit**3) #Exponential :raise to the power
#     temp=temp//10   #Floor division:rounds down to nearest whole number

# #display the result
# if num==sum:
#     print("{} is a Armstrong number.".format(num)) 
# else:
#     print("{} is not a Armstrong number.".format(num)) 
"""Whether to check string is a Palindrome"""
"""
A palinndrome is a word , number , phrase or other sequence of
symbols that reads the same backwards as forwards 
for example: MADAM,RACECAR
"""
# # take the user input string /using split method
# my_str=input("Enter the string ")
# # make it suitable for caseless comparisions
# my_str=my_str.casefold()
# # reverse the string
# rev_str="".join(reversed(my_str))
# # rev_str=my_str[::-1] #2nd method of reverse
# # check if str is equal to its reverse
# if my_str==rev_str:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# method-3 using idexing/using loops
# def palindrome(s):
#     n=len(s)
#     for i in range(n):
#         if s[i] !=s[n-i-1]:
#             return False
#     return True
# print(palindrome("madam"))

"""How to combine 2 dataframe using pandas in python"""
# import pandas as pd
# df1=pd.DataFrame({"State":['Bihar','Mp','Punjab']})
# df2=pd.DataFrame({"City":['Saharsa','Indore','Ludhiana']})
# frames=[df1,df2]
# # Method-1 using concat
# results=pd.concat(frames)
# print(results)
# # Method-2 using append
# result=df1.append(df2)
# print(result)

"""How to read file in python"""
# M-1
# with open("Pythons//Problems//file.text",'r') as f:
#     line=f.read()
#     print(line)
# M-2
# f=open("Pythons//Problems//file.text","r")
# line=f.read()
# print(line)
# f.close()

"""Fibonic series using loop"""
# def fibonic(n):
#     a,b=0,1
#     print(a)
#     while (b<n):
#         print(b)
#         # swap var without using third variable
#         a,b=b,a+b
# fibonic(150)

"""Compress string"""
# aabbccddeeee = a2b2c2a4f3e1i3
# Input - aabbccaaaafffeiii
# Output - a2b2c2a4f3e1i3
# By using loop compress string
# def compress(s):
#     n=len(s)
#     new_s=''
#     count=1
#     for i in range(n-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             new_s=new_s+s[i]+str(count)
#             # new_s+=(s[i]+str(count))
#             count=1
#     new_s=new_s+s[n-1]+str(count)
#     return new_s
# print(compress('aabbccaaaafffeiii'))

"""Fiz/buzz/fizbuzz
if number divide by 3 than call Fizz,divide by 5 call buzz ,divide by 15 call Fizbuzz
"""
# def fizzbuzz(n):
#     for i in range(1,n+1):
#         if i%3==0 and i%5 ==0: #i%15 ==0
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         else:
#             print(i)
# fizzbuzz(20)

# By using dict
# def fizzbuzzdict(n):
#     d={3:'fizz',5:'Buzz'}
#     for i in range(1,n+1):
#         result=''
#         for k, v in d.items():
#             if i%k==0:
#                 result+=v
#         if not result:
#             result=i
#         print(result)
# fizzbuzzdict(40)

"""Q.sum of array is"""
inupt_arr=[1,2,3,4,5]
# cal sum
array_sum=sum(inupt_arr)
print("The sum of all element of array is ",array_sum)

"""Q.Sum of all value of dictionary"""
dicts={'a':10,'b':20,'c':30}
# cal sum
dict_sum=sum(dicts.values())
print("The sum of all values in dict ",dict_sum)

"""Q.Sum of all element of list"""
List=[1,2,3,4,5]
# cal sum of list
List_sum=sum(List)
print('The sum of element in list' ,List_sum)

"""Q.Sum of all element of Set"""
my_set={1,2,3,4,5}
# cal sum of Set
Set_sum=sum(my_set)
print('The sum of element in my_set' ,Set_sum)

"""Q.Sum of all element of Tuple"""
my_tuple=(1,2,3,4,5)
# cal sum of Tuple
Tuple_sum=sum(my_tuple)
print('The sum of element in my_Tuple' ,Tuple_sum)


"""Q.Swap element at position of list for ps1 and ps3"""
my_list=[1,2,3,4,5]
my_list[1],my_list[3]=my_list[3],my_list[1]
print("List after swapping element at ps1 and ps3 ",my_list)

"""Q.Iterator in Python"""
# Iterator is an object that implement the iterator protocol ,which consists
# of two method __iter__() and __next__() iterator are used to iterate over
# container like lists,tuples,dictonaries and sets
# Example
class MyIterator:
    def __init__(self,data):
        self.data=data
        self.index=0
        # __iter__ method returns the iterator object itself
    def __iter__(self):
        return self
        # __next__method returns the next element in the iterations
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value=self.data[self.index]
        self.index +=1
        return value
# Create an instance of iterator custom iterator over list
my_iterator=MyIterator([1,2,3,4,5])
# Iterate over the elements using a for loop
for item in my_iterator:
    print(item)

"""Q. Incerement and decrement operator in python
Int python no specifice increment('++') and decrement('--') operators like in 
some others in python programming use '+=' and '-=' operatoror for incrementing and decrementing
in python icrement and decrement operator are assignment operator.
"""
# # Increment example
# x=5
# x +=1 # equvalent to x=x+1
# print("After Increment x= ",x)
# # Decrement example
# x=5
# x -=1 # equvalent to x=x-1
# print("After Decrement x= ",x)

"""Accolite interview"""
# make class for statice method and class method
# What is Class Method in Python? 
# The @classmethod decorator is a built-in function decorator that is an expression 
# that gets evaluated after your function is defined. The result of that evaluation shadows your function definition. A class method receives the class as an implicit first argument, just like an instance method receives the instance 
# Syntax Python Class Method: 
class C(object):
    @classmethod
    def fun(cls, arg1, arg2,):
       pass
"""fun: function that needs to be converted into a class method
returns: a class method for function.
A class method is a method that is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. 
For example, it can modify a class variable that will be applicable to all the instances."""
class MyClass:
    def __init__(self, value):
        self.value = value
    def get_value(self):
        return self.value
# Create an instance of MyClass
obj = MyClass(10)
# Call the get_value method on the instance
print(obj.get_value())  # Output: 10

# What is the Static Method in Python?
"""A static method does not receive an implicit first argument. A static method 
is also a method that is bound to the class and not the object of the class. 
This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.
Syntax Python Static Method: """
class C(object):
    @staticmethod
    def fun(arg1, arg2,):
        pass
# returns: a static method for function fun.
# example sm
class MyClass:
    def __init__(self, value):
        self.value = value
    @staticmethod
    def get_max_value(x, y):
        return max(x, y)
# Create an instance of MyClass
obj = MyClass(10)
print(MyClass.get_max_value(20, 30))  
print(obj.get_max_value(20, 30))
# make one decorator
# make lambda function
# input :[29,02,2024] convert
# output: 29-02-2024
"""Here's how to convert the input list [29, 02, 2024] to the
 formatted string "29-02-2024" in Python:"""
from datetime import date
# Create a date object from the list
date_obj = date(2024, 2, 29)
# Format the date as desired
formatted_date = date_obj.strftime("%d-%m-%Y")
print(formatted_date)

""""""
# arr=[1,2,3,4,5]
# sum=0
# for i in arr:
#     sum=sum+i
# print(sum)
# arr=[1,2,3,4]
# result=[sum(arr[i:i+3]) for i in range(len(arr)-2)]
# print(result)

"""How to remove duplicates from list using stream in python
Ways to Remove duplicates from the list:
Below are the methods that we will cover in this article:

Using set() method
Using list comprehension 
Using list comprehension with enumerate() 
Using collections.OrderedDict.fromkeys()
Using in, not in operators
Using list comprehension and Array.index() method
Using Counter() method
Using Numpy unique method
Using a Pandas DataFrame
"""
lst=[2,3,4,5,6,4,4,3,2,8,9]
# #using sets
# print(set(lst))
# # Using for loop
# res=[]
# for i in lst:
#     if i not in res:
#         res.append(i)
# print(res)
# # Using list comprehension
# new_lst=[]
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(new_lst)
"""Using dict"""
# We get ValueError when we try to convert a simple list into a dictionary
#print(dict(lst)) #gaet value error
# # S1-Convert list into a list of tuples
lst_of_tuple=list(map(lambda x:(x,None),lst))
print(lst_of_tuple, end='\n\n')
# # S2. Convert list of tuples into a dictionary
dict_lst=dict(lst_of_tuple)
print('The resulting dictionary from the list of tuples:')
print(dict_lst, end='\n\n')
# # S3. Get the unique keys from the dictionary and convert into a list
new_lst=list(dict_lst.keys())
print('The new list without duplicates:')
print(new_lst, end='\n\n')

## Find the sum of n-terms series: 
#Q. 1 + ((1+3)/(1+2)) + ((1+3+5)/(1+2+3))....... n terms
def sumofseries(n):
    total_sum=0
    for i in range(1, n+1):
        if i==1 :
            terms = 1
        else:
           terms= (2 * i)/(i+1)
        print(terms)
        total_sum +=terms
        print(total_sum)
    return total_sum
s=sumofseries(5)
print(s)

## Create a dictonary:
emp_no = [1,2,3]
emp_name = ['Shreyas', 'Pratap', 'Prabhash' ]
emp_dict = dict(zip(emp_no,emp_name))
print(emp_dict) # o/p {1:'Shreyas', 2:'Pratap', 3:'Prabhash'}

# Add employe no in emp_no list
l2 = emp_no
l2.append(4)
print(emp_no)

##QWe have a Pandas DataFrame with a 'date' column containing dates in the format 'YYYY-MM-DD'. The goal is to extract the month from these dates and create a new column named 'month'.
import pandas as pd
df = pd.DataFrame()
df['date'] = ['2024-01-01', '2024-02-01', '2024-03-01']

# Convert the 'date' column to datetime format (if not already)
df['date'] = pd.to_datetime(df['date'])

# Extract the month and create a new column 'month'
df['month'] = df['date'].dt.month

print(df)

# How to convert string cooma sepertated value in list 
str1= "Prabhash,kumar"
str1=str1.split(",")
print(type(str1))
print(str1) # o/p = ['Prabhash', 'kumar']


## You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
st=input("enter the string ")
def swape_case(st):
    result=str.swapcase(st)
    return result
# print(swape_case(st))

## You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
line= input("Enter the line ")
def split_and_join(line):
    return line.replace(" ","-")
# print(split_and_join(line))

## Complete the 'print_full_name' function below.
first=input("Enter the first name ")
last=input("Enter the last name ")
def fullname(first,last):
    print(f"Hello {first} {last}! You just delved into python.")
result=fullname(first,last)
# print(result)

## difference mutable and immutable in python
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# Ex-convert the string to a list and then change the value.
string = "abracadabra"
# print(list(string))
# convert the list to string
l=list(string)
# 
l[5]='k'
strs="".join(l)
print(strs)

#2 Another approach is to slice the string and join it back.
# Example
string = string[:5] + "k" + string[6:]
print (string) #abrackdabra

def mutate_string(string, position, character):
    # convert string to list
    l=list(s)
    # 5th position of list is replace by character k
    l[5]="k"
    # convert list to string
    string= "".join(l)
    return string
# metod 2
    # s_new = string[:position] + character + string[(position + 1):]
    # return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

## count substring in string 
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    # strip remove the white space of string
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

## Q writa program for check number is prime or not
n=int(input("Enter the value of n = "))
def checkprimeno(n):
    if n<2:
        print("Number less thane 2 is not a prime number ")
    elif n%2==0:
        print(f"{n} is not a prime no")
    else:
        print(f"{n} is a prime no")
checkprimeno(n)

# Method-2
def is_prime(num):
# cheack if the number is less thane 2
    if num<2:
        return False
# check for factor from 2 to the square root of the number
    for i in range(2, int(num**0.5)+1): 
        if num % i==0:
            return False
# If no factor are found number is a prime number
    return True
# Input
num = int(input('Enter a number: '))
# Check if a number is a prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number. ")

# Write a program to find outy the factorial of the number
# check if the number is negative, positive or zero
def compute_factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
# take input from the user
compute_factorial(int(input("Enter a number")))

## How to generate random number in python
# generate random float number between 0 to 1 using random method
import random 
num = random.random()
print(num)
# give a random float number in specified range
num = random.uniform(1, 100)
print(num)
# give a random integer number in specified range
num = random.randint(1, 100)
print(num)
# random even Num/odd 2/3
# give a random number in a range with increments steps
num = random.randrange(0, 100, 2)
print(num)
# Random series
# gives a series of a random number
numlist = random.sample(range(0, 100), 3) # here 3 is ki total number of random number generate
print(numlist)


    
## Write return type function and Returning Different Types
def add(x, y):
  return x + y
result = add(3, 4)
print(result) # 7
print(type(result))  # Output: <class 'int'>

# A function can return different types based on conditions:
def get_value(condition):
  if condition:
    return "True condition"
  else:
    return 42
result = get_value(True)
print(type(result))  # Output: <class 'str'>
result = get_value(False)
print(type(result))  # Output: <class 'int'>
# Returning Multiple Values
# You can return multiple values using tuples:
def get_user_data():
  name = "Alice"
  age = 30
  return name, age
name, age = get_user_data()
print(type(name)) # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>

## Write simple post method in django
# csrf_token
from django.contrib.auth.models import User
def registration(request):
    name=request.POST.get("name")
    email=request.POST.get("Email")
    password=request.POST.get("password")
    user=User.objects.create_user(name=name,email=email,password=password)
    user.save()
    print(user)

## pandas
"""Requirements
1. Convert it to a pandas dataframe with column names as A, B and C
2. Add a new column 'Remove' with default value as False
3. Update the 'Remove' column to True for rows where B value is 2
4. Filter the dataframe and keep the rows where the 'Remove' value is False
5. Set a index on columns A and B"""
import pandas as pd
l1 = [[1, 2, 3], [2, 2, 4], [3, 4, 5], [4, 5, 6], [5, 2, 7]]

# 1. Convert to pandas DataFrame with column names A, B, C
df = pd.DataFrame(l1, columns=['A', 'B', 'C'])
# 2. Add a new column 'Remove' with default value as False
df['Remove'] = False
# 3. Update the 'Remove' column to True for rows where B value is 2
df.loc[df['B'] == 2, 'Remove'] = True
# 4. Filter the dataframe and keep rows where 'Remove' value is False
df = df[df['Remove'] == False]
# 5. Set a multi-index on columns A and B
df = df.set_index(['A', 'B'])
print(df)
# Add two list of data in data frame with columns and row is index.
import pandas as pd
d1 = [[1, 2, 3], [2, 2, 4], [3, 4, 5], [4, 5, 6], [5, 2, 7]]
d2 = [[1, 6, 3], [2, 2, 4], [3, 4, 5], [4, 5, 6], [5, 2, 7]]
df=pd.DataFrame([d1,d2],columns=['A','B','C','D','E'],index=['a','b'])
print(df)

"""Q.What is the difference between a module and a package?
# Module
A module in Python is simply a .py file containing Python code.
This code can be imported and used in another Python script using the import statement.
The syntax is import<module name>
 
# Package:
A package, on the other hand, is a collection of modules. It is a way of organizing related 
Python modules into a directory.
Essentially, it's a directory that contains multiple module files, along with a special file called
_init__.py, which tells Python that the directory is a package. 
"""

"""Q.What is the use of decorators in Python?
Decorators:
In Python, decorators are a special kind of function that add extra 
functionality to another function.
- They do this without changing the other function's code.

That means They provide way to wrap another function which can add functionality before or after 
the original function is called without permanently modifying it.
# Example:-
def my_decorator(func):
def wrapper():                                                                    Output:
print("Something is happening before the function is called.")          Something is happening before 
func()                                                                      the function is called.                             func()                                                                            Hello!
print("Something is happening after the function is called.")            Something is happening after                                                                       
return wrapper                                                            the function is called.
@my_decorator
def say_hello():
print("Hello!")
say_hello()
"""

"""Q.What is exception handling and how it is done in Python?
try: This keyword is used to specify a block of code that might raise an exception.
except: This keyword is used to catch and handle the exception(s) that are
encountered in the try block.
finally: This keyword is used to specify a block of code that will be executed
no matter if an exception is raised or not.
raise: This keyword is used to manually raise an exception.

try:
# Try block
    num = int(input("Enter a number: ")) # This line could raise a ValueError 
    print(f"You entered: (num}")
except ValueError:
    # Except block 
    print("That's not a valid number!")
finally:
    # Finally block
    print("This gets executed no matter what")
"""

"""Q.What is inheritance in Python?
Inheritance:
In Python, inheritance is a way we can define a new class (child class) that 
takes on attributes and methods from an existing class (parent class).

Q.What is the difference between single and multiple inheritance?
Single Inheritance is when a class inherits from a single superclass. For example:
class Parent:
def speak(self):
print("Parent speaking!")
class Child(Parent):
def talk(self):
print("Child talking!")
# Creating an object of Child
child = Child()
child.speak() #Output: Parent speaking!
child.talk() # Output: Child talking!
50:58/1:08:03 Inheritance in Python >

Multiple inheritance is when a class can inherit from more than one superclass. For example:
class Mother:
def speak(self):
print("Mother speaking!")
class Father:
def talk(self):
print("Father talking!")
class Child(Mother, Father):
pass
#Creating an object of Child
child = Child()
child.speak() # Output: Mother speaking!
child.talk() # Output: Father talking!
"""

"""Q.Explain the difference between “is” and “==" in Python.
"==" checks for value equality. It compares the values of the two objects and returns True if they are equal and False if they are not.
For example:
list1 = [1, 2, 3] 
list2 = [1, 2, 3] 
print(list1 == list2)
Output: True

But "is" checks for identity. It returns True if both variables point to the same object (not just
equal values, but the exact same instance in memory), and False otherwise.
For example: 
list1 = [1, 2, 3] 
list2 = list1 # list2 now references the same object as list1
print(list1 is list2)
Output: True
"""

# Q What are Generators? Tell about their use in Python.
"""
Generator:
    A generator in Python returns an iterator that produces sequences of values one at a time.
    We use the yield keyword to produce values. YIELD Keyword to produce value.
Usage:
    Since the generator doesn't produce all the values at the same time, it saves memory if
    we use the generator to process the sequence of values without the need to save the initial values.    
def count_up_to(n):
    num = 1 
    while num <= n: 
        yield num # This makes our function a generator 
        num += 1
# Using the generator 
for number in count_up_to(10): 
    print(number)
"""

# Q. What is Shallow Copy and Deep Copy in Python?
"""
In Python, deep copy and shallow copy are methods used to copy objects.
We use the = operator, It only creates a new variable that shares the reference of the original object.
In order to create "real copies" or "clones" of these objects, we can use the copy module in Python.
There are two types: Shallow copy and Deep copy.

- Shallow copy: A shallow copy is a copy of an object that stores the reference of the original elements.
- It makes copies of the nested objects' reference and doesn't create a copy of the nested objects. 
So if we make any changes to the copy of the object, it will reflect in the original object.
 
Deep copy: A deep copy is a process where we create a new object and add copy elements recursively. 
The independent copy is created of the original object and its entire elements Changes made in one object do not affect the other.       
"""

# Q. Explain the use of lambda expressions in Python. When is it useful?
"""
    The lambda is used to define a function without a name in Python.
    - They are useful in situations where you need a small, temporary function that
    you won't need to use elsewhere in your code.
A regular function looks like       A lambda function look like: single expression one line function
input:                              input:  
def add(x,y):                       add2 = lambda x, y: x+y
    return(x+y)                     print(add2(4,5))
print(add(4,5))                     o/p = 9
Output =                            any number of arguement map,filterf
"""

# Q.What is the use of PASS keyword in Python?
"""
Pass: Pass is a null statement that basically does nothing.
Usage: It is often used as a placeholder where a statement is required syntactically,
but no action needs to be taken. 
For example, if you want to define a function or a class but 
haven't yet decided what it should do, you can use the pass as a placeholder. 
def my_function():
    pass #TODO: implement this function"""

"""Q.Reverse of String"""
str1 = "Analytics Vidhyas"
# method 1 using string built in 
print(str1[::-1])
# Without built in function/method
str2 = ""
for i in str1: # i is each character of str1
    str2 = i + str2
    print("The origional string is: ", str1)
    print("The reversed string is: ", str2)

"""Sort a list in python by defgault ascending order from smallest to highest"""
my_list = [3, 1, 2]
# re arrange the list of item
my_list.sort()
print(my_list)

"""Delete  file in python"""
import os
f = open("txt1.txt", "x")
os.remove("txt1.txt")

"""Delete element from a list"""
# Method1
list1 = [1,2,3,4]
list1.remove(2)
print(list1)
# Method 2 base on index means here index 1 remove
list1.pop(1)
print(list1)

# Delete an entire list
list1 = [1,2,3,4]
list1.clear() # its clear all the element in list []

""" reverse an array"""
# Method -1
import numpy as np
arr1 = np.array([1,2,3,4,])
arr2 = np.flip(arr1)
print(arr2)  #[4,3,2,1]
# method 2 special slicing technique
arr2 = arr1[::-1]
print(arr2) # [4,3,2,1]

"""Access, delete,update elements in Numpy Array"""
arr1 = [1,2,3,4]
# To access element
print(arr1[0]) # 1
# To delete elemen t
x = np.delete(arr1, 0)
print(x) # [2,3,4]
# To update element
arr1[1] = 100 
print(arr1) # [1,100,3,4]

"""Concatenaste two lists"""
list1 = ['W', 'a', 'w', 'b']
list2 = ['e', 're', 'riting', 'log']
# Method  Using Zip() function pair element from two list tuple
lst3 = [x + y for x, y in zip(list1, list2)]
print(lst3)
# o/p ['We', 'are', 'writing', 'blog']

"""Square of list elements"""
# M-1 using for loop and list comperhansion
my_list=[1,2,3,4]
# Square each element using a for loop and list comprehension iterate
squared_list = [x * x for x in my_list]
print("original lisdt:", my_list)
print("Squared list:", squared_list)

"""
In Python, the map() function applies a given function to every item in an iterable
(like a list, tuple, etc.) and returns a map object (an iterator) containing the results.
Syntax:
Python
map(function, iterable)
"""
#M-2 using map() function 
# Square each element using the map() func and a lambda expression
squared_list_map = list(map(lambda x: x * x, my_list))
# Convert to list for clarity
print("Squared list using map():", squared_list_map)

"""Different b/w split & join"""
a = "This is a string"
b = a.split(' ') # ' ' it is delemeter
print(b) # o/p ['This', 'is', 'a', 'string']

c = "-".join(b)
print(c) # This-is-a-string

# print(*cartesian_product) # print each tuple in the cartesian product with tuples seperated by space

#
# How to create user define list added index 0 se start
user_list=[]
no_of_element=int(input("Enter number of element which you added ion user_list: "))
for i in range(no_of_element):
    user_list.append(i)
print(user_list)

# Iterator is an obj that allows you to iterate over collections of data 
# such as list ,tuples, dict and sets. also these are called iterable data.
# class of an object.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x, end=" ")
# out is 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

"""Generator"""
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value, end=' ')
# o/p is 1 2 3

# A Python program to demonstrate use of 
# generator object with next() 

# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
 
# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next

# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))

"""fibonic"""
def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b
# Create a generator object
x = fib(200)
# Iterate over the generator object and print each value
for i in x:
    print(i)


# Interview questions mynextfilm
# transition,signal in django
"""In Django, transactions refer to a set of operations that are executed as a single unit, ensuring data
consistency and integrity in the database. Transactions allow developers to group multiple database queries
into a single atomic operation,
using set of query atomic
from django.db import transaction
@transaction.atomic
def example_transaction():
 # Your database operations here
"""
"""Signals in Django are a notification system that allows certain “senders” to notify a set of 
“receivers” when certain actions take place."""
# background job in django
# make book model for seralizein
from rest_framework import serializers
from .import models
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Book
        fields='__all__'
        # fields=['id','user','mobile','address','profile_img','categories']
    def __init__(self,*args,**kwargs):
        super(BookSerializer,self).__init__(*args, **kwargs)
        # self.Meta.depth=1
        # nested seralizer
    def to_representation(self, instance):
        response=super().to_representation(instance)
        # response['user']=UserSerializer(instance.user).data
        return response
# what is decorator in django
"""Ans=>Decorators in Django are a powerful tool for adding additional functionality to
your views and functions. They can be used to implement common patterns such as authentication
and authorization, caching, and logging.
Authentication and authorization:
Restricting access to views based on user permissions or login status 
(e.g., @login_required, @permission_required).
Caching:
Improving the performance of views by caching their output (e.g., @cache_page).
Logging:
Tracking user actions or view execution details.
HTTP method handling:
Ensuring that a view only accepts specific HTTP methods (e.g., @require_POST).
# builtin decorator
from django.contrib.auth.decorators import login_required
@login_required
def my_view(request):
    # This view will only be accessible to logged-in users
    ...
# Custom decorator
def my_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        # Add your custom logic here
        print("Before view execution")
        response = view_func(request, *args, **kwargs)
        print("After view execution")
        return response
    return wrapper
@my_decorator
def my_view(request):
"""
# Q array
arr1=[1,2,3,4]
arr2=arr1
# : print whole element by default
arr3=arr1[:]
arr2.append(5)
print(arr3)
print(arr2)
# o/p [1, 2, 3, 4] [1, 2, 3, 4, 5]

"""Samsung RD interview"""
# What is generator func.
# how to create custom implementation of iterator
# how the normal class is different from meta class.

# lis=[1,2,3,3,5,6,7,7,7,9]
from collections import Counter
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
# Create a counter objects
res = Counter(a)
# Get count of 3
print(res[3])

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
# Count occurrences of 2
print(a.count(2))
# Count occurrences of 3
print(a.count(3))

# Macquarie (M-1)
l=[1,2,3,3,4,5,6,6,6,7]
# l=[1,2,3,3,3,4,5,6,6,6,7]
def frq(l):
    return max(set(l), key=l.count)
print(frq(l))
# M-2
from collections import Counter
def max_freq_num(lst):
    return [num for num, count in Counter(lst).items() if count == max(Counter(lst).values())]
my_list = [1,2,3,3,4,5,6,6,6,7]
print(max_freq_num(my_list))

# Deloitte
#(Q1) print("My Name Is Prabhash Kumar")
#(Q2) count each char in string
from collections import Counter
inp="My Name Is Prabhash Kumar"
# using collections.Counter() to get  
# count of each element in string  
oup = Counter(inp) 
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(inp)) 
print(Counter(inp))
# Q(2) how to run javascript on browser.
# Q(3)Multitherading how to do manage 4 thrade one by one
# Q(4)]how to same S3 bucket one time ctreation

# check out put will be 6
def check(x,y):
    if x == y:
        return False
    elif x < y :
        x,y = y,x
        if x==6 or y==6:
            return True
        elif x+y ==6:
            return True
        elif x-y==6:
            return True
        else:
            return False
    else:
        return True
print(check(-1,-7))

# For decorator
def smart_plus(funn):
    def inner(*args):
        for ele in args:
            if isinstance(ele, int):
                print(f"{ele} is integer")
            elif isinstance(ele, float):
                print(f"{ele} is float")
            elif isinstance(ele, str):
                print(f"{ele} is String")
            else:
                print("not int not float")
        return funn(*args)
    return inner
@smart_plus
def plus(*args):
    pass
plus(4,2.2,4.5, "Prabhas")

# 2nd decorator check sum type
def smart_plus(funn):
    def inner(a,b):
        add = funn(a,b)
        if isinstance(add, int):
            print(f"The result {add} is integer")
        elif isinstance(add, float):
            print(f"The result {add} is float")
        else:
            print("not int not float")
        return add
    return inner
@smart_plus
def plus(a,b):
    return a + b

"""(Q) without built in function use for  of count of each string"""
def char_count(s):
    count_dist = {}
    for char in s:
        if char in count_dist:
            count_dist[char] += 1
        else:
            count_dist[char] = 1
    return count_dist
input = 'bbbbcccaad'
output = char_count(input)
print(output)

"""(Q)Count frequency of list of strings of vowels only"""
l=["Prabhash Kumar"]
# convert list to string
strings ='.'.join(l)
vowels='aeiouAEIOU'
counts = {}
for i in strings:
    if i in vowels:
        counts[i]=counts.get(i,0)+1
print(counts)

# Method-3
l1=["Prabhash Kumar"]
l="".join(l1)
vowel='aeiouAEIOU'
d={}
for i in l:
    if i in vowel:
        if i not in d:
            d[i]=0
        d[i]+=1
print(d)

## Method-2 Using str.count() in a loop
s = "Python is fun!"
vowels = "aeiouAEIOU"
# Dictionary Comprehension
cnt = {i: s.count(i) for i in vowels if i in s}
print(cnt)

## Method-3 using Regular exp
import re
s = "Python is fun!"
p = r'[aeiouAEIOU]'
vowels = re.findall(p,s)
print(f"count: {len(vowels)}, Vowels: {vowels}")

# without built in function use for reverse of array/string
# Abstarction 
# Abstract class method ABC method
# Polymorphisam/Inheritence/Comperihensions like list
# List and Tuple which consumed memory and which Fast
# Overloading/Overridding/dynamicalliy/copy
# set/tuple/list
# print(1 to 100) using function

## Airtel Interview questions:-
"""
(1)datatypes in Python
(2)List and Tuple difference
(3)List and which cane more memory conusme=>List more beacuse dynemic but tuple fixed so less
(4)Django connect multiple database and if apply migration thane effect each database or not and how to connect
   Ans=>yes both
(5)input = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
   output = [1, 2, 5, 9]
   soln=>
    input = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    # print(set(input)) {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s=set(input)
    l=list(s)
    print([l[0],l[1],l[4],l[8]])
    # output = [1, 2, 5, 9]
"""
 
 # (Q) Merge Two Sorted List and Output will become sorted list
list1 = [1,3,5]
list2 = [2,4,6]
merge=list1.extend(list2)
print(sorted(list1))
# # output : [1,2,3,4,5,6]

# Find misssing element in list use function and comperihensiton
li=[1,2,4,5]
missing=[ele for ele in range(1,max(li)+1) if ele not in li]
print("missing ele : " + str(missing))

# Add item in list between two list item use insert() otherwist append() method
l=[1,2,3]
l.insert(1,4)
print(l)
##(Q) Find maximum number from list 
print(max(l))
# (M2) Using loops max in list
l = [1,4,2,3]
# Assuming first element is largest.
largest = a[0]
# Iterate through list and find largest
for val in l:
    if val > largest:
        # If current element is greater than largest
        # update it
        largest = val
print(largest)

# Step-2 using reduce function
from functools import reduce
l = [1, 2, 3]
# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, l)
print(largest)

# Step 3 using sort method
a=[1,2,3]
a.sort()
largest = a[-1]
print(largest)
"""(Q) How to read csv file her r+ use both read and write mode"""
try:
    flight_file=open("flight.txt","r+")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
    flight_file.close()
except:
    print("Error occurred")

# (Q) Create numpy array thane creat this array pandas using dataframe
# for numpy array 1-d 
import numpy as np
arr = np.array([1,2,3])
print(arr) # o/p = [1,2,3]
# for df using pandas
import pandas as pd
column_value=['a']
# index_values=['first']  #for 2d array use
# df = pd.DataFrame(data=arr,index=index_values,columns=column_value)
df = pd.DataFrame(data=arr,columns=column_value)
print(df)

"""# now each word complete present capital first"""
l=["Today is wednesday","Yesterday was tuesday", "Tomorrow is thursday"]
# M-1 Using List Comprehension:- by title method for list of string
capitalfirst_each_word = [i.title() for i in l]
print(capitalfirst_each_word)
# Using str method .split() and .capitalize()
capital_fl=[" ".join([word.capitalize() for word in i.split()]) for i in l]
print(capital_fl)

'''Print every 3rd element of list '''
l=[0,1,2,3,4,5,6,7,8]
# M-1 slice method
print(l[0::3])
# M-2
for i in range(0,len(l),3):
    print(l[i])
    
"""Django authenti cation"""
# built in method are:-
# Username And Password default method.,Email and Password same as prev,
# Third Pairty Library:-
# (a) Social Authentication: through like social media pf like google, FB, library ""django-allauth""
# (b) JWT(JSON Web Tokens) as json object
# (c) OAuth and OpenID Connect
# Django use HTTP Basic Authentication for testing, DRF provide OAuth2.0

"""Cal area using oops using class"""
r=int(input("value of r "))
class Circle:
    def __init__(self,r):
        self.r=r
    def cal_area(self):
        pi=3.14
        r=self.r
        return pi*r*r
c=Circle(r)
d=c.cal_area()
print("The area of circle is ",d)

"""Github Copilot, AWS"""
"""Ey Technologies Int"""
"""(Q) find greater element of each lement after """
arr = [2, 3, 1, 2, 4]
output = []
for i in range(len(arr)):
    found = False
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            output.append(arr[j])
            found = True
            break
    if not found:
        output.append(-1)
print(output) # op=[3,4,2,4,-1]

"""
(Q) In Python, you can apply multiple decorators to a single function by stacking them on top of
one another. Each decorator wraps the function it decorates, starting from the innermost to 
the outermost."""
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One: Before the function call")
        result = func(*args, **kwargs)
        print("Decorator One: After the function call")
        return result
    return wrapper
 
def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two: Before the function call")
        result = func(*args, **kwargs)
        print("Decorator Two: After the function call")
        return result
    return wrapper
 
@decorator_one
@decorator_two
def my_function(name):
    print(f"My function is called with {name}")

# Call the decorated function
my_function("John")

"""
Explanation:
Order of Execution:
The function is first passed through "decorator_two", then the result of 
that is passed through "decorator_one".
Execution happens from the "outermost decorator" (decorator_one) to the "innermost" (decorator_two) 
when the function is called.
@decorator_one: Wraps the function decorated by @decorator_two.
@decorator_two: Wraps the original my_function.
"""

class A:
    def hello(self):
        print("Hello from A")
class B:
    def hello(self):
        print("Hello from B")
class C(A, B):  # Class C inherits from A and B
    pass
# Create an instance of C
c = C()
c.hello() 
# o/p = Hello from A
# IF C(B,A)
# then o/p=Hello from B depend order of classes in heritence using 
# MRO rule check mro print(C.__mro__) or print(C.mro())
# o/p class C->A->B for C(A,B)





