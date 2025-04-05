def isim_sehir_oyunu():
    # Kullanıcıdan oyun için başlangıç harfini alıyoruz
    harf = input("Oyun başlasın! Lütfen bir harf seçin: ").upper()
    
    # Söylenen isim ve şehirleri saklamak için liste
    isimler = []
    sehirler = []
    
    # Oyun devam ettiği sürece
    while True:
        # İsim sormak
        isim = input(f"{harf} harfi ile bir isim söyleyin: ").capitalize()
        if isim in isimler:
            print("Bu isim zaten söylendi, tekrar deneyin.")
            continue
        if isim[0].upper() != harf:
            print(harf," harfi ile başlamıyor, tekrar deneyin.")
            continue
        
        isimler.append(isim)  # İsim kaydediliyor
        
        # Şehir sormak
        sehir = input(f"{harf} harfi ile bir şehir söyleyin: ").capitalize()
        if sehir in sehirler:
            print("Bu şehir zaten söylendi, tekrar deneyin.")
            continue
        if sehir[0].upper() != harf:

print(f"{harf} harfi ile başlamıyor, tekrar deneyin.")
            continue
        
        sehirler.append(sehir)  # Şehir kaydediliyor
        
        # Sonraki harfi belirleyelim: Şehirlerin son harfi
        harf = sehir[0].upper()
        print(f"Şimdi {harf} harfi ile devam edin!")
        
        # Kullanıcı oyunu bırakmak isterse, programı bitirebiliriz
        devam = input("Devam etmek ister misiniz? (Evet/Hayır): ").lower()
        if devam != "evet":
            print("Oyun sona erdi.")
            break

# Oyunu başlatma
isim_sehir_oyunu()