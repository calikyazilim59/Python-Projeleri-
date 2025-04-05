from random import randint
 
kolaySeviyeHak = 10
zorSeviyeHak = 5
 
 
# zorluk seviyesi yaz
def zorluk_seviyesi():
    seviye_tercihi = input("Oyun zorluğunu seçiniz. 'Kolay','Zor'\n")
    if seviye_tercihi == "kolay":
        print("Oyunu kazanabilmek için 10 hakkın var!")
        return kolaySeviyeHak
    else:
        print("Oyunu kazanabilmek için 5 hakkın var!")
        return zorSeviyeHak
 
 
def tahmin_oyunu():
    print("Bilgisayar 1 ile 100 arasında bir sayıyı aklından tuttu.")
    bilgisayar_tuttu = randint(1, 100)
    devam_et = True
    kalan_hak = zorluk_seviyesi()
 
    while devam_et:
        senin_tahminin = int(input("Bilgisayarın aklından tuttuğu sayı nedir?"))
        if senin_tahminin > bilgisayar_tuttu:
            print("Fazla attın, bir sonrakine küçük bir sayı seç!\n")
            kalan_hak -= 1
        elif senin_tahminin < bilgisayar_tuttu:
            print("Ufak attın, bir dahakine büyük bir sayı seç!\n")
            kalan_hak -= 1
        else:
            print("Tabrikler, kazandın!")
            devam_et = False
            yeni_oyun = input("Yeni bir oyun oynamaya ne dersin? 'Evet','Hayır'\n")
            if yeni_oyun == "evet":
                tahmin_oyunu()
            else:
                devam_et = False
 
        if kalan_hak == 0:
            print("Hakkın bitti, oyunu kaybettin!")
            devam_et = False
            yeni_oyun = input("Yeni bir oyun oynamaya ne dersin? 'Evet','Hayır'\n")
            if yeni_oyun == "evet":
                tahmin_oyunu()
            else:
                devam_et = False
 
 
tahmin_oyunu()