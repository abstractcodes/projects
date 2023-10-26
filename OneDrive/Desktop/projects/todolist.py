from tkinter import *
from tkinter.font import Font

# Thanking the author for this icon <a href="https://www.flaticon.com/free-icons/paper" title="paper icons">Paper icons created by Pixel perfect - Flaticon</a>
window_root = Tk()
window_root.title('To Do List!')
#window_root.iconbitmap("C:\\Users\\rishi\\OneDrive\\Desktop\\projects\\post-it.png")
window_root.geometry("500x800")

# creating a font.
font_style = Font(family="Times New Roman", size=20, weight="bold")

# creating a frame.
window_frame = Frame(window_root)
window_frame.pack(pady=10)

# creating a listbox
window_list = Listbox(window_frame,
                      font=font_style,
                      width=10,
                      height=10,
                      bg="SystemButtonFace",
                      bd=0,
                      fg="#464646",
                      highlightthickness=0,
                      selectbackground="#a6a6a6",
                      activestyle="none")

window_list.pack(side="left", fill="both")

# creating scrollbar
window_scrollbar = Scrollbar(window_frame)
window_scrollbar.pack(side="right", fill="both")

# Adding scrollbar
window_list.config(yscrollcommand=window_scrollbar.set)
window_scrollbar.config(command=window_list.yview)

# entry box
window_entry = Entry(window_root, font=("Helvetica", 24))
window_entry.pack(pady=10)


# Creating button
window_button_frame = Frame(window_root)
window_button_frame.pack(pady=20)

# Creating Functions.
def delete_item():
    window_list.delete(ANCHOR)

def add_item():
    window_list.insert(END, window_entry.get())
    window_entry.delete(0, END)

def cross_off_item():
    # crossing off an item.
    window_list.itemconfig(
        window_list.curselection(),
        fg="#dedede")
    # get rid of seclection bar.
    window_list.select_clear(0,END)

def uncross_item():
    # uncrossing off an item.
    window_list.itemconfig(
        window_list.curselection(),
        fg="#464646")
    # get rid of seclection bar.
    window_list.select_clear(0,END)
    

def clear_list():
    window_list.delete(0,END)
    
# Adding menu
windows_menu = Menu(window_root)
window_root.config(menu=windows_menu)

# Creating the menu
file_menu = Menu(windows_menu, tearoff=False)
windows_menu.add_cascade(label="file", menu=file_menu)

# Adding the dropdown.
file_menu.add_command(label="Clear list", command=clear_list)
# Adding button.
window_delete_button = Button(window_button_frame, text="Delete Item", command=delete_item)
window_add_button = Button(window_button_frame, text="Add Item", command=add_item)
window_cross_off_button = Button(window_button_frame, text="Cross Off Item", command=cross_off_item)
window_Uncross_button = Button(window_button_frame, text="Uncross Item", command=uncross_item)

# putting buttons to the grid.
window_delete_button.grid(row=0, column=0)
window_add_button.grid(row=0, column=1, padx=20)
window_cross_off_button.grid(row=0, column=2)
window_Uncross_button.grid(row=0, column=3, padx=20)

# create a dummy list.
#for item in window_list_1:
#   window_list.insert(END, item)

window_root.mainloop()
