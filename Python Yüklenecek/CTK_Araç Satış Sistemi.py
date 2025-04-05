import tkinter as tk
import customtkinter as ctk
from tkinter import ttk,messagebox

ctk.set_appearance_mode("dark")

def bilgileri_isle():
    marka=marka_entry.get()
    modeli=modeli_entry.get()
    model_yili=model_yili_entry.get()
    kilometresi=kilometresi_entry.get()
    yakiti=yakiti_entry.get()
    vitesi=vitesi_entry.get()
    renk=renk_combo.get()
    
    if marka and modeli and model_yili and kilometresi and yakiti and vitesi and renk:
        tablo.insert("","end", values=(marka,modeli,model_yili,kilometresi,yakiti,vitesi,renk))
        
        marka_entry.delete(0,tk.END)
        modeli_entry.delete(0,tk.END)
        model_yili_entry.delete(0,tk.END)
        kilometresi_entry.delete(0,tk.END)
        yakiti_entry.delete(0,tk.END)
        vitesi_entry.delete(0,tk.END)
        renk_combo.set('')
    else:
        messagebox.showwarning("HATA","Lütfen gerekli tüm alanları doldurmadan kayıt oluşturmayınız")

form=ctk.CTk()
form.geometry("750x500")
form.title("Çalık Showroom - İkinci El Araba Bayii Satış Platformu")

marka=ctk.CTkLabel(form,text="Araç Markası: ",font=('open sans',20))
marka.grid(row=0,column=0,padx=10,pady=5)
marka_entry=ctk.CTkEntry(form,font=('open sans',20))
marka_entry.grid(row=0,column=1,padx=10,pady=5)

modeli=ctk.CTkLabel(form,text="Araç Modeli: ",font=('open sans',20))
modeli.grid(row=1,column=0,padx=10,pady=5)
modeli_entry=ctk.CTkEntry(form,font=('open sans',20))
modeli_entry.grid(row=1,column=1,padx=10,pady=5)

model_yili=ctk.CTkLabel(form,text="Model Yılı: ",font=('open sans',20))
model_yili.grid(row=2,column=0,padx=10,pady=5)
model_yili_entry=ctk.CTkEntry(form,font=('open sans',20))
model_yili_entry.grid(row=2,column=1,padx=10,pady=5)

kilometresi=ctk.CTkLabel(form,text="Kilometresi: ",font=('open sans',20))
kilometresi.grid(row=3,column=0,padx=10,pady=5)
kilometresi_entry=ctk.CTkEntry(form,font=('open sans',20))
kilometresi_entry.grid(row=3,column=1,padx=10,pady=5)

yakiti=ctk.CTkLabel(form,text="Yakıtı: ",font=('open sans',20))
yakiti.grid(row=4,column=0,padx=10,pady=5)
yakiti_entry=ctk.CTkEntry(form,font=('open sans',20))
yakiti_entry.grid(row=4,column=1,padx=10,pady=5)

vitesi=ctk.CTkLabel(form,text="Vitesi: ",font=('open sans',20))
vitesi.grid(row=5,column=0,padx=10,pady=5)
vitesi_entry=ctk.CTkEntry(form,font=('open sans',20))
vitesi_entry.grid(row=5,column=1,padx=10,pady=5)

renk=ctk.CTkLabel(form,text="Araç Rengi: ",font=('open sans',20))
renk.grid(row=6,column=0,padx=10,pady=5)
combo_baslik=["Siyah","Beyaz","Kırmızı","Gri","Sarı","Mavi","Lacivert","Turuncu","Yeşil","Bordo"]
renk_combo=ctk.CTkComboBox(form,font=('open sans',20),values=combo_baslik)
renk_combo.grid(row=6,column=1,padx=10,pady=5)

ekle_buton=ctk.CTkButton(form,text="Sisteme Kaydet", font=('open sans',15),command=bilgileri_isle)
ekle_buton.grid(row=7,column=0,columnspan=2,padx=10,pady=5)

tablo=ctk.CTkFrame(form)
tablo.grid(row=8,column=0,columnspan=6,padx=10,pady=10)

tablo_basliklari=("Araç Markası","Araç Modeli","Model Yılı","Kilometresi","Araç Yakıtı","Araç Vitesi","Araç Rengi")
tablo=ttk.Treeview(tablo,columns=tablo_basliklari, show="headings", height=20)

for col in tablo_basliklari:
    tablo.heading(col,text=col)
    tablo.column(col, width=250,anchor="center")
    
tablo.pack()
form.mainloop()