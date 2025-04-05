import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

# Kullanıcıları saklamak için liste
users = [("admin", "123456")]

def kullanici_giris_ekrani():
    login = ctk.CTk()
    login.geometry("550x400")
    login.title("Kullanıcı Giriş Ekranı")
    login.grid_columnconfigure(0, weight=1)
    login.grid_columnconfigure(1, weight=1)
    
    # Üst başlık
    etiket = ctk.CTkLabel(login, text="ÇALIK YAZILIM\nSistem Girişi",font=('Open Sans', 20, "bold"), text_color="orange")
    etiket.grid(row=0, column=0, columnspan=3, pady=15, sticky="n")

    # Kullanıcı Adı
    login_username = ctk.CTkLabel(login, text="Kullanıcı Adınız:", font=('Open Sans', 15))
    login_username.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    login_username_entry = ctk.CTkEntry(login, font=('Open Sans', 15), width=200)
    login_username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Şifre
    login_password = ctk.CTkLabel(login, text="Şifreniz:", font=('Open Sans', 15))
    login_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    login_password_entry = ctk.CTkEntry(login, font=('Open Sans', 15), show="*", width=200)
    login_password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Logo (Varsa)
    try:
        image = Image.open("kullanici.png")
        image = image.resize((150, 150), Image.LANCZOS)
        logo = ImageTk.PhotoImage(image)
        logo_label = ctk.CTkLabel(login, image=logo, text="")
        logo_label.grid(row=1, column=2, rowspan=2, padx=10, pady=10, sticky="w")
        logo_label.image = logo  # Referans tutarak görüntünün kaybolmasını engelle
    except Exception as hata:
        print("Logo yüklenemedi:", hata)

    # Kullanıcı doğrulama fonksiyonu
    def kullanici_giris_ekrani_sorgulama():
        login_user_entry = login_username_entry.get()
        login_pass_entry = login_password_entry.get()

        if (login_user_entry, login_pass_entry) in users:
            messagebox.showinfo("Hoşgeldiniz", "Başarıyla giriş yaptınız!")
            login.destroy()
        else:
            messagebox.showerror("Hata", "Kullanıcı bilgileriniz yanlış veya böyle bir kullanıcı yok")

    # Giriş Butonu
    login_button = ctk.CTkButton(login, text="Giriş Yap", command=kullanici_giris_ekrani_sorgulama, width=150)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

    login.mainloop()

kullanici_giris_ekrani()
