# Ayakkabı bilgilerini saklamak için bir liste
ayakkabi_listesi = []
# Ayakkabı ekleme fonksiyonu
def ayakkabi_ekle(marka, numara, renk, fiyat):
    ayakkabi = {
        "marka": marka,
        "numara": numara,
        "renk": renk,
        "fiyat": fiyat
    }
    ayakkabi_listesi.append(ayakkabi)
    print(f"{marka} markalı ayakkabı listeye eklendi.")
# Listeyi görüntüleme fonksiyonu
def listeyi_goster():
    if not ayakkabi_listesi:
        print("Liste boş!")
        return
    print("\n--- Ayakkabı Listesi ---")
    for ayakkabi in ayakkabi_listesi:
        print(f"Marka: {ayakkabi['marka']}, Numara: {ayakkabi['numara']}, Renk: {ayakkabi['renk']}, Fiyat: {ayakkabi['fiyat']} TL")
# Fiyat aralığına göre filtreleme
def fiyata_gore_filtrele(min_fiyat, max_fiyat):
    print(f"\n--- {min_fiyat}-{max_fiyat} TL Arasındaki Ayakkabılar ---")
    bulundu = False
    for ayakkabi in ayakkabi_listesi:
        if min_fiyat <= ayakkabi['fiyat'] <= max_fiyat:
            bulundu = True
            print(f"Marka: {ayakkabi['marka']}, Numara: {ayakkabi['numara']}, Renk: {ayakkabi['renk']}, Fiyat: {ayakkabi['fiyat']} TL")
    if not bulundu:
        print("Bu fiyat aralığında ayakkabı bulunamadı.")
# Menü fonksiyonu
def menu():
    while True:
        print("\n1. Ayakkabı Ekle")
        print("2. Listeyi Göster")
        print("3. Fiyata Göre Filtrele")
        print("4. Çıkış")
        secim = input("Seçiminizi yapın (1-4): ")
        if secim == "1":
            marka = input("Marka: ")
            numara = int(input("Numara: "))
            renk = input("Renk: ")
            fiyat = float(input("Fiyat: "))
            ayakkabi_ekle(marka, numara, renk, fiyat)
        elif secim == "2":
            listeyi_goster()
        elif secim == "3":
            min_fiyat = float(input("Minimum fiyat: "))
            max_fiyat = float(input("Maksimum fiyat: "))
            fiyata_gore_filtrele(min_fiyat, max_fiyat)
        elif secim == "4":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")
# Programı başlat
menu()