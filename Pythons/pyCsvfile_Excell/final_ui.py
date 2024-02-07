import tkinter
import tkinter as tk
import os
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

master=tkinter.Tk()
master.geometry("900x550")
master.configure(bg= "#c3c3c3")   #gray bg
master.resizable(width= False, height= False)
master.title("Offboarding Automation Report")

# White bg color frame
options_frame = tk.Frame(master, bg = '#F0F0F0')
options_frame.pack(side = tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width = 350, height = 580)

# -------------------------- Add image ---------------------------

# Get the current directory containing the .py file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Load the image
image_path = current_directory + "\\report_img.jfif"
# Replace with the path to your image
image = Image.open(image_path)

# Resize the image if necessary
image = image.resize((230, 270)) # Replace width and height with desired dimensions

# Create a Tkinter-compatible photo image object
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(master, image=photo)
image_label.pack()
image_label.place(x=50,y=80)


#left side buttons (Title)
interim_btn = tk.Button(options_frame, text = 'Offboarding Report', font = "arial 19 bold", fg = 'black', bd =0 )
interim_btn.place(x = 45, y = 360)

def offboarding_rep():
    
    namee = current_directory + "\main.py"
    command = f'python "{namee}"'
    os.system(command)
    showinfo(
        title='Generate Offboarding Report',
        message="Offboarding Report generated."
    ) 
    
#generate offboarding report
    
button7=tkinter.Button(master, text="Generate Offboarding Report & Pivot",fg="#000080",bd = '5', padx = '4', pady = '4', font = ('Calibri bold',17), height='2',width='35',command=offboarding_rep)
button7.place(x=430, y=170)
    
# Add Buttons to generate mails

def offboarding_email():
    
    # os.system("python Draft Timesheet Report with blank values(Py)\\main.py")
    
    namee = current_directory + "\send_email.py"
    command = f'python "{namee}"'
    os.system(command)
    showinfo(
        title='Send Offboarding Report email',
        message= "Offboarding report email sent."
    ) 
button7=tkinter.Button(master, text="Send Offboarding Report Email",fg="#000080",bd = '5', padx = '4', pady = '4', font = ('Calibri bold',16), height='2',width='30',command=offboarding_email)
button7.place(x=470, y= 280)


master.mainloop()