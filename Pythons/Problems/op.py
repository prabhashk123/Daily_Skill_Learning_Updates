# numbers = []

# # 5 is the list size
# # run loop 5 times
# for i in range(0, 5):
#     print("Enter number at location", i, ":")
#     # accept float number from user
#     item = float(input())
#     # add it to the list
#     numbers.append(item)

# print("User List:", numbers)

"""Exercise 6: Write all content of a given file into a new file by skipping line number 5"""
# open new file in write mode
# with open("C://Users//prabhash.kumar\OneDrive - Infosys Limited//Desktop//Daily_Skill_Learning_Updates//Pythons//Problems//file.text",'r') as f:
#     lines=f.readlines()
# # open new file in write mode
# with open("C://Users//prabhash.kumar\OneDrive - Infosys Limited//Desktop//Daily_Skill_Learning_Updates//Pythons//Problems//newfile.text",'w') as f:
#     count=0
#     # iterate each lines from a file.text
#     for line in lines:
#         # skip 5th lines
#         if count == 4:
#             count += 1
#             continue
#         else:
#             # write current line
#             f.write(line)
#         # in each iteration reduce the count
#         count += 1

"""Exercise 9: Check file is empty or not"""
# import os
# size_of_file=os.stat("C://Users//prabhash.kumar\OneDrive - Infosys Limited//Desktop//Daily_Skill_Learning_Updates//Pythons//Problems//newfile.text").st_size
# if size_of_file==0:
#     print("This file is empty.")
# else:
#     print("This file is not empty.")

"""Exercise 10: Read line number 4 from the following file"""
# read file
# with open("C://Users//prabhash.kumar\OneDrive - Infosys Limited//Desktop//Daily_Skill_Learning_Updates//Pythons//Problems//newfile.text",'r') as f:
#     # read all lines from a file
#     lines = f.readlines()
#     # get line number 3
#     print(lines[1])


