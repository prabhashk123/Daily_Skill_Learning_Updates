"""This data structure exercise is for beginners to understand and practice basic data structure 
in Python. Practice Python List, Set, Dictionary, and Tuple questions.
The data structure is widely used to hold any data. To perform any programming tasks in Python,
good knowledge of data structure is a must."""

# ---------------------------------------------------------------------------------------
"""Exercise 1: Create a list by picking an odd-index items from the first list and even index 
items from the second use slice method"""
# list1 = [3, 6, 9, 12, 15, 18, 21]
# list2 = [4, 8, 12, 16, 20, 24, 28]
# res = list()

# odd_elements = list1[1::2]
# print("Element at odd-index positions from list one")
# print(odd_elements)

# even_elements = list2[0::2]
# print("Element at even-index positions from list two")
# print(even_elements)

# print("Printing Final third list")
# res.extend(odd_elements)
# res.extend(even_elements)
# print(res)

"""Exercise 2: Remove and add item in a list
Write a program to remove the item present at index 4 and add it to
the 2nd position and at the end of the list.
Use the list methods, pop(), insert() and append()----use
"""
# list1 = [34, 54, 67, 89, 11, 43, 94]
# print("original list",list1)
# remove=list1.pop(4)
# print("List After removing element at index 4",list1)
# list1.insert(2,remove)
# print("List after Adding element at index 2 ",list1)
# list1.append(remove)
# print("List after Adding element at last ",list1)

"""Exercise 3: Slice list into 3 equal chunks and reverse each chunk
Given:
"""
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print("Original list ", sample_list)
# length=len(sample_list)
# chunk_size=int(length/3)

"""Exercise 4: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of 
each element and create a dictionary to show the count of each element."""
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list) 
count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Printing count of each item  ", count_dict)




