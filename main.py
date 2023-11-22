import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Enty Form")
frame=tkinter.Frame(window)
frame.pack()
data_info= tkinter.LabelFrame(frame,text="Information")
data_info.grid(row=0,column=0)


date_label= tkinter.Label(data_info,text="תאריך")
date_label.grid(row=0,column=1)
date_entry = tkinter.Entry(data_info)
date_entry.grid(row=0,column=0)


code_hc_label=tkinter.Label(data_info,text="קוד")
code_hc_label.grid(row=1,column=1)
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


weight_label= tkinter.Label(data_info,text="משקל")
weight_label.grid(row=8,column=1)
weight_entry = tkinter.Entry(data_info)
weight_entry.grid(row=8,column=0)


temp_label= tkinter.Label(data_info,text="טמפרטורה")
temp_label.grid(row=9,column=1)
temp_entry = tkinter.Entry(data_info)
temp_entry.grid(row=9,column=0)


humidity_label= tkinter.Label(data_info,text="לחות")
humidity_label.grid(row=10,column=1)
humidity_entry = tkinter.Entry(data_info)
humidity_entry.grid(row=10,column=0)



desc_label= tkinter.Label(data_info,text="הערות")
desc_label.grid(row=11,column=1)
desc_entry = tkinter.Entry(data_info)
desc_entry.grid(row=11,column=0)
                          

window.mainloop()