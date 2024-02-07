# import os
# # create directory and subdirectory in python 
# # os.makedirs('ds/ds1/ds2')
# # os.mkdir('directory/subdirectory')
# # get current directory
# # print(os.getcwd())
# # change working directory
# # os.chdir('directory')
# # print(os.getcwd())
# # rename dirctory
# # os.rename('directory','directories')
# # make dirs then remove directory
# # os.mkdir('newdirectory')
# # os.rmdir('newdirectory')
# # make subdirectory then delete sub directory
# # os.makedirs('infosys/engineer')
# # os.rmdir('infosys/engineer')
# # removes all directory
# # os.makedirs('i/j/k/l')
# # os.removedirs('i/j/k/l')
# # information on current directory or point use walk it return itrator object then use for loop
# # search all directory
# # w=os.walk('.')
# # for i in w:
# #     print(i)
# # search specific directory use
# # w=os.walk('directories', topdown=False)
# # for i in w:
# #     print(i)
# mydir="C:/Users/prabhash.kumar/OneDrive - Infosys Limited/Desktop/infosys/task/directories"
# mylist=[]
# for (path, folders, files) in os.walk('mydir'):
#     filePaths=[
#         os.path.join(path,file)
#         for file in files 
#         ]
#     mylist.extend(filePaths)
# for file in mylist:
#     print('>>',file)


# import os
# import fnmatch
# def search_directory(root,pattern):
#     for path,subdir,files in os.walk(root):
#         for name in files:
#             if fnmatch.fnmatch(name, pattern):
#                 filepath=os.path.join(path, name)
#                 with open (filepath) as f:
#                     if pattern in f.read():
#                         print(filepath)
# search_directory("C://Users//prabhash.kumar//OneDrive - Infosys Limited//Desktop//infosys//task//directories",'de')
"""search string of list in txt file for current directries"""
# import os
# import fnmatch
# def search_string_in_files(directories,search_str):
#     line_number=[]
#     for subdir,_,files in os.walk(directories):
#         for file in files:
#                 filepath=os.path.join(subdir,file)
#                 if filepath.endswith(".txt"):
#                     with open(filepath,'r') as f:
#                         for i, line in enumerate(f,start=1):
#                             if any(search_str in line for search_str in search_str):
#                                 line_number.append(i)
#                     return line_number                      
# search_str=['Quem','Lorem','Indicant']
# filepath='C://Users//prabhash.kumar//OneDrive - Infosys Limited//Desktop//infosys//task//directories'
# line_number=search_string_in_files(filepath,search_str)
# if line_number == -1:
#     print(f"Found '{search_str}' not found in file '{filepath}' ")
# else:
#     print(f"Found '{search_str}'found in line {line_number} of file '{filepath}'")
"""both current+subdir all folder"""
import os
import re
def search_strings_in_files(root_dir, search_strings):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(subdir, file)
            if not os.path.isfile(filepath):
                continue
            with open(filepath, 'r') as f:
                for line_no, line in enumerate(f, start=1):
                    for search_string in search_strings:
                        if re.search(search_string, line):
                            print(f"Found '{search_string}' in {filepath} at line {line_no}")

search_strings = ["Lorem","de","Prabhash"]
search_strings_in_files(".", search_strings)

