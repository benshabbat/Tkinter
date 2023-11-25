import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Enty Form")
frame=tkinter.Frame(window)
frame.pack()
data_info= tkinter.LabelFrame(frame,text="Information").grid(row=0,column=0 ,padx=20,pady=20)


date_label= tkinter.Label(data_info,text="תאריך").grid(row=0,column=1)
date_entry = tkinter.Entry(data_info).grid(row=0,column=0)


code_hc_label=tkinter.Label(data_info,text="קוד").grid(row=1,column=1)
code_hc_combobox = ttk.Combobox(data_info,values=["אדום","צהוב"]).grid(row=1,column=0)


mana_label= tkinter.Label(data_info,text="מנת").grid(row=2,column=1)
mana_entry = tkinter.Entry(data_info).grid(row=2 ,column=0)



number_mana_label= tkinter.Label(data_info,text="מספר מנה").grid(row=3,column=1)
number_mana_entry = tkinter.Entry(data_info).grid(row=3 ,column=0)



mana_color_label= tkinter.Label(data_info,text="מנת צבע").grid(row=4,column=1)
mana_color_entry = tkinter.Entry(data_info).grid(row=4 ,column=0)



number_risusim_label= tkinter.Label(data_info,text="מספר ריסוסים").grid(row=5,column=1)
number_risusim_combobox =  ttk.Combobox(data_info,values=[1,2,3,4,5,6,7]).grid(row=5 ,column=0)



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


window.mainloop()