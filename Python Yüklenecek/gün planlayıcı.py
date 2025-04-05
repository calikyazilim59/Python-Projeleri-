from datetime import datetime

gun_plani=[]

def zaman_kontrol(input_date_time):
    try:
        # Kullanıcının formatta giriş yapıp yapmadığını kontrol et
        datetime.strptime(input_date_time, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False
    

#Aktivite ekleyelim
def aktivite_ekle(aktivite,datetime):
    gun_plani.append({"time": datetime, "aktivite":aktivite})
    print(f"{aktivite} aktivitesi {datetime} eklendi!")
    
#Akriviteleri gösterme fonksiyonu
def aktivite_goster():
    print("Günlük planınız: \n")
    if not gun_plani:
        print("Henüz bir plan eklenmedi...")
    else:
        for plan in gun_plani:
            print(f"{plan['time']} - {plan['aktivite']}")
            
#Menü döngüsü oluşturuyoruz
while True:
    print("\nGün Planlayıcı")
    print("1. Aktivite Ekle")
    print("2. Planı Göster")
    print("3. Çıkış")
    
    menu_secim=input("Lütfen planlayıcı programınızda seçiminizi yapınız: ")
    if menu_secim == "1":
        aktivite = input("Eklemek istediğiniz aktivite: ")
        while True:
            date_time = input("Tarih ve saat girin (YYYY-MM-DD HH:MM formatında): ")
            if zaman_kontrol(date_time):
                break
            else:
                print("Hatalı format! Lütfen 'YYYY-MM-DD HH:MM' formatını kullanın.")
        aktivite_ekle(aktivite, date_time)
        
    elif menu_secim == "2":
        aktivite_goster()
    elif menu_secim == "3":
        print("Planlayıcıdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin!")
    
    