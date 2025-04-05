
import random
print("Rastgele Öğrenci Seçme Uygulaması")

sınıf_list=["rascıhsa","5-0","semih kiliçsoy","semıh kılıçsoy"]
secilenler_list=[]

def ogrenci_listele():
    anahtar=True
    while anahtar:
        
        secilen_eleman=random.choice(sınıf_list)
        sınıf_list.remove(secilen_eleman)
        print("\n")
        print("Rastgele seçilen öğrenci: ",secilen_eleman)
        
        yeni_secim=input('Yeniden bir öğrenci seçmek ister misiniz?(evet/hayır): ')
        if(yeni_secim=="evet"):
            anahtar=True
            if not sınıf_list:
                print("Listede seçilebilecek öğrenci kalmamıştır, sistemden çıkılıyor...")
                anahtar=False
            else:
                continue
        elif(yeni_secim=="hayır"):
            anahtar=False
            
ogrenci_listele()