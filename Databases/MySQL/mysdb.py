# pip install mysql.connector
"""Insert operation"""
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",password='',database="Lexdb")
# cur=con.cursor()
# # cur.execute("Insert INTO lextable VALUES(1183163,'Prabhash Kumar','System Engineer','2021-10-18')")
# cur.execute("Insert INTO lextable VALUES(1183164,'Akash Kumar','System Engineer','2021-12-01')")
# cur.execute("Insert INTO lextable VALUES(1183165,'Subhash Kumar','System Engineer','2021-11-10')")
# cur.execute("Insert INTO lextable VALUES(1183166,'Rahul Kumar','System Engineer','2021-09-14')")
# cur.close()
# con.commit()
# con.close()


"""SELECT operation"""
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",password='',database="Lexdb")
# cur=con.cursor()
# cur.execute("SELECT * from lextable")
# # for r in cur:
# #     print(r)
# # for r in cur:
# #     print(r[1],r[3])
# for c1,c2,c3,c4 in cur:
#     print(c1)
# # print(cur.rowcount)
# cur.close()
# con.commit()
# con.close()
"""Feth  data"""
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",password='',database="Lexdb")
# cur=con.cursor()
# cur.execute("SELECT * from lextable where Emp_id=1183164")
# print(cur.fetchall())
# # print(cur.fetchone())
# # print(cur.fetchmany())
# # print(cur.rowcount)
# cur.close()
# con.commit()
# con.close()
"""Delete operation"""
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",password="",database="Lexdb")
# cur=con.cursor()
# cur.execute("DELETE FROM lextable where Emp_id=1183164 ")
# print("deleted")
# cur.close()
# con.commit()
# con.close()
"""Update"""
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="root",password="",database="Lexdb")
# cur=con.cursor()
# cur.execute("Update lextable set Emp_Doj='2021-10-18' where Emp_id=1183163")
# print(cur.rowcount)
# cur.close()
# con.commit()
# con.close()
"""Variable binding"""
# import mysql.connector
# Id=input('Enter Your id ')
# Name=input("Enter your name ")
# Role=input("Enter yor role ")
# Location=input("Enter your Location ")
# Exp=input("Enter your exp ")
# Tech=input("Enter your technology which yoy have work")
# Plang=input("Enter your Programming language ")
# Proj=input("Enter your project which you have work ")
# Mob=input("Enter your mobile number ")
# con=mysql.connector.connect(host="localhost",user="root",password="",database='Lexdb')
# cur=con.cursor()
# Pass List
# cur.execute("insert into filltable(Id,Name,Role,Location,Exp,Tech,Plang,Proj,Mob) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",[Id,Name,Role,Location,Exp,Tech,Plang,Proj,Mob])
# # Pass Dict
# cur.execute("insert into filltable(Id,Name,Role,Location,Exp,Tech,Plang,Proj,Mob) values(%(Id)s,%(Name)s,%(Role)s,%(Location)s,%(Exp)s,%(Tech)s,%(Plang)s,%(Proj)s,%(Mob)s)",{'Id':Id,'Name':Name,'Role':Role,'Location':Location,'Exp':Exp,'Tech':Tech,'Plang':Plang,'Proj':Proj,'Mob':Mob})
# cur.close()
# con.commit()
# con.close()
"""Exception mysql query"""
# import mysql.connector
# try:
#     con=mysql.connector.connect(host="localhost",user="root",password="",database="Lexdb")
#     cur=con.cursor()
#     cur.execute("Update lextable set Emp_Doj='2021-10-17' where Emp_id=1183163")
#     cur.close()
#     con.commit()
#     con.close()
# except mysql.connector.errors.ProgrammingError as e:
#     print("Prgramming Error",str(e))
# except mysql.connector.errors.OperationalError as e:
#     print("Operational Error",str(e))
# except Exception as e:
#     print(str(e))

# import mysql.connector
# con=mysql.connector.connect(user='root',host='localhost',password='',database='Lexdb')
# cur=con.cursor()
# cur.execute("select * from travello_destination")
