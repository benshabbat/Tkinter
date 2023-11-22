import tkinter

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
window.mainloop()