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
# for i in range(10):
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





