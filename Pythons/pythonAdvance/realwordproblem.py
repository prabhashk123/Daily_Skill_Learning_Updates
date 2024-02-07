# def purchase_product(product_type,price):
#     discount = 10
#     total_price = price - price * discount / 100
#     print("Total price of " +product_type+ " is "+str(total_price))
# purchase_product("Mobile", 20000)
# purchase_product("Shoe", 200)
# p2
# def purchase_product(product_type,price,mobile_brand,material=None):
#     if product_type=="Mobile":
#         if mobile_brand=="Apple":
#             discount=10
#         else:
#             discount=5
#         total_price = price - price * discount / 100
#     else:
#         if material=="leather":
#             tax=5
#         else:
#             tax=2
#         total_price=price+price*tax/100
#     print("Total price of " +product_type+" of brand "+mobile_brand+" is "+str(total_price))
# # purchase_product("Mobile",20000,"Apple")
# # # purchase_product("Shoes",200)
# # purchase_product("Mobile",20000,"Apple",None)
# purchase_product("Shoe",200000,"puma","leather")
"""p3"""
# total_price_mobile = 0
# total_price_shoe = 0
# def purchase_mobile(price,brand):
#     global total_price_mobile
#     if brand=="Apple":
#         discount=10
#     else:
#         discount=5
#     total_price_mobile=price-price*discount/100  
#     print("Total price of " +brand+ " is "+str(total_price_mobile))
# def purchase_shoe(price,material):
#     global total_price_shoe
#     if material=="leather":
#         tax=5
#     else:
#         tax=2
#     total_price_shoe=price+price*tax/100
#     print("Total price of " +material+ " is "+str(total_price_shoe))
# def return_mobile():
#     print("refund price of moblie "+ "is " +str(total_price_mobile))
# def return_shoe():
#     print("refund price of shoe " + "is " +str(total_price_shoe)) 
# # purchase_mobile(20000,"Sony")
# # purchase_shoe(10000,"leather")
# # purchase_mobile(20000,"Apple")
# purchase_shoe(200,"leather")
# purchase_mobile(2000,"Samsung")
# return_mobile()
# return_shoe()
"""soplved real problem by oops"""
# class Mobile:
#     def __init__(self,brand,price):
#         print("Inside Constructor")
#         self.brand=brand
#         self.price=price
# m1=Mobile("Apple",20000)
# print("Moble 1 has a brand "+ m1.brand + " of price is "+ str(m1.price))
# m2=Mobile("samsung",3000)
# print("Moble 2 has a brand "+ m2.brand + " of price is "+ str(m2.price))

# class Mobile:
#     def __init__(self,price,brand):
#         print("Price:",price)
#         print("Brand:",brand)
# #Uncomment each line below. Try it out and observe the output.
# mob1=Mobile()
# # mob1=Mobile(10000,'Samsung','Android')
# mob1=Mobile(10000,'Samsung')
"""prob on destructor"""
# call destructor when the object is removed from the memory
# class Product:
#     def __init__(self,price,brand):
#         self.price=price
#         self.brand=brand
#     def __del__(self):
#         print('Deleting the object')
# p1=Product(10000,'Apple')
# p2=Product(7000,'Samsung')
# # del p1
# del p2
"""prob on self"""
# class Mobile:
#     def __init__(self,price,brand):
#         print("Inside constructor")
#         self.price=price
#         self.brand=brand
#     def purchase(self):
#         print("Purchasing the mobile")
#         print("The mobile has brand ",self.brand," and price is ",self.price)
    
# print("Mobile-1")
# m1=Mobile("20000","Realme")
# m1.purchase()

"""based on encapsulation"""
# class Customer:
#     def __init__(self,Cus_id,name,age,wallet_balance):
#         self.Cus_id=Cus_id
#         self.name=name
#         self.age=age
#         self.__wallet_balance=wallet_balance
#     def update_balance(self,amount):
#         if amount<10000 and amount>0:
#             self.__wallet_balance +=amount
#     def show_balance(self):
#         print("The Balance is",self.__wallet_balance)

# c1=Customer(1183163,"Prabhash",24,20000)
# # make private by add double underscore private outside class not access only inside access this data is callled encapsulation
# # print(c1.__wallet_balance)
# c1._Customer__wallet_balance=10000000 # that can be access _classname__attributename
# c1.update_balance(1000)
# c1.show_balance()
"""p encapsulation access private by setter getter method"""
# class Customer:
#     def __init__(self,id,name,age,wallet_balance):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.__wallet_balance=wallet_balance
#     def set_wallet_balance(self,amount):
#         if amount<1000 and amount>0 :
#             self.__wallet_balance=amount
#     def get_wallet_balance(self):
#         return self.__wallet_balance

# c1=Customer(1183163,"Prabhash",24,1000)
# c1.set_wallet_balance(500)
# print(c1.get_wallet_balance())

class Student:
    def __init__(self,student_id,marks,ages):
        self.__student_id=student_id
        self.__marks=marks
        self.__age=ages
    def validate_marks(self,mark):
        if mark<100 and mark>0:
            self.__marks=mark
    def validate_age(self,age):
        if age>20:
            self.__age=age
    def check_qualification(self,mark):
        if mark>=65:
            return True
        else:
            return False
    def set_student_id(self,ids):
        if ids>=1:
            self.__student_id=ids
    def get_student_id(self):
            return self.__student_id
    def set_marks(self,mark):
        if mark>=65:
            self.__marks=mark    
    def get_marks(self):
            return self.__marks
    def set_age(self,age):
        if age>20:
            self.__age=age
    def get_age(self):
        return self.__age
s=Student(1,67,24)
s.set_student_id(2)
print(s.get_student_id())
s.set_marks(69)
print(s.get_marks())
s.set_age(25)
print(s.get_age())
# print(s.check_qualification())
        

        






    
        

