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
    kelimeler=["lily","fang","shelly","nita","colt","bull","brock","elprimo","barley","poco","rosa","dynamike","tick","8bit","rico","darryl","penny","carl","jacky","gus"]
    kelime=random.choice(kelimeler).lower()
    kelime_uzunlugu=len(kelime)
    tahmin_edilen_harfler=[]
    tahmin_sayisi=0
    oyun_skor=(-1)
    print("kelime tahmin oyununa hoşgeldiniz")
    print("kelime",kelime_uzunlugu,"harften oluşmaktadır.")
    

    while True:

        insan_tahmin=input('bir harf tahmin ediniz:').lower()
        tahmin_sayisi+=1
        if len(insan_tahmin)!=1:
            print("SADECE BİR HARF GİREBİLİRSİN KARDEŞ AKLIN YOK MU?!")
            continue
        if insan_tahmin in tahmin_edilen_harfler:
            print(" daha önce bu harf kullanıldı")
            continue
        tahmin_edilen_harfler.append(insan_tahmin)
        if insan_tahmin in kelime:
            print("doğru tahmin kelimmenin içindwe bu kelime var")
        else:
            print("bu harf yok")
            oyun_skor+=1 
            print(adam_asmaca[oyun_skor])
        kapalı_kelime=""
        for harf in kelime:
            if harf in tahmin_edilen_harfler:
                kapalı_kelime+=harf
            else:
                kapalı_kelime+="_"
                
        print(" tahmin edilen kelime:",kapalı_kelime)
        if oyun_skor==6:
            print("kelimeyi bulamadınız adamız GG oldu ")
            break
        if kapalı_kelime==kelime:
            print("tebrikler",tahmin_sayisi,"denmednenede buldunuz")
            break
    yeni_oyun=input("yeniden oynıycaymı??(evet/hayır): ")
    if yeni_oyun.lower()=="evet":
        kelime_avi()
    else:
        print("oyundan cıkıyoy")
kelime_avi()
          