print("Yıldızkent Yeni Öğrenci Kayıt Sistemine Hoşgeldiniz")

ogr_no_list=[]
ogr_adsoyad_list=[]
ogr_sınıf_list=[]

def kayıt_ekle():
    
    anahtar=True
    
    while anahtar:
        
        sayac=int(-1)
        
        ogr_no=int(input("Öğrenci numaranızı giriniz: "))
        ogr_adsoyad=input("Öğrenci adı soyadı nedir: ")
        ogr_sınıf=input("Öğrenci kaçıncı sınıfta okuyor: ")
        
        ogr_no_list.append(ogr_no)
        ogr_adsoyad_list.append(ogr_adsoyad)
        ogr_sınıf_list.append(ogr_sınıf)
        
        print("\n")
        
        print("Öğrenci no:",ogr_no_list[sayac],"\nÖğrenci adı soyadı:",ogr_adsoyad_list[sayac],"\nÖğrenci sınıfı:",ogr_sınıf_list[sayac])
        
        sayac=(sayac+1)
        
        yeni_kayıt=input("Yeni kayıt yapmak istiyor musunuz(evet/hayır): ")
        
        if(yeni_kayıt=="evet"):
            
            anahtar=True
            
        elif(yeni_kayıt=="hayır"):
                
            anahtar=False
            
kayıt_ekle()
    
