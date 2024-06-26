"""print("Printing current and previous number and their sum in a range(10)")"""
# previous_num = 0
# # loop from 1 to 10
# for i in range(0, 10):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i

"""Exercise 3: Print characters from a string that are present at an even index number"""
# str = "pynative"
# for i in range(0,len(str)-1,2):
#     print(str[i])

"""Exercise 4: Remove first n characters from a string"""
# Method-1
# str = "pynative"
# print(str[4:])

# Method-2
# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))

"""Exercise 5: Check if the first and last number of a list is the same"""
# number_x = [10, 20, 30, 40, 13]
# def check_f_l_number(number_x):
#     if number_x[0]==number_x[len(number_x)-1]:
#         return True
#     else:
#         return False
# print(check_f_l_number(number_x))

"""Exercise 6: Display numbers divisible by 5 from a list"""
# lst=[10, 20, 33, 46, 55]
# for num in lst:
#     if num%5==0:
#         print(num)
        
"""Exercise 7: Return the count of a given substring from a string"""
# Method-1
# str_x = "Emma is good developer. Emma is a writer"
# c=str_x.count("Emma")
# print(f"{c} Times of substring Emma.")

# Method-2 2: Without string method
# def count_emma(statement):
#     print("Given String: ", statement)
#     count = 0
#     for i in range(len(statement) - 1):
#         count += statement[i: i + 4] == 'Emma'
#     return count
# count = count_emma("Emma is good developer. Emma is a writer")
# print("Emma appeared ", count, "times")

"""Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

"""
# for num in range(6):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print("\n")

"""Exercise 9: Check Palindrome Number"""
# palindrom if number is same afte reverse the number
# number=int(input("Enter number: "))
# def number_is_palindrome(number):
#     print("original number", number)
#     original_num = number
    
# # reverse the given number
#     reverse_num = 0
#     while number>0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10
    
# # Check palindrome 
#     if original_num == reverse_num:
#         print("Given number is palindrome")
#     else:
#         print("Given number is not palindrome")

# number_is_palindrome(121)

""" Create a new list from two list using the following condition
new list should contain odd numbers from the first list and even 
numbers from the second list.
"""
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# def merge_list(list1,list2):
#     result_list=[]
    
#     # iterate first list
#     for num in list1:
#         # check if current number is odd
#         if num%2!=0:
#             # add odd number to result list
#             result_list.append(num)
#     # iterate second list
#     for num in list2:
#         # check if current number is even
#         if num % 2 == 0:
#             # add even number to result list
#             result_list.append(num)
            
#     return result_list
    
# print("result list:", merge_list(list1, list2))

"""Exercise 11: Write a Program to extract each digit from an integer in the reverse order."""
# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")

"""Exercise 12: Calculate income tax for the given income by adhering to the rules below
10000*0% + 10000*10%  + 25000*20% = $6000. ---this rule
"""
# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income<=19000:
#     tax_payable = 0
# elif income<=20000:
#      # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0
    
#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100
    
#         # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100

# print("Total tax to pay is", tax_payable)

"""Exercise 13: Print multiplication table from 1 to 10"""
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print("\t\t")

"""Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*

*  
* *  
* * *  
* * * *  
* * * * * 
"""
# for i in range(6,0,-1):
#     for j in range(0,i-1):
#         print("*", end=' ')
#     print(" ")
# m-2
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=' ')
#     print(" ")

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print(" ")
         
"""Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp"""
# def exponent(base, exp):
#     num=exp
#     result = 1
#     while num>0:
#         result=result*base
#         num=num-1
#     print(base, "raises to the power of", exp, "is: ", result)
# exponent(5, 4)

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
# base=int(input("Enter base: "))
# exp=int(input("Enter exponential value: "))
print("Result:",power(5,4))
    


    

        
    
        

