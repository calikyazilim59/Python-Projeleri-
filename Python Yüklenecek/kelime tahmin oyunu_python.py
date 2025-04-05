import random

def kelime_avi():
    adam_asmaca = [
        """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
        ]
    
    kelimeler = [
        "araba", "elma", "yazılım", "python", "arduino", "çanakkale", "deniz",
        "galatasaray", "ışık", "okul", "kitap", "bilgisayar", "kodlama", "oyun",
        "eğitim", "şehir", "tatil", "baba", "çocuk", "müzik", "teknoloji", "bulut",
        "ev", "şehir", "çiçek", "kamera", "spor", "gezegen", "yıldız", "masa"]
    kelime=random.choice(kelimeler).lower()
    kelime_uzunlugu=len(kelime)
    tahmin_edilen_harfler=[]
    tahmin_sayisi=0
    oyun_skor=(-1)
    print("Kelime tahmin oyununa hoş geldiniz")
    print("kelime",kelime_uzunlugu,"harften oluşmaktadır.")
    
    while True:
        insan_tahmin=input('Bir harf tahmin edin:').lower()
        tahmin_sayisi+=1
        if len(insan_tahmin)!=1:
            print("sadece bir harf girebilirsiniz")
            continue
        if insan_tahmin in tahmin_edilen_harfler:
            print("Daha önceden bu harfi girdiniz ")
            continue
        tahmin_edilen_harfler.append(insan_tahmin)
        if insan_tahmin in kelime:
            print("Doğru tahmin,kelimenin içinde bu harf var")
        else:
            print("bu harf kelime içinde yok")
            oyun_skor +=1
            print(adam_asmaca[oyun_skor])
        
        kapalı_kelime=""
        for harf in kelime:
            if harf in tahmin_edilen_harfler:
                kapalı_kelime+=harf
            else:
                kapalı_kelime+=" _ "
                
        print("Tahmin edilen kelime:",kapalı_kelime)
        
        if oyun_skor == 6:
            print("Kelimeyi doğru tahmin edemediniz, adamınız asıldı. Tekrar başlayınız")
            break
        if kapalı_kelime==kelime:
            print("Tebrikler, kelimenizi",tahmin_sayisi," denemede buldunuz")
            break
        
    yeni_oyun=input("Yeniden oynamak ister misiniz(evet/hayır): ")
    if yeni_oyun.lower()=="evet":
        kelime_avi()
    else:
        print("Oyundan çıkılıyor")
kelime_avi()
       
   
   