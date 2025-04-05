import random
import string

mail_list=[]

def add_mail(mail_adres,mail_sifre):
    mail={"Mail Adres":mail_adres,
          "Mail Şifre":mail_sifre
          }
    mail_list.append(mail)


        
def güçlü_şifre_oluştur(uzunluk=12):
    # Şifre için kullanılacak karakter kümeleri
    küçük_harfler = string.ascii_lowercase
    büyük_harfler = string.ascii_uppercase
    rakamlar = string.digits
    semboller = string.punctuation

    # Tüm karakterlerin birleşimi
    tüm_karakterler = küçük_harfler + büyük_harfler + rakamlar + semboller

    # Rastgele şifreyi oluştur
    şifre = random.sample(tüm_karakterler, uzunluk)

    # Karakterleri karıştır ve şifreyi birleştir
    random.shuffle(şifre)
    return ''.join(şifre)

def mail_olusturma():
    
        mail_adi=input('Oluşturmak istediğiniz mail adresinizi giriniz: ')
        mail_sifresi=güçlü_şifre_oluştur()
        
        add_mail(mail_adi,mail_sifresi)
        
        print("Kullanıcı Blgileriniz")
        print("Kullanıcı Mail Adınız: ",mail_adi,"\nKullanıcı Şifreniz: ",mail_sifresi)
        
mail_olusturma()