import tkinter
from plyer import notification
from tkinter import Tk,PhotoImage
from tkinter import messagebox


def enter_data():
    title = title_text_entry.get()
    message = message_text_entry.get()
    if title!="" and message!="":
      notification.notify(title,
                    message,
                    app_icon = "",
                    app_name="Notifier",
                    timeout=10)  
      root_window.destroy()
    else:
       tkinter.messagebox.showwarning(title="Error",message="Please Enter The title and message to be displayed!") 

    
root_window = tkinter.Tk()
root_window.title("Desktop Notifier")

icon_image = PhotoImage(file="C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\free-bell-icon-2031-thumb.png")
root_window.iconphoto(False,icon_image)
# create a label frame
main_frame = tkinter.Frame(root_window)
main_frame.pack()
main_frame.configure(bg="light blue")

information_frame = tkinter.LabelFrame(main_frame,text="Notification Message")
information_frame.grid(row=0,column=0,padx=20,pady=10)
information_frame.configure(bg="light blue")

title_text = tkinter.Label(information_frame,text="Title")
title_text.grid(row=0,column=0)
title_text.configure(font=("Times New Roman",10,"bold"),background="Light Pink")

message_text = tkinter.Label(information_frame,text="Message input")
message_text.grid(row=2,column=0)
message_text.configure(font=("Times New Roman",10,"bold"),background="Light Pink")

title_text_entry = tkinter.Entry(information_frame)
title_text_entry.grid(row=1,column=0)
title_text_entry.configure(bg="light yellow")

message_text_entry = tkinter.Entry(information_frame)
message_text_entry.grid(row=3,column=0)
message_text_entry.configure(bg="light yellow")

enter_button = tkinter.Button(information_frame,text="Enter Data",command=enter_data)
enter_button.grid(row=4,column=0)

for widget in information_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

root_window.mainloop()
