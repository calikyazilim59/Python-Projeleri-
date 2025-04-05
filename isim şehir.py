def isim_sehir_oyunu():
    harf = input("oyun başlasın! Lütfen bir harf seçin:").upper()
    isimler = []
    sehirler = []
    while True:
        isim = input(f"{harf} harfi ile bir isim söyleyin:").capitalize()
        if isim in isimler:
            print("bu isim zaten söylendi, tekrar deneyin.")
            continue
        if isim[0].upper() !=harf:
            print(harf,"harfi ile başlamıyor,tekrar deneyin.")
            continue
        isimler.append(isim)
        sehir = input(f"{harf} harfi ile bir şehir söyleyin:")capitalize()