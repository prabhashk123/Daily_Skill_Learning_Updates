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
# # find the sum of the cube of each digits
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













    
