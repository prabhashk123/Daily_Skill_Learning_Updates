# import openpyxl as xl
"""Create workbook,worsheet,remove worksheet"""
# wb=xl.Workbook()          #create workbook
# wb.save(r'Employeex.xlsx')

# wb.create_sheet(title="d3",index=3)  #worksheet creation
# print(wb.sheetnames)
# wb.remove(wb['Sheet'])               #remove worksheet
# print(wb.sheetnames)
# wb.save(r'pyxlfile.xlsx')

# workbook=xl.load_workbook("Employeex.xlsx")
# print("Sheetnames:",workbook.sheetnames)
# worksheet=workbook['d2']
# print(type(worksheet))
# cells=worksheet.cell(2,2)
# print(cells.value)
# c2=worksheet['A2']
# print(c2.value)

"""ex2-to read row and col data"""
# -------------------------------
# wb=xl.load_workbook(r'Employeex.xlsx')
# ws=wb['d2']
# print("maximum row:",ws.max_row)
# print("maximum column:",ws.max_column)

# row=ws[2]

# for r in row:
#     print(r.value)

# col=ws['B']
# for col in col:
#     print(col.value)

"""Slicing
---------------"""
# import openpyxl as xl
# wb=xl.load_workbook(r'Employeex.xlsx')
# ws=wb['d2']

# row=ws['A1':'B4']
# for col in row:
#     for cell in col:
        # print(cell.value)

"""Append->to add data
------------------------
->append() - is used to add data"""

# wb=xl.load_workbook(r'Employeex.xlsx')
# ws=wb['d2']
# ws.append(['Id',"Name"])
# ws.append([5,'ROHAN'])
# ws.append([6,"Pragya"])
# wb.save(r'Employeex.xlsx')

"""To delete data"""
# wb=xl.load_workbook(r'Employeex.xlsx')
# ws=wb['d2']
# ws.delete_rows(2,2)
# ws.delete_cols(2)
# wb.save(r'Employeex.xlsx')

"""Insert Row /Column
------------------------"""
# ->insert_rows()->to insert row
# ->insert_cols()->to insert col
# wb=xl.load_workbook(r'Employeex.xlsx')
# ws=wb['d2']
# ws.insert_rows(2,2)
# ws.insert_cols(1,4)
# wb.save(r'Employeex.xlsx')
# import openpyxl as xl

# wb=xl.load_workbook(r'Employeex.xlsx')
# ws=wb['d2']
# id_to_be_deleted=2
# for row_num in range(2,ws.max_row+1):
#     if ws.cell(row_num,1).value == id_to_be_deleted:
#         ws.delete_rows(row_num,1)
# print(row_num)
