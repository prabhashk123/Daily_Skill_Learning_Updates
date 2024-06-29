"""Exercise 1A: Create a string made of the first, middle and last character"""
# strs='James'
# print(strs[0]+strs[len(strs)//2]+strs[-1])

"""Exercise 3: Create a new string made of the first, middle, and last characters of each 
input string"""
# def mix_string(s1, s2):
#     # get first character from both string
#     first_char = s1[0] + s2[0]
#     # get middle character from both string
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
#     # get last character from both string
#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
#     # add all
#     res = first_char + middle_char + last_char
#     print("Mix String is ", res)
# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)

"""Exercise 4: Arrange string characters such that lowercase letters should come first"""
# str1 = "PYnAtivE"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         # add lowercase characters to lower list
#         lower.append(char)
#     else:
#         # add uppercase characters to lower list
#         upper.append(char)
# # Join both list
# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)

"""Exercise 5: Count all letters, digits, and special symbols from a given string
Given:"""
# def find_digits_chars_symbols(sample_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
#     for char in sample_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         # if it is not letter or digit then it is special symbol
#         else:
#             symbol_count += 1
#     print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)
# sample_str = "P@yn2at&#i5ve"
# print("total counts of chars, Digits, and symbols \n")
# find_digits_chars_symbols(sample_str)

"""Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the 
first char of s1, then the last char of s2, Next, the second char of s1 and second last 
char of s2, and so on. Any leftover chars go at the end of the result."""
# s1 = "Abc"
# s2 = "Xyz"

# # get string length
# s1_length = len(s1)
# s2_length = len(s2)

# # get length of a bigger string
# length = s1_length if s1_length > s2_length else s2_length
# result = ""

# # reverse s2
# s2 = s2[::-1]

# # iterate string 
# # s1 ascending and s2 descending
# for i in range(length):
#     if i < s1_length:
#         result = result + s1[i]
#     if i < s2_length:
#         result = result + s2[i]
# print(result)

"""Exercise 9: Calculate the sum and average of the digits present in a string"""
# input_str = "PYnative29@#8496"
# total = 0
# cnt = 0
# for char in input_str:
#     if char.isdigit():
#         total += int(char)
#         cnt += 1
#         print(char,end=' ')
#         # print(cnt,end=' ')
# # average = sum / count of digits
# avg = total / cnt
# print("Sum is:", total, "Average is ", avg)

# Solution 2: Use regular expression
# import re
# input_str = "PYnative29@#8496"
# digit_list = [int(num) for num in re.findall(r'\d', input_str)]
# print('Digits:', digit_list)
# # use the built-in function sum
# total = sum(digit_list)
# # average = sum / count of digits
# avg = total / len(digit_list)
# print("Sum is:", total, "Average is ", avg)

"""Exercise 10: Write a program to count occurrences of all characters within a string
In the body of a loop, use the count() function to find how many times a current character 
appeared in a string"""
# str1 = "Apple"
# # create a result dictionary
# char_dict = dict()
# for char in str1:
#     count = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = count
# print('Result:', char_dict)

"""Exercise 12: Find the last position of a given substring"""
str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Original String is:", str1)
# # Use the string function rfind()
# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at index:", index)

"""Exercise 13: Split a string on hyphens"""
# str1 = "Emma-is-a-data-scientist"
# print("Original String is:", str1)
# # split string
# sub_strings = str1.split("-")
# print("Displaying each substring")
# for sub in sub_strings:
#     print(sub)

"""Exercise 14: Remove empty strings from a list of strings
Given:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
"""
# Solution 1: Using the loop and if condition
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# res_list = []
# for s in str_list:
#     # check for non empty string
#     if s:
#         res_list.append(s)
# print(res_list)

# Solution 2: Using the built-in function filter()
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# # use built-in function filter to filter empty value
# new_str_list = list(filter(None, str_list))
# print("After removing empty strings")
# print(new_str_list)

"""Exercise 15: Remove special symbols / punctuation from a string
Given: Use string functions translate() and maketrans()
Use the translate() function to get a new string where specified characters are
replaced with the character described in a dictionary or a mapping table.
Use the maketrans() function to create a mapping table.
str1 = "/*Jon is @developer & musician" """
# import string
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)
# new_str = str1.translate(str.maketrans('', '', string.punctuation))
# print("New string is ", new_str)

# Solution 2: Using regex replace pattern in a string
# import re
# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# # replace special symbols with ''
# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)

"""Exercise 16: Removal all characters from a string except integers"""
# str1 = 'I am 25 years and 10 months old'
# print("Original string is", str1)
# # Retain Numbers in String
# # Using list comprehension + join() + isdigit()
# res = "".join([item for item in str1 if item.isdigit()])
# print(res)

"""Exercise 17: Find words with both alphabets and numbers"""
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)

# res = []
# # split string on whitespace
# temp = str1.split()

# # Words with both alphabets and numbers
# # isdigit() for numbers + isalpha() for alphabets
# # use any() to check each character

# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)

# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)

"""Exercise 18: Replace each special symbol with # in the following string
Use the string.punctuation constant to get the list of all punctuations
punchuation !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
Iterate each symbol from a punctuations
Use string function replace() to replace the current special symbol in a string with #
"""
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)
# Replace punctuations with #
replace_char = '#'
# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    print("punchuation",string.punctuation)
    str1 = str1.replace(char, replace_char)
print("The strings after replacement : ", str1)













