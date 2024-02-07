"""For class"""
# class Table:
#     def __init__(self):
#         self.no_of_legs=4
#         self.__glass_top=None
#         self.__wooden_top=None

#     def assign_data(self,glass_top,wooden_top):
#         self.__glass_top=glass_top
#         self.__wooden_top=wooden_top

#     def identify_rate(self,glass_top,wooden_top):
#         self.assign_data(glass_top, wooden_top)
#         if(self.__glass_top==True):
#             rate=20000
#         elif(self.__wooden_top==True):
#             rate=30000
#         else:
#             rate=0
#         return rate
# dining_table=Table()
# rate=dining_table.identify_rate(True, False)
# print(rate)
# class Example:
#     num=10
#     @staticmethod
#     def add(num1,num2):
#         result=(num1+num2)*Example.num
#         return result
# print(Example.add(100, 200))
# class Lion:
#     __water_source="well in the circus"

#     def __init__(self,name, gender):
#         self.__name=name
#         self.__gender=gender

#     def drink_water(self):
#         print(self.__name,"drinks water from the",Lion.__water_source)

# simba=Lion("Simba","Male")
# nala=Lion("Nala","Female")
# simba.drink_water()
# nala.drink_water()
"""Aggresation and association"""
# class Customer:
#     def __init__(self,name,age,phone_no,address):
#         self.name=name
#         self.age=age
#         self.phone_no=phone_no
#         self.address=address
#     def view_details(self):
#         print(self.name,self.age,self.phone_no)
#         print (self.address.door_no, self.address.street,self.address.area, self.address.pincode)
#     def update_details(self,add):
#         self.address=add
# class Address:
#     def __init__(self,door_no,street,area,pincode):
#         self.door_no=door_no
#         self.street=street
#         self.area=area
#         self.pincode=pincode
#     def update_address(self):
#         pass
# add1=Address(123,"5th Lane","Urban",56001)
# add2=Address(567,"6th Lane","Rural",82006)
# # cus1=Customer("Jack",24,1234,None)
# cus1=Customer("Jack",24,1234,add1)
# cus1.view_details()
# cus1.update_details(add2)
# cus1.view_details()
# # cus2=Customer("Jane",25,5678,None)
# # aggresation
# # cus2=Customer("Jane",25,5678,add2)
""""make private"""
# class Customer:
#     def __init__(self,name,age,phone_no,address):
#         self.name=name
#         self.age=age
#         self.phone_no=phone_no
#         self.address=address
#     def view_details(self):
#         print(self.name,self.age,self.phone_no)
#         print (self.address.get_door_no(), self.address.get_street(),self.address.get_area(), self.address.get_pincode())
#     def update_details(self,add):
#         self.address=add
# class Address:
#     def __init__(self,door_no,street,area,pincode):
#         self.__door_no=door_no
#         self.__street=street
#         self.__area=area
#         self.__pincode=pincode
#     def get_door_no(self):
#         return self.__door_no
#     def get_street(self):
#         return self.__street
#     def get_area(self):
#         return self.__area
#     def get_pincode(self):
#         return self.__pincode
#     def set_door_no(self, value):
#         self.__door_no = value
#     def set_street(self, value):
#         self.__street = value
#     def set_pincode(self, value):
#         self.__pincode = value
#     def update_address(self):
#         pass
# add1=Address(123,"5th Lane","Urban",56001)
# # add2=Address(567,"6th Lane","Rural",82006)
# cus1=Customer("Jack",24,1234,add1)
# cus1.view_details()
# # cus1.update_details(add2)
# # cus1.view_details()
"""Uses of class attribute """
# class Customercare:
#     helpline=9570588189
# class Custromer:
#     def call_support(self):
#         print("Calling",Customercare.helpline)
# Custromer().call_support()
"""Uses of classmethod -means private of class attribue"""
# class CustomerCare:
#     __helplineno=9709938919
#     @classmethod
#     def get_helpline(cls):
#         return cls.__helplineno
# class Customers:
#     def call_supports(self):
#         print("Calling",CustomerCare.get_helpline())
# Customers().call_supports()

"""Assciation -dependent on other class"""
# class Cuutomer:
#     def __init__(self,cus_id,name):
#         self.cus_id=cus_id
#         self.name=name
#     def pay(self,payment):
#         print(payment.type,payment.price)
#     def cus_details(self):
#         print(self.cus_id,self.name)
        
# class Payment:
#     def __init__(self,type,price):
#         self.type=type
#         self.price=price
# p1=Payment("Upi",200)
# c1=Cuutomer("Prabhash",1183163)
# c1.cus_details()
# c1.pay(p1)
"""Inheritence"""
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price
#         self.brand=brand
#         self.camera=camera
#     def buy(self):
#         print(f"Buying phone {self.brand} having camera {self.camera} of price is {self.__price}.")
#     def return_phone(self):
#         print(f"Returning phone brand is {self.brand}.")
# # Make private for price
#     def get_price(self):
#         return self.__price
#     def set_price(self,price):
#         self.__price=price
# class FeaturePhone(Phone):
#     pass 
# class SmartPhone(Phone):
#     def check(self):
#         print(self.brand)
#         print(self.camera)
#         print(self.get_price())
# p1=Phone(19999,"Realme","50mpx")
# p1.buy()
# p1.return_phone()
# s=SmartPhone(2999,"Oppo","30mpx")
# s.check()
"""Method overiding means same method name of child and parent class solve as suprr()"""
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price
#         self.brand=brand
#         self.camera=camera
#     def buy(self):
#         print(f"Buying phone {self.brand} having camera {self.camera} of price is {self.__price}.")
#     def return_phone(self):
#         print(f"Returning phone brand is {self.brand}.")
# # Make private for price
#     def get_price(self):
#         return self.__price
#     def set_price(self,price):
#         self.__price=price
# class FeaturePhone(Phone):
#     pass 
# class SmartPhone(Phone):
#     def check(self):
#         print(self.brand)
#         print(self.camera)
#         print(self.get_price())
#     def buy(self):
#         print("Buying Smartphone")
#         super().buy()
# p1=Phone(19999,"Realme","50mpx")
# p1.buy()
# p1.return_phone()
# s=SmartPhone(2999,"Oppo","30mpx")
# # s.check()
# s.buy()
"""Method overdding using for cunstructor"""
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor as parent class")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print ("Buying a phone")
#     def return_phone(self):
#         print ("Returning a phone")
# class FeaturePhone(Phone):
#     pass
# class SmartPhone(Phone):
#     def __init__(self,price,brand,camera, os, ram):
#         super().__init__(price,brand,camera)
#         self.os = os
#         self.ram = ram
#         print ("Inside SmartPhone constructor as child class")
#     def buy(self):
#         print("Buying a SmartPhone")
# s=SmartPhone(20000, "Samsung", 12, "Android", 2)
# print(s.os)
# print(s.brand)
while(True):
    age=int(input("enter your age"))

    try:
        if age<18:
            raise Exception("age")
        else:
            v_id=input("Do u have voter id?Y or N")
            if v_id=="N":
                raise Exception("id")
            print("You are eligible to vote")

    except Exception as e:
        if(str(e)=="age"):
            print("You r not eligible to vote as your age is less than 18")
        elif(str(e)=="id"):
            print("You cannot vote without voter Id")
        else:
            print("Some Error occured")

