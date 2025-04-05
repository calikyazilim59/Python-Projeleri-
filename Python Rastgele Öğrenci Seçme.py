import random
print("Sınıftan Rastgele Öğrenci Seçme Uygulamasına Hoşgeldiniz")

sınıf_list=["Mauro ICARDI","Victor OSIMHEN","Gabriel SARA","Yunus AKGUN"]
secilenler=set()



def rastgele_eleman_sec():
    anahtar=True
    while anahtar:
        #random_choice=random.choice(sınıf_list)
        secilmemis_elemanlar=[eleman for eleman in sınıf_list if eleman not in secilenler]
        
        secilen_eleman=random.choice(secilmemis_elemanlar)
        secilenler.add(secilen_eleman)
        print("Rastgele seçilen öğrenci: ",secilen_eleman)
        
        
        
        yeni_secim=input('Yeniden bir öğrenci seçmek ister misiniz?(evet/hayır): ')
        if(yeni_secim=="evet"):
            anahtar=True
        elif(yeni_secim=="hayır"):
            anahtar=False

rastgele_eleman_sec()
        
