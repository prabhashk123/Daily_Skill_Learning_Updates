"""Write Lcm of Two number"""
"""(1)import This approach leverages the relationship between LCM and GCD 
(Greatest Common Divisor):"""
# import math
# n1=int(input("Enter first number "))
# n2=int(input("Enter second number "))

# def LCM(n1,n2):
#     """Calculates the LCM of two numbers using the GCD formula."""
#     gcd_n1n2 = math.gcd(n1,n2)
#     return abs(n1 * n2) // gcd_n1n2 # Handle negative numbers correctly
# print(f"Lcm of two number {n1} and {n2} is: ",LCM(n1,n2))

"""2. Step-by-Step Brute Force Method:"""
# def lcm_brute_force(n1,n2):
#     """Calculates the LCM of two numbers using brute force approach."""
#     max_num = max(n1, n2)
#     while True:
#         if max_num % n1 == 0 and max_num % n2 == 0:
#             return max_num
#         max_num += 1
# print(f"Lcm of lcm_brute_force of two number {n1} and {n2} is: ",lcm_brute_force(n1,n2))
"""3.using loop(iteration method)"""
# Program to display the Fibonacci sequence up to n terms
# nterms = int(input("How many terms? "))

# # First two terms
# n1, n2 = 0, 1
# count = 0

# # Check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")
# elif nterms == 1:
#     print("Fibonacci sequence up to", nterms, ":")
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         # Update values
#         n1 = n2
#         n2 = nth
#         count += 1
"""Loop method"""
# def fibonacci_iterative(n):
#   """Calculates the Fibonacci sequence using iteration."""
#   a, b = 0, 1
#   for _ in range(n):
#     yield a
#     a, b = b, a + b

# # Example usage
# for num in fibonacci_iterative(10):
#   print(num)

"""Recursion fibonaic"""
# def fibonacci_recursive(n):
#   """Calculates the Fibonacci sequence using recursion."""
#   if n <= 1:
#     return n
#   else:
#     return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
# # Example usage
# n=10
# if n<=0
    # print("Invalid")
# else:
#   for i in range(n):
#   print(fibonacci_recursive(i))
# The base cases are 0 and 1.
# For other terms, the function recursivel

"""sorted the list using python without  built in function sort() and sorted()"""
"""use nested loop Sorting in Ascending Order Without an Extra Variable:"""
# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)

# for i in range(0, len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i] >= l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
# print("Sorted List:", l1)

"""Sorting in Ascending Order Using an Extra Variable: nested loop"""
# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)
# for i in range(0, len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i] >= l1[j]:
#             temp = l1[i]
#             l1[i] = l1[j]
#             l1[j] = temp
# print("Sorted List:", l1)

"""Sorting in Descending Order (User-Provided Values):"""
# l1 = []
# n = int(input("Enter the number of elements required: "))
# for i in range(0, n):
#     element = int(input())
#     l1.append(element)

# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)

# for i in range(0, len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i] <= l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
# print("Sorted List:", l1)

"""Using sorted()"""
# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)
# l2=sorted(l1)
# print("Sorted List:", l2)

"""Using sort() # Sort the list directly using the sort() method"""
# l1 = [76, 23, 45, 12, 54, 9]
# l1.sort()
# print("Original list:", l1)
# print("Sorted list:", l1)


"""Q.Sure, here are two ways to reverse a list in Python without using built-in functions:"""
# 1. Swapping elements:
# This approach iterates through the list and swaps elements from both ends until the middle is reached. Here's the code:
# def reverse_list(data):
# #  """ Reverses a list in-place without using built-in functions.
# #   Args:
# #     data: The list to be reversed.
# #   Returns:
# #     None (the list is modified in-place)."""
#     start, end = 0, len(data) - 1
#     while start < end:
#         data[start], data[end] = data[end], data[start]
#         start += 1
#         end -= 1
# l1 = [1, 2, 3, 4, 5]
# reverse_list(l1)
# print("Reversed list:", l1)

"""Reverse slice"""
# def reverse_list(lst):
#     """
#     Reverses a list without using built-in functions.
#     Args:
#         lst (list): The input list to be reversed.
#     Returns:
#         list: The reversed list.
#     """
#     reversed_lst = lst[::-1]
#     return reversed_lst
# # Example usage:
# original_list = [1, 2, 3, 4]
# reversed_result = reverse_list(original_list)
# print("Reversed list:", reversed_result)  # Output: [4, 3, 2, 1]

"""for testing"""
# for test
# def add_lists(l1, l2):
#   """Adds two lists of digits representing numbers in reverse order.

#   Args:
#     l1: A list of digits representing a number in reverse order.
#     l2: A list of digits representing a number in reverse order.

#   Returns:
#     A list of digits representing the sum of l1 and l2 in reverse order.
#   """

#   result = []
#   carry = 0
#   for i in range(max(len(l1), len(l2))):
#     digit1 = l1[i] if i < len(l1) else 0
#     digit2 = l2[i] if i < len(l2) else 0
#     sum_of_digits = digit1 + digit2 + carry
#     carry = sum_of_digits // 10
#     result.append(sum_of_digits % 10)

#   if carry:
#     result.append(carry)

#   return result[::-1]

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# result = add_lists(l1, l2)
# print(result)  # Output: [7, 0, 8]

"""Merge two sorted list"""
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# list1 = [1,2,4]
# list2 = [1,3,4]
# s_l1=len(list1)
# s_l2=len(list2)
# res=[]
# i,j=0,0
# while i<s_l1 and j<s_l2:
#         if list1[i]<list1[j]:
#             res.append(list1[i])
#             i+=1
#         else:
#             res.append(list2[j])
#             j+=1
# res=res+list1[i:]+list2[j:]
# print(str(res))

# using sorted() method
# list1 = [1,2,4]
# list2 = [1,3,4]
# res=sorted(list1+list2)
# print(str(res))

# using extend() and sort()
# list1 = [1,2,4]
# list2 = [1,3,4]
# list1.extend(list2)
# list1.sort()
# print(str(list1))

"""Q.swap element """
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# head = [1,2,3,4]
# head[0],head[1],head[2],head[3]=head[1],head[0],head[3],head[2]
# print(head)

"""Q.Find Maximum & Minimum Elements in an Array"""
# Method1 using loop
# Input:arr[]={10,20,4}
# Output:20
# Output:4
# arr=[8,2,3,4,5]
# let first element is max
# max=arr[0]
# n=len(arr)
# for i in range(1,n):
#     if arr[i]>max:
#         max=arr[i]
# print("max element = ",max)
# let first element is min
# min=arr[0]
# n=len(arr)
# for i in range(1,n):
#     if arr[i]<min:
#         min=arr[i]
# print("min element = ",min)

"""Q. find the 2nd largest element inside in a list"""
# Method-1 for
# mylist=[70,11,20,4,100]
# # output=70
# mylist.sort()
# print(mylist) #[4,11,20,,70,100]
# print("First Largest element inside list is ",mylist[-1])
# print("Second Largest element inside list is ",mylist[-2])

#  Method-2 for convert list to set than remove first largest number   
# mylist=[70,11,20,4,100]
# new_list=set(mylist)
# new_list.remove(max(new_list))
# print(new_list) #{4,70,11,20}
# print("second largest element is ",max(new_list))

"""Q. find the smallest and largest number inside in a list"""
# mylist=[20,100,20,1,10]
# output 1,100
# method1-1 sort in asceding order
# mylist.sort()
# print(mylist) #[1,10,20,20,100]
# print("smallest number in list ",mylist[0])
# print("largest number in list ",mylist[-1])

# method-2 using built in function min and max
# print("smallest number in list using min is ",min(mylist))
# print("largest number in list using max is ",max(mylist))

"""Q. Multiplay all number in list """
# list1=[3,2,4]
# # output =24
# # Method-1 Traversal
# result=1
# for i in list1:
#     result=result * i
# print("Multiplay all number in list is",result)

"""Q.Count Occurrences of an element in a list"""
# lists=[15,6,7,10,12,20,10,28,10]
# # x=10 output=3  means 10 apperas three times
# # Method-1 using loops
# x=10
# # intiialy
# count=0
# for ele in lists:
#     if(ele==x):
#         count=count+1
# print("{} has occured {} times in list.".format(x,count))

# # Method-2 using count() built in.
# lists=[15,6,7,10,12,20,10,28,10]
# x=10
# print("{} has occured {} times in this lists.".format(x,lists.count(x)))

# Method-3 using Counter() built in.
# from collections import Counter
# lists=[15,6,7,10,12,20,10,28,10]
# x=10
# # this counter return dictonary
# dicts=Counter(lists) # {10:3 , 15:1......}
# print(dicts)
# print("{} has occured {} times in this lists.".format(x,dicts[x]))

"""Q.How To Clone or Copy a List"""
# mylist=[4,8,2,10,15,18]
# # output: mylistcopy=[4,8,2,10,15,18]
# # Method-1 slicing
# mylist_copy1=mylist[:]
# print(mylist_copy1)
# # Method-2 extend
# mylist_copy2=[]
# mylist_copy2.extend(mylist)
# print(mylist_copy2)

"""Q.How To Clear a List"""
# mylist=[4,8,2,10,15,18]
# mylist.clear()
# print("mylist =",mylist)

"""Q.How To Search an Element in a List"""
# mylist=[4,8,2,10,15,18]
# # Method-1 using Loops
# find_ele=4
# flag=0
# for i in mylist:
#     if(i==find_ele):
#         print("Element found here.")
#         flag=1
#         break
# if(flag==0):
#     print("Element not found here.")

"""Q.How To Remove Nth occurrence of the word from a List"""
# lists=["geeks","for","geeks"]
# word="geeks"
# n=3
# count=0
# for i in range(0,len(lists)):
#     if(lists[i]==word):
#         count+=1
#         if(count==n):
#             del lists[i]
# print("lists after delete nth ocuurence is =",lists)

"""Q.How To Find Factorial of A Number"""
# # inalize factorial
# factorial=1
# n=int(input("Enter the value of n "))
# if(n<0):
#     print("Factorial does not exist for negative number.")
# elif(n==0):
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         factorial=factorial * i
#     print(f"Factorial of {n} is =",factorial)

# Method-2 using function
# n=int(input("Enter the value of n "))
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# # using ternary operators
#     # return 1 if(n==0 or n==1) else n*factorial(n-1)
# print(f"Factorial of {n} is =",factorial(n))

# Method-3
# def factorial(n):
#   if n < 0:
#     raise ValueError("Factorial is not defined for negative numbers.")
#   elif n == 0 or n == 1:
#     return 1
#   else:
#     return n * factorial(n - 1)
# # Get user input and handle potential errors
# while True:
#   try:
#     n = int(input("Enter the value of n (non-negative integer): "))
#     if n >= 0:
#       break
#     else:
#       print("Error: n must be non-negative. Please try again.")
#   except ValueError:
#     print("Error: Invalid input. Please enter an integer.")

# # Calculate and print the factorial
# print(f"Factorial of {n} is =", factorial(n))

"""Q.WAP for prime numbers define in logic using function and claculate excution time"""
# import time
# def prime(n):
#     # for exexution time
#     t1=time.time()
#     print(t1)
#     for i in range(1,n):
#         for j in range(2,i//2):
#             if(i%j==0):
#                 break
#             else:
#                 print(i)
#     # for exexution time cal
#     print(time.time()-t1)
# prime(20)

"""Conccatence two tuple"""
# # Method-1 Concatenating Tuples (Creating a New Tuple):
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# combined_tuple = tuple1 + tuple2
# print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)
# # Method 2. Creating a New Tuple with Additional Elements:
# original_tuple = (10, 20)
# new_element = 30
# new_tuple = original_tuple + (new_element,)  # Notice the comma after new_element
# print(new_tuple)  # Output: (10, 20, 30)
# """Method 3. Converting to List, Modifying, and Converting Back (Not Recommended):
# It's not generally recommended to modify a tuple directly due to its immutability. 
# However, if absolutely necessary, you can temporarily convert the tuple to a list, 
# modify it, and then convert it back to a tuple."""
# original_tuple = (100, 200)
# new_element = 300
# # Convert to a list (not recommended)
# modifiable_list = list(original_tuple)
# modifiable_list.append(new_element)
# # Convert back to a tuple (not recommended)
# new_tuple = tuple(modifiable_list)
# print(new_tuple)  # Output: (100, 200, 300)
"""Zip"""
l1=[2,3,4,5]
t1=(6,7,8,9)
c=zip(l1,t1)
print(set(c))
d={}
for i in range(1,10):
    sqr=i*i
    d[i]=i*i
print(d) 




    
  



