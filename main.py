import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Enty Form")
frame=tkinter.Frame(window)
frame.pack()
user_info= tkinter.LabelFrame(frame,text="User Information")
user_info.grid(row=0,column=0)


user_first_name= tkinter.Label(user_info,text="First Name")
user_first_name.grid(row=0,column=0)
user_first_name_entry = tkinter.Entry(user_info)
user_first_name_entry.grid(row=0,column=1)

user_last_name= tkinter.Label(user_info,text="Last Name")
user_last_name.grid(row=1,column=0)
user_last_name_entry = tkinter.Entry(user_info)
user_last_name_entry.grid(row=1 ,column=1)

check=tkinter.Label(user_info,text="Check")
check.grid(row=2,column=0)
check_combobox = ttk.Combobox(user_info,values=[1,2,3,4,5,6])
check_combobox.grid(row=2,column=1)
window.mainloop()