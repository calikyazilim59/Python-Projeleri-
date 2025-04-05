import tkinter as tk
import customtkinter as ctk
import sqlite3
from tkinter import messagebox

ctk.set_appearance_mode("dark")

# SQLite Veritabanı Bağlantısı
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    fullname TEXT,
    phone TEXT,
    address TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bookname TEXT,
    bookwriter TEXT,
    bookpagesnumber TEXT,
    bookgenre TEXT,
    booksummary TEXT
    )
""")
    
conn.commit()

# Giriş Ekranı Fonksiyonu
def login_screen():
    login_win = ctk.CTk()
    login_win.title("Giriş Yap")
    login_win.geometry("400x300")

    login_user=ctk.CTkLabel(login_win, text="Kullanıcı Adı:", font=('open sans', 15))
    login_user.grid(row=1,column=0,padx=20,pady=10)
    entry_login_user = ctk.CTkEntry(login_win, font=('open sans', 15))
    entry_login_user.grid(row=1,column=1,padx=20,pady=10)

    login_pass=ctk.CTkLabel(login_win, text="Şifre:", font=('open sans', 15))
    login_pass.grid(row=2,column=0,padx=20,pady=10)
    entry_login_pass = ctk.CTkEntry(login_win, show="*", font=('open sans', 15))
    entry_login_pass.grid(row=2,column=1,padx=20,pady=10)

    def login():
        username = entry_login_user.get()
        password = entry_login_pass.get()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            login_win.destroy()
            add_books_screen()  # Kitap ekleme ekranını aç
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")

    connect_buton=ctk.CTkButton(login_win, text="Giriş Yap", command= login)
    connect_buton.grid(row=3,column=0,padx=20,pady=10)
    uyelik_buton=ctk.CTkButton(login_win, text="Üye Ol", command=lambda: [login_win.destroy(), register_screen()])
    uyelik_buton.grid(row=3,column=1,padx=20,pady=10)
    login_win.mainloop()

# Kayıt Ekranı Fonksiyonu
def register_screen():
    register_win = ctk.CTk()
    register_win.title("Üyelik Oluştur")
    register_win.geometry("400x500")

    username=ctk.CTkLabel(register_win, text="Kullanıcı Adı:",font=('open sans',17))
    username.grid(row=0,column=0,padx=40,pady=10)
    entry_username = ctk.CTkEntry(register_win,font=('open sans',17))
    entry_username.grid(row=0,column=1,padx=40,pady=10)

    password=ctk.CTkLabel(register_win, text="Şifre:",font=('open sans',17))
    password.grid(row=1,column=0,padx=40,pady=10)
    entry_password = ctk.CTkEntry(register_win, show="*",font=('open sans',17))
    entry_password.grid(row=1,column=1,padx=40,pady=10)

    fullname=ctk.CTkLabel(register_win, text="Ad Soyad:",font=('open sans',17))
    fullname.grid(row=2,column=0,padx=40,pady=10)
    entry_fullname = ctk.CTkEntry(register_win,font=('open sans',17))
    entry_fullname.grid(row=2,column=1,padx=40,pady=10)

    phone=ctk.CTkLabel(register_win, text="Telefon:",font=('open sans',17))
    phone.grid(row=3,column=0,padx=40,pady=10)
    entry_phone = ctk.CTkEntry(register_win,font=('open sans',17))
    entry_phone.grid(row=3,column=1,padx=40,pady=10)

    address=ctk.CTkLabel(register_win, text="Adres:",font=('open sans',17))
    address.grid(row=4,column=0,padx=40,pady=10)
    entry_address = ctk.CTkEntry(register_win,font=('open sans',17))
    entry_address.grid(row=4,column=1,padx=40,pady=10)

    def register():
        username = entry_username.get()
        password = entry_password.get()
        fullname = entry_fullname.get()
        phone = entry_phone.get()
        address = entry_address.get()

        if username and password and fullname and phone and address:
            try:
                cursor.execute("INSERT INTO users (username, password, fullname, phone, address) VALUES (?, ?, ?, ?, ?)",
                               (username, password, fullname, phone, address)) #veritabanına verilerin eklenmesi için döndürülen komut
                conn.commit() #değişiklikleri veritabanına kaydeder
                messagebox.showinfo("Başarılı", "Üyelik oluşturuldu!")
                register_win.destroy()
                login_screen()
            except sqlite3.IntegrityError: #aynı kullanıcı adıyla ekleme yapılmaya çalışılırsa hata döndürülmesi için yazılan komut
                messagebox.showerror("Hata", "Bu kullanıcı adı zaten alınmış!")
        else:
            messagebox.showwarning("Hata", "Tüm alanları doldurun!")

    register_buton=ctk.CTkButton(register_win, text="Kayıt Ol", command=register)
    register_buton.grid(row=5,column=0,padx=10,pady=10)
    back_buton=ctk.CTkButton(register_win, text="Geri Dön", command=lambda: [register_win.destroy(), login_screen()])
    back_buton.grid(row=5,column=1,padx=10,pady=10)
    register_win.mainloop()
    
def add_books_screen():
    add_book=ctk.CTkToplevel()
    add_book.geometry("650x500")
    add_book.title("Kitap Kayıt Otomasyonu")
    
    bookname=ctk.CTkLabel(add_book, text="Kitap Adı:",font=('open sans',17))
    bookname.grid(row=0,column=0,padx=40,pady=10)
    entry_bookname = ctk.CTkEntry(add_book,font=('open sans',17))
    entry_bookname.grid(row=0,column=1,padx=40,pady=10)
    
    bookwriter=ctk.CTkLabel(add_book, text="Kitap Yazarı:",font=('open sans',17))
    bookwriter.grid(row=1,column=0,padx=40,pady=10)
    entry_bookwriter = ctk.CTkEntry(add_book,font=('open sans',17))
    entry_bookwriter.grid(row=1,column=1,padx=40,pady=10)
    
    book_pages_number=ctk.CTkLabel(add_book, text="Kitap Sayfa Sayısı:",font=('open sans',17))
    book_pages_number.grid(row=2,column=0,padx=40,pady=10)
    entry_book_pages_number= ctk.CTkEntry(add_book,font=('open sans',17))
    entry_book_pages_number.grid(row=2,column=1,padx=40,pady=10)
    
    book_genre=ctk.CTkLabel(add_book, text="Kitap Türü:",font=('open sans',17))
    book_genre.grid(row=3,column=0,padx=40,pady=10)
    booksgenre=["öykü","roman","savaş","macera","gezi","anı","dini","bilgi","bilim-kurgu","diğer"]
    book_genre_combo=ctk.CTkComboBox(add_book, values=booksgenre ,font=('open sans',17))
    book_genre_combo.grid(row=3,column=1,padx=40,pady=10)
    
    book_summary_label=ctk.CTkLabel(add_book, text="Kitap Özeti:",font=('open sans',17))
    book_summary_label.grid(row=4,column=0,padx=40,pady=10)
    book_summary=ctk.CTkTextbox(add_book, font=('open sans',17),height=200, width=300)
    book_summary.grid(row=4,column=1,padx=40,pady=10)

    def add_books():
        bookname=entry_bookname.get()
        bookwriter=entry_bookwriter.get()
        bookpagesnumber=entry_book_pages_number.get()
        bookgenre=book_genre_combo.get()
        booksummary=book_summary.get("1.0","end")
        
        if bookname and bookwriter and bookpagesnumber and bookgenre and booksummary:
                cursor.execute("INSERT INTO books (bookname,bookwriter,bookpagesnumber,bookgenre,booksummary) VALUES (?, ?, ?, ?, ?)",
                               (bookname,bookwriter,bookpagesnumber,bookgenre,booksummary)) #veritabanına verilerin eklenmesi için döndürülen komut
                conn.commit() #değişiklikleri veritabanına kaydeder
                messagebox.showinfo("Başarılı", "Kitap Kaydedildi !")
                
                entry_bookname.delete(0,tk.END)
                entry_bookwriter.delete(0,tk.END)
                entry_book_pages_number.delete(0,tk.END)
                book_genre_combo.set("")
                book_summary.delete(1.0,tk.END)
                
        else:
            messagebox.showwarning("Hata", "Tüm alanları doldurun!")
        
            
    add_button=ctk.CTkButton(add_book,text="Kaydet",font=('open sans',17), command=add_books)
    add_button.grid(row=5,column=0,padx=40,pady=10)
    exit_button=ctk.CTkButton(add_book,text="Çıkış Yap", font=('open sans',17), command=lambda: [add_book.destroy(), login_screen()])
    exit_button.grid(row=5,column=1,padx=40,pady=10)
    
# İlk olarak giriş ekranını aç
login_screen()

# Veritabanı bağlantısını kapat
conn.close()
