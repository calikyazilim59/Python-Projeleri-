import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

# CustomTkinter Temasını Ayarla
ctk.set_appearance_mode("dark")  # "light" veya "dark" seçilebilir
ctk.set_default_color_theme("blue")

# Ana Pencere
app = ctk.CTk()
app.title("Kütüphane - Kitap Ekle")
app.geometry("800x600")  # Genişliği artırıldı
app.attributes('-alpha', 0.75)  # %50 şeffaflık

# Ana Çerçeve
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Sol Bölüm (Kitap Bilgileri)
left_frame = ctk.CTkFrame(main_frame, width=350)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Başlık
title_label = ctk.CTkLabel(left_frame, text="Kitap Ekle", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Giriş Alanları
entries = {}
fields = ["Kitap Adı", "Yazar", "Yayınevi", "Tür", "Sayfa Sayısı", "Sınıf Düzeyi"]
for field in fields:
    frame = ctk.CTkFrame(left_frame)
    frame.pack(pady=5, padx=20, fill="x")
    label = ctk.CTkLabel(frame, text=field, width=120)
    label.pack(side="left", padx=10)
    entry = ctk.CTkEntry(frame, width=180)
    entry.pack(side="right", padx=10)
    entries[field] = entry

# Kitap Görseli Seçme
img_label = ctk.CTkLabel(left_frame, text="Kitap Görseli Eklenmedi", width=150, height=200)
img_label.pack(pady=10)

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((150, 200))
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img, text="")
        img_label.image = img

img_button = ctk.CTkButton(left_frame, text="Görsel Seç", command=select_image)
img_button.pack(pady=5)

# Butonlar
button_frame = ctk.CTkFrame(left_frame)
button_frame.pack(pady=20)

def clear_form():
    for entry in entries.values():
        entry.delete(0, "end")
    img_label.configure(image=None, text="Kitap Görseli Eklenmedi")

def save_data():
    data = {field: entry.get() for field, entry in entries.items()}
    print("Kaydedilen Veriler:", data)
    # Burada veritabanına veya dosyaya kayıt işlemi eklenebilir
    clear_form()

save_button = ctk.CTkButton(button_frame, text="Ekle", command=save_data)
save_button.pack(side="left", padx=10)

clear_button = ctk.CTkButton(button_frame, text="Temizle", command=clear_form)
clear_button.pack(side="right", padx=10)

button_frame.pack()

# Sağ Bölüm (Özet Alanı)
right_frame = ctk.CTkFrame(main_frame, width=350)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

summary_label = ctk.CTkLabel(right_frame, text="Kitap Özeti", font=("Arial", 16, "bold"))
summary_label.pack(pady=10)

summary_text = ctk.CTkTextbox(right_frame, width=300, height=400)
summary_text.pack(pady=10, padx=10, fill="both", expand=True)

app.mainloop()
