import tkinter
from tkinter import ttk
import os
import openpyxl

def enter_data():
    print("date: "+date_entry.get())
    print("code h/c: "+code_hc_combobox.get())
    print("mana: "+mana_entry.get())
    print("mana color: "+mana_color_entry.get())
    print("number risusim: "+number_risusim_combobox.get())
    print("viscosity: "+viscosity_entry.get())
    print("PSI: "+psi_entry.get())
    print("מידה: "+mida_entry.get())
    print("משקל: "+weight_entry.get())
    print("טמפרטורה: "+temp_entry.get()+"C")
    print("לחות: "+humidity_entry.get()+"%")
    print("הערות: "+desc_entry.get())
    
    print("----------------------------------------------------------------")    
    
            
    filepath = 'data.xlsx'
    
    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["תאריך", "קוד", "מנת", "מספר מנה","מנת צבע"
                           "מספר ריסוסים", "צמיגות", "PSI","מידה","משקל","טמפרטורה","לחות","הערות"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([date_entry.get(), code_hc_combobox.get(), mana_entry.get(), mana_color_entry.get(), number_risusim_combobox.get(), viscosity_entry.get(),
                          psi_entry.get(), mida_entry.get(),weight_entry.get(),temp_entry.get()+"C",humidity_entry.get()+"%",desc_entry.get()])
    workbook.save(filepath)
                
    
window = tkinter.Tk()
window.title("Data Enty Form")
frame=tkinter.Frame(window)
frame.pack()
data_info= tkinter.LabelFrame(frame,text="Information")
data_info.grid(row=0,column=0 ,padx=20,pady=20)


date_label= tkinter.Label(data_info,text="תאריך")
date_label.grid(row=0,column=1)
date_entry = tkinter.Entry(data_info)
date_entry.grid(row=0,column=0)


code_hc_label=tkinter.Label(data_info,text="קוד")
code_hc_label.grid(row=1,column=1 )
code_hc_combobox = ttk.Combobox(data_info,values=["אדום","צהוב"])
code_hc_combobox.grid(row=1,column=0)


mana_label= tkinter.Label(data_info,text="מנת")
mana_label.grid(row=2,column=1)
mana_entry = tkinter.Entry(data_info)
mana_entry.grid(row=2 ,column=0)


number_mana_label= tkinter.Label(data_info,text="מספר מנה")
number_mana_label.grid(row=3,column=1)
number_mana_entry = tkinter.Entry(data_info)
number_mana_entry.grid(row=3 ,column=0)


mana_color_label= tkinter.Label(data_info,text="מנת צבע")
mana_color_label.grid(row=4,column=1)
mana_color_entry = tkinter.Entry(data_info)
mana_color_entry.grid(row=4 ,column=0)


number_risusim_label= tkinter.Label(data_info,text="מספר ריסוסים")
number_risusim_label.grid(row=5,column=1)
number_risusim_combobox =  ttk.Combobox(data_info,values=[1,2,3,4,5,6,7])
number_risusim_combobox.grid(row=5 ,column=0)


viscosity_label= tkinter.Label(data_info,text="צמיגות")
viscosity_label.grid(row=6,column=1)
viscosity_entry = tkinter.Entry(data_info)
viscosity_entry.grid(row=6,column=0)


psi_label= tkinter.Label(data_info,text="PSI")
psi_label.grid(row=7,column=1)
psi_entry = tkinter.Entry(data_info)
psi_entry.grid(row=7,column=0)

mida_label= tkinter.Label(data_info,text="מידה")
mida_label.grid(row=7,column=3)
mida_entry = tkinter.Entry(data_info)
mida_entry.grid(row=7,column=2)


weight_label= tkinter.Label(data_info,text="משקל")
weight_label.grid(row=8,column=1)
weight_entry = tkinter.Entry(data_info)
weight_entry.grid(row=8,column=0)


temp_label= tkinter.Label(data_info,text="טמפרטורה")
temp_label.grid(row=9,column=1)
temp_entry = tkinter.Entry(data_info)
temp_entry.grid(row=9,column=0)


humidity_label= tkinter.Label(data_info,text="לחות")
humidity_label.grid(row=9,column=3)
humidity_entry = tkinter.Entry(data_info)
humidity_entry.grid(row=9,column=2)



desc_label= tkinter.Label(data_info,text="הערות")
desc_label.grid(row=11,column=1)
desc_entry = tkinter.Entry(data_info)
desc_entry.grid(row=11,column=0)
                          
for widget in data_info.winfo_children():
    widget.grid_configure(padx=5,pady=5)

button = tkinter.Button(data_info, text="ENTER",command=enter_data).grid(row=12,column=0)

window.mainloop()