# import csv
"""Read"""
# with open(r'data.csv','r') as csvfile:
#     contents=csv.reader(csvfile)
#     print(type(contents))
#     for c in contents:
#         print(c)
# with open(r'data.csv','r') as csvfile:
#     contents=csv.DictReader(csvfile)
#     print(type(contents))
#     for c in contents:
#         print(c)
"""Write"""
# For writer()
# with open(r'data.csv','a') as csvfile:
#     content=csv.writer(csvfile)
#     content.writerow(['Shrey','22'])
#     content.writerow(["Name","Prabhash"])
#     content.writerows([["Name",'Prabhash'],["Role","System Engineer"]])
"""For dictwriter"""
# with open(r'data1.csv','a') as csvfile:
#     fields=['name','age','city']

#     content=csv.DictWriter(csvfile,fields)
#     content.writeheader()

#     content.writerow({'name':'Shrey','age':'22','city':'Prayag'})
#     content.writerow({'name':'Shreya','age':'22','city':'LKO'})
  
# class Parent:
#     def __init__(self,var1):
#         self.__var1=var1
#     def get_var1(self):
#         return self.__var1

# class Child(Parent):
#     def __init__(self,var1,var2):
#         super().__init__(var1)
#         self.var2 = var2

# obj1 = Child(10,20)
# print(obj1.get_var1())
    