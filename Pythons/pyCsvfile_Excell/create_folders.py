#To work with paths and files
import os

# Get the current directory containing the .py file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the path of the current .py file
current_file_path = os.path.abspath(__file__)

# Create a new directory in the current directory
input_path = os.path.join(current_directory, 'Input_Files')     # join() : create file paths
output_path = os.path.join(current_directory, 'Output_Files')
output_path_backup = os.path.join(current_directory, 'Output_Files_Backup')

# Check if the new directory already exists
if not os.path.exists(input_path):
    # If it does not exist, create it
    os.makedirs(input_path)

if not os.path.exists(output_path):
    # If it does not exist, create it
    os.makedirs(output_path)
    
if not os.path.exists(output_path_backup):
    # If it does not exist, create it
    os.makedirs(output_path_backup)