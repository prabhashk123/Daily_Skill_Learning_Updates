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

"""Q How to interchange first and last element list in python """
# lst=[]
# n=int(input("Enter the number of element in List :"))
# for i in range(0,n):
#     element=int(input("Enter element "+str(i+1) + ":"))
#     lst.append(element)
# print("lst =" ,lst)
"""Swap the lst element first and last interchange"""
# lst[0],lst[len(lst)-1]=lst[len(lst)-1],lst[0]
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
# with open("Pythons//Problems//file.text") as f:
#     line=f.read()
#     print(line)
# M-2
# f=open("Pythons//Problems//file.text")
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
#         if i%3==0 and 1%5 ==0: #i%15 ==0
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
# make one decorator
# make lambda function
# input :[29,02,2024] convert
# output: 29-02-2024
"""Here's how to convert the input list [29, 02, 2024] to the
 formatted string "29-02-2024" in Python:"""
# from datetime import date
# Create a date object from the list
# date_obj = date(2024, 2, 29)
# # Format the date as desired
# formatted_date = date_obj.strftime("%d-%m-%Y")
# print(formatted_date)

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
str1= "Prabhash kumar"
print(type(str1.split(" ")))
print(type(str1)) # o/p ['Prabhash', 'kumar']


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
    for i in range(2, int(num**0.5+1)): 
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


         

















    
