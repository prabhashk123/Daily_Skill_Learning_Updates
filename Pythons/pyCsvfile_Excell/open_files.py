#import another file into this file
import shutil
import numpy as np
import sys
import pandas as pd
import openpyxl
import create_folders
import os
from datetime import datetime

file_cnt = 0 

#Read all input files 
for item in os.listdir(create_folders.input_path) :
    
    item_path = os.path.join(create_folders.input_path,item)
    item = item.strip().lower()
    
    if not item.startswith("~$") and item.startswith('master') and item.endswith('.xlsx'):
        master_path = item_path
        #print(master_path)
        #master_file = openpyxl.load_workbook(master_path)
        master_file  = pd.read_excel(master_path, sheet_name = 'Sheet1' )
        #master_file = master_file.iloc[:-3]
        file_cnt += 1

        
#access to_cc_mail list excel file 
to_cc_list = None
for filename in os.listdir(create_folders.current_directory): 
    if not filename.startswith("~$") and filename.startswith('mail') and filename.endswith('.xlsx'): 
        to_cc_file_path = os.path.join(create_folders.current_directory,filename)
        #print(to_cc_file_path)
        file_cnt += 1


if not file_cnt == 2:
    print("Input File not found, code abrupts....")
    sys.exit(1)
    
