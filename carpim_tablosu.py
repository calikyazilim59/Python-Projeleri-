import random

def carpmayi_sor(seviye):
    if seviye == 1:
        sayi1=random.randint(0,6)
        sayi2=random.randint(0,6)
        
    elif seviye == 2:
        sayi1=random.randint(0,15)
        sayi2=random.randint(0,15)
        
    elif seviye == 3:
        sayi1=random.randint(0,25)
        sayi2=random.randint(0,25)
        
    elif seviye == 4:
        sayi1=random.randint(0,100)
        sayi2=random.randint(0,100)
    
    islem=sayi1*sayi2
    cevap=int(input(f' {sayi1} ve {sayi2} çarpım sonucu kaçtır: '))
    
    if cevap == islem:
        print("Tebrikler, doğru cevap verdiniz")
        return True
    else:
        print(f"Yanlış cevap verdiniz, doğru cevap: {islem}")
        return False
def carpmayi_oyna():
    print("Çarpım Tablosu Oyunu Başlıyor!")
    seviye=int(input("Oyunda 4 seviye bulunmaktadır. Hangi seviyeden başlamak istersiniz? : "))
    if seviye==1:
        while True:
            carpmayi_sor(seviye)
            devam=input("Oyuna devam etmek ister misiniz(evet/hayır): ")
            if devam.lower() != "evet":
                print("Oyundan çıkılıyor")
                break
            else:
                continue
    elif seviye==2:
        while True:
            carpmayi_sor(seviye)
            devam=input("Oyuna devam etmek ister misiniz(evet/hayır): ")
            if devam.lower() != "evet":
                print("Oyundan çıkılıyor")
                break
            else:
                continue
    elif seviye==3:
        while True:
            carpmayi_sor(seviye)
            devam=input("Oyuna devam etmek ister misiniz(evet/hayır): ")
            if devam.lower() != "evet":
                print("Oyundan çıkılıyor")
                break
            else:
                continue
    elif seviye==4:
        while True:
            carpmayi_sor(seviye)
            devam=input("Oyuna devam etmek ister misiniz(evet/hayır): ")
            if devam.lower() != "evet":
                print("Oyundan çıkılıyor")
                break
            else:
                continue
# Oyunu başlat
carpmayi_oyna()