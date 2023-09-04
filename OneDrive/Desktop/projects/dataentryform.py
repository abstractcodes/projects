import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl


def display_data():
    accept = terms_variable.get()
    if accept=="Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        courses = numcourses_spinbox.get()
        semesters = numsemesters_spinbox.get()
        register_status = register_variable.get()
        root_window.destroy()
    else:
        tkinter.messagebox.showwarning(title="Error",message="Please accept the terms and conditions!")
    
    # adding to excel sheet
    filepath = "C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\data.xlsx"
    
    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Title","First Name","Last Name","Age","Courses Completed","Semesters Completed","Registration Status"]
        sheet.append(heading)
        workbook.save(filepath)
    # if active
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([title,first_name,last_name,age,courses,semesters,register_status])
    workbook.save(filepath)
        
    
# root window
root_window = tkinter.Tk()
root_window.title("Data entry Form")

# root window           
root_frame = tkinter.Frame(root_window)
root_frame.pack()

# top frame
user_input_frame = tkinter.LabelFrame(root_frame, text="User Information")
user_input_frame.grid(row=0, column=0, padx=20, pady=10)

# deploy the user input input
first_name_label = tkinter.Label(user_input_frame, text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label = tkinter.Label(user_input_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_input_frame)
last_name_entry = tkinter.Entry(user_input_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

# columnbox
title_label = tkinter.Label(user_input_frame, text="Title")
title_combobox = ttk.Combobox(user_input_frame, values = ["","Mr.","Ms.","Dr."])
title_label.grid(row=0,column=3)
title_combobox.grid(row=1,column=3)

#spinbox
age_label = tkinter.Label(user_input_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_input_frame, from_= 18, to=100)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

for widget in user_input_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

course_label = tkinter.LabelFrame(root_frame)
course_label.grid(row=1, column=0, sticky="news", padx= 20, pady=10)

registration_label = tkinter.Label(course_label, text="Registration status")
register_variable = tkinter.StringVar(value="Not Registered")
registration_checkbutton = tkinter.Checkbutton(course_label, text= "Currently Registered", variable=register_variable,onvalue="Registered",offvalue="Not Registered")
registration_label.grid(row=0, column=0)
registration_checkbutton.grid(row=1,column=0)

numcourses_label = tkinter.Label(course_label, text="Courses Completed")
numcourses_spinbox = tkinter.Spinbox(course_label, from_=0, to="40")
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_label = tkinter.Label(course_label, text="Semesters Completed")
numsemesters_spinbox = tkinter.Spinbox(course_label, from_=0, to="8")
numsemesters_label.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)

for widget in course_label.winfo_children():
    widget.grid_configure(padx=10,pady=10)

# Accept terms
terms_frame = tkinter.LabelFrame(root_frame,text="Terms And Conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

terms_variable = tkinter.StringVar(value="Not Accepted")
terms_checkbutton = tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions", variable=terms_variable,onvalue="Accepted",offvalue="Not Accepted")
terms_checkbutton.grid(row=0,column=0)    

# Adding button
button = tkinter.Button(root_frame,text="Enter data", command=display_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)



root_window.mainloop()