"""Control flow statements: Use the if-else statements in Python for conditional decision-making
for loop: To iterate over a sequence of elements such as list, string.
range() function: Using a for loop with range(), we can repeat an action a specific number of times
while loop: To repeat a block of code repeatedly, as long as the condition is true.
Break and Continue: To alter the loop’s execution in a certain manner.
Nested loop: loop inside a loop is known as a nested loop"""

"""Exercise 1: Print First 10 natural numbers using while loop"""
# n=1
# while n<=10:
#     print(n,end=" ")
#     n+=1

"""Exercise 2: Print the following pattern
1             1 2 3 4 5
1 2           1 2 3 4
1 2 3         1 2 3  
1 2 3 4       1 2
1 2 3 4 5     1  
"""
# n=6
# # run outer loop 5 times
# for i in range(n):
#     # Run inner loop i+1 times
#     for j in range(1,i+1):
#         print(j,end=" ")
#     # empty line after each row
#     print("")

# n=6
# # run outer loop 5 times
# for i in range(n):
#     # Run inner loop i+1 times
#     for j in range(1,n-i):
#         print(j,end=" ")
#     # empty line after each row
#     print("")

"""Exercise 3: Calculate the sum of all numbers from 1 to a given number
For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
"""
# Solution 1 : using loop
# number=int(input("Enter the number "))
# sum=0
# for i in range(1,number+1):
#     # add current number to sum variable
#     sum+=i     
# print("")
# print("Sum is: ", sum)

# # Solution 2: Using the built-in function sum()
# n = int(input("Enter number "))
# # pass range of numbers to sum() function
# x = sum(range(1, n + 1))
# print('Sum is:', x)

"""Exercise 4: Write a program to print multiplication table of a given number"""
# number=int(input("Enter the number "))
# for i in range(1,11):
#     print(number*i,end=' ')

"""Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy 
the following conditions:-
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:
numbers = [12, 75, 150, 180, 145, 525, 50]
"""
# numbers = [12, 75, 150, 180, 145, 525, 50]
# # iterate each item of a list
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # check if number is divisible by 5
#     elif item % 5 == 0:
#         print(item)

"""Exercise 6: Count the total number of digits in a number"""
# 
# number=9570588189
# count=0
# while number!=0:
#     # floor division
#     # to reduce the last digit from number
#     number=number//10
#       # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)

# Example 2: Using inbuilt methods
# number=9570588189
# print(len(str(number)))

"""Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
# n=5
# for i in range(n):
#     for j in range(n-i,0,-1):
#         print(j,end=' ')
#     print("")
"""Exercise 8: Print list in reverse order using a loop"""
# Using a reversed() function and for loop
# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)

# Method-2  Using for loop and the len() function
# list1 = [10, 20, 30, 40, 50]
# # get list size
# # len(list1) -1: because index start with 0
# # iterate list in reverse order
# # star from last item to first
# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i])

"""Exercise 9: Display numbers from -10 to -1 using for loop reverse range"""
# for num in range(-10,0,1):
#     print(num,end=' ')
"""Use else block to display a message “Done” after successful execution of for loop"""
# for i in range(5):
#     print(i,end=' ')
# else:   
#     print("\n\n"+"done!")
"""Write a program to display all prime numbers within a range"""
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")
# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num >= 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num,end=' ')

"""Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is
found by adding up the two numbers before it. The first two numbers are 0 and 1.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34."""
# first two numbers
# num1, num2 = 0, 1
# print("Fibonacci sequence:")
# # run loop 10 times
# for i in range(10):
#     # print next number of a series
#     print(num1, end="  ")
#     # add last two numbers to get next number
#     res = num1 + num2
#     # update values,swipe
#     num1 = num2
#     num2 = res
"""Exercise 13: Find the factorial of a given number"""
# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     # run loop 5 times
#     for i in range(1, num + 1):
#         # multiply factorial by current number
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

"""Reverse a given integer number"""
# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)

"""Exercise 15: Use a loop to display elements from a given
list present at odd index positions.
Use list slicing. Using list slicing, we can access a range of elements from a list"""
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # stat from index 1 with step 2( means 1, 3, 5, an so on for odd use slice method)
# for i in my_list[1::2]:
#     print(i, end=" ")

"""Exercise 16: Calculate the cube of all numbers from 1 to a given number"""
# input_number = 6
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))

"""Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, 
if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690"""
# n = 5
# # first number of sequence
# start = 2
# sum_seq = 0
# # run loop n times
# for i in range(0, n):
#     print(start, end="+")
#     sum_seq += start
#     # calculate the next term
#     start = start * 10 + 2
# print("\nSum of above series is:", sum_seq)

"""Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*"""
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


    







