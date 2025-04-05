import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox


def bilgileri_isle():
    adsoyad = ad_soyad_entry.get()
    ogrenci = ogrencisi_entry.get()
    ziyaret = ziyaret_edilen_entry.get()
    saat = ziyaret_saati_combobox.get()
    
    if adsoyad and ogrenci and ziyaret and saat:
        # Bilgileri tabloya ekleyelim
        tablo.insert("", "end", values=(adsoyad, ogrenci, ziyaret, saat))

        # Giriş kutularını temizle
        ad_soyad_entry.delete(0, tk.END)
        ogrencisi_entry.delete(0, tk.END)
        ziyaret_edilen_entry.delete(0, tk.END)
        ziyaret_saati_combobox.set('')  # Başlangıçta boş bırakalım
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun!")
        
def bilgileri_sil():
    secili_oge = tablo.selection()
    if secili_oge:
        tablo.delete(secili_oge)
    else:
        messagebox.showwarning("Hata", "Herhangi bir öğe seçilmeden silme işlemi yapılamaz")
    
    
# CustomTkinter ayarları
ctk.set_appearance_mode("dark")  # Dark mode için "dark" kullanabilirsiniz


form = ctk.CTk()
form.geometry("900x600")
form.title("Ziyaretçi Kayıt Sistemi")

# Etiketler ve giriş kutuları
ad_soyad = ctk.CTkLabel(form, text="Ad Soyad:", font=('Arial', 15))
ad_soyad.grid(row=0, column=0, padx=5, pady=5)
ad_soyad_entry = ctk.CTkEntry(form, font=('Arial', 15))
ad_soyad_entry.grid(row=0, column=1, padx=5, pady=5)

ogrencisi = ctk.CTkLabel(form, text="Öğrencisi:", font=('Arial', 15))
ogrencisi.grid(row=1, column=0, padx=5, pady=5)
ogrencisi_entry = ctk.CTkEntry(form, font=('Arial', 15))
ogrencisi_entry.grid(row=1, column=1, padx=5, pady=5)

ziyaret_edilen = ctk.CTkLabel(form, text="Ziyaret Edilen Öğretmen:", font=('Arial', 15))
ziyaret_edilen.grid(row=2, column=0, padx=5, pady=5)
ziyaret_edilen_entry = ctk.CTkEntry(form, font=('Arial', 15))
ziyaret_edilen_entry.grid(row=2, column=1, padx=5, pady=5)

ziyaret_saati = ctk.CTkLabel(form, text="Ziyaret Saati:", font=('Arial', 15))
ziyaret_saati.grid(row=3, column=0, padx=5, pady=5)
combo_veriler = ["08.00-09.00", "09.00-10.00", "10.00-11.00", "11.00-12.00", "12.00-13.00", "13.00-14.00", "14.00-15.00", "15.00-16.00", "16.00-17.00"]
ziyaret_saati_combobox = ctk.CTkComboBox(form, font=('Arial', 15), values=combo_veriler, state="readonly")
ziyaret_saati_combobox.grid(row=3, column=1, padx=5, pady=5)

# Butonlar
buton = ctk.CTkButton(form, text="Bilgileri İşle", font=('Arial', 15), command=bilgileri_isle)
buton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

buton2 = ctk.CTkButton(form, text="Bilgileri Sil", font=('Arial', 15), command=bilgileri_sil)
buton2.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

# TABLO (Treeview)
tablo_frame = ctk.CTkFrame(form)  # Frame içinde tabloyu tutuyoruz
tablo_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Sütun başlıkları
basliklar = ("Ad Soyad", "Öğrencisi", "Ziyaret Edilen", "Saat")
tablo = ttk.Treeview(tablo_frame, columns=basliklar, show="headings", height=10)

# Sütun genişlikleri
for col in basliklar:
    tablo.heading(col, text=col)
    tablo.column(col, width=200, anchor="center")

tablo.pack()  # Frame içinde gösterilen tabloyu pack ile ekliyoruz
form.mainloop()
