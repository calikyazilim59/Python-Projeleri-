import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

# Kullanıcıları saklamak için liste
users = [("admin","123456")]

def kullanici_giris_ekrani():
    login=ctk.CTk()
    login.geometry("600x400")
    login.title("Kullanıcı Giriş Ekranı")
    
    etiket=ctk.CTkLabel(login, text="Çalık Yazılım Şirketi Sistem Girişi", font=('open sans',20))
    etiket.grid(row=0,column=0,padx=40,pady=20,columnspan=2)
    
    login_username=ctk.CTkLabel(login, text="Kullanıcı Adınız:", font=('open sans',17))
    login_username.grid(row=1,column=0,padx=20,pady=20)
    login_username_entry=ctk.CTkEntry(login,font=('open sans',17))
    login_username_entry.grid(row=1,column=1,padx=20,pady=20)
    
    login_password=ctk.CTkLabel(login, text="Kullanıcı Şifreniz:", font=('open sans',17))
    login_password.grid(row=2,column=0,padx=20,pady=20)
    login_password_entry=ctk.CTkEntry(login,font=('open sans',17),show="*")
    login_password_entry.grid(row=2,column=1,padx=20,pady=20)

    def kullanici_giris_ekrani_sorgulama():
        login_user_entry=login_username_entry.get()
        login_pass_entry=login_password_entry.get()
        
        if (login_user_entry , login_pass_entry) in users:
            messagebox.showinfo("Hoşgeldiniz","Başarılı bir şekilde giriş yaptınız")
            login.destroy()
        else:
            messagebox.showerror("Hata","Kullanıcı bilgileriniz yanlış veya böyle bir kullanıcı yok")
            
    login_button = ctk.CTkButton(login, text="Giriş Yap", command=kullanici_giris_ekrani_sorgulama)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

    login.mainloop()

kullanici_giris_ekrani()


