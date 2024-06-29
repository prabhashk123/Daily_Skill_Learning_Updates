"""Exercise 1: Create a function in Python"""
# def Prabhash(gender,age):
#     print(gender,age)
# print("Male",26)

"""Exercise 2: Create a function with variable length of arguments"""
# call function with 3 arguments
# def func1(a,b,c):
#     print(a,b,c)
# func1(20, 40, 60)
# # call function with 2 arguments
# # func1(80, 100)

"""Exercise 3: Return multiple values from a function ex-calculation
like both substract and addition"""
# def multivaluefunc(a,b):
#     return a+b,a-b
# res=multivaluefunc(6,3)
# print(res)

"""Exercise 4: Create a function with a default argument"""
# function with default argument
# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)
# show_employee("Ben", 12000)
# show_employee("Jessa")

"""Exercise 5: Create an inner function to calculate the addition in the following way"""
# outer function
# def outer_fun(a, b):
#     square = a ** 2
#     # inner function
#     def addition(a, b):
#         return a + b
#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5
# result = outer_fun(5, 10)
# print(result)

"""Exercise 6: Create a recursive function"""
# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0
# res = addition(10)
# print(res)

"""Exercise 7: Assign a different name to function and call it through the new name"""
# def display_student(name, age):
#     print(name, age)
# # call using original name
# display_student("Emma", 26)
# # assign new name
# showStudent = display_student
# # call using new name
# showStudent("Emma", 26)

"""Exercise 8: Generate a Python list of all the even numbers between 4 to 30"""
# print(list(range(4,30,2)),end=' ')

"""Exercise 9: Find the largest item from a given list"""
# x = [4, 6, 8, 24, 12, 2]
# # for built in func
# print(max(x))
