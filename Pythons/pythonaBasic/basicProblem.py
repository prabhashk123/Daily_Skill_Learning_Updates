"""first basic problem"""
# print("GeeksQuiz") 
# name=input("Enter Your Name ")
# if name=="Bond":
#     print("Welcom to on board 007 ")
# else:
#     print(f"Good Morning {name} ")
# str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"


#Type your answer here.

# def count_l(a):
#     letter=0
#     for i in a.split():
#         if "l" in i:
#             letter +=1
#         else:
#             pass
#     return letter
     
# print(count_l(str))
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def show_Emp_details(self):
#         print(self.name,self.id)
# e=Employee("Prabhash",1183163)
# e.show_Emp_details()

# lst=[0,1,2,3,4]
# # Type your answer here.

# # ans_1=lst[::-1]

# lst.reverse()
# print(lst)
# str = 'My Name is Jessa'
# str=list(str)

# print(str)

# --------------------------------------------------------
# nextdays
"""Qes-(1)DEV and QA : Write a function (addNums) to add numbers.
But the # of arguments can vary."""
# ------------------
# def addNums(*args):
# 	i=0
# 	for num in args:
# 	    i=i+num
# 	return i
# result1=addNums(4,5,6)
# print(result1)
# result2=addNums(4,5)
# print(result2)
# # ---------------------------
# """ques(2)DEV and QA: Add a decorator function to the above addNums function to print "Before" and "After"
# -----------------------"""
# def decort(func):
#     def sum(**kwargs):
#         print("Before")
#         result=func(**kwargs)
#         print(result)
#         print("After")
#     return sum
# @decort
# def addNums(**kwargs):
#     sum=0
#     for i,j in kwargs.items():
#         sum =sum+j
#     return sum
# result=addNums(num1=4,num2=5,num3=6)
# result=addNums(n1=4,n2=5)
"""--------------------------------------
ques(4)
Dev Only: Write a class Cars with
- max_speed and model as instace attributes.
- available_qty as Class Attribute initialized to 5
-  Buy() as method
--------------------------"""
# class Car:
#     available_qty =5
#     def __init__(self,max_speed,model):
#         self.max_speed=max_speed
#         self.model=model
#     def Buy(self):
#         if Car.available_qty >0:
#             Car.available_qty -=1
#             print(self.model,"Bought")
#         else:
#             print("Not Bought")
            
# Honda = Car(200,'Honda')
# Toyota = Car(200,'Toyota')
# print(Car.available_qty)
# Honda.Buy()
# Toyota.Buy()
# print(Car.available_qty)
"""--------------------------
ques-(5)"""
# class Solution:
#     def plusOne(self, digits):
#     string=""
#     for i in digits:
#         string +=str(i)
#     string=int(string)+1
#     string=str(string)
#     i=[int(x) in string]
#     print(i)
# temp=Solution()
# temp.plusOne([4,3,2,1])