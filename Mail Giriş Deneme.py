print("Yıldızkent Mail Hesabınıza Hoşgeldiniz")

mail1="orhancalik17@yıldızkent.com"
mail1_sifre="Yldz_0059"
mail2="orhancalik65@yıldızkent.com"
mail2_sifre="Yldz.kent.47"

kullanıcı_adı=input('Lütfen kullanıcı adınızı giriniz: ').lower()
kullanıcı_sifre=input('Lütfen kullanıcı şifrenizi giriniz: ')
print("\n")

if(kullanıcı_adı==mail1 or kullanıcı_adı==mail2):
    if(kullanıcı_sifre==mail1_sifre or kullanıcı_sifre==mail2_sifre):
        print("Hesabınıza giriş yapıldı..")
        
    elif(kullanıcı_sifre != mail1_sifre or kullancı_sifre != mail2_sifre):
        print("Hesabınızın şifresi yanlış girilmiştir, lütfen kontrol ediniz.")
        
elif(kullanıcı_adı != mail1 or kullanıcı_adı != mail2):
    print("Hesabınızın kullanıcı adını yanlış girdiniz. Lütfen kontrol edip tekrar deneyiniz.")
    