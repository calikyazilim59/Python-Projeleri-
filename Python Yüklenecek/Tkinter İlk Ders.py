import tkinter as tk

def bilgileri_al():
    isim=isim_entry.get()
    soyisim=soyisim_entry.get()
    sonuc_label.config(text=f"Merhaba, {isim} {soyisim} !")
    
form=tk.Tk()
form.geometry("400x200")
form.title('Tkinter Grafik Arayüz Dersleri')

etiket=tk.Label(form,text="TKINTER ÖĞRENİYORUM", font=('Arial', 12), fg='blue')
etiket.pack()

isim_label=tk.Label(form,text="İsim:", font=('Arial',10))
isim_label.pack()
isim_entry=tk.Entry(form,font=('Arial',10))
isim_entry.pack()

soyisim_label=tk.Label(form,text="Soyisim:", font=('Arial',10))
soyisim_label.pack()
soyisim_entry=tk.Entry(form,font=('Arial',10))
soyisim_entry.pack()

buton=tk.Button(form,text="Bilgileri Al", font=('Arial',10), command=bilgileri_al)
buton.pack()

sonuc_label=tk.Label(form,text="", font=('Arial',10), fg="blue")
sonuc_label.pack()

form.mainloop()