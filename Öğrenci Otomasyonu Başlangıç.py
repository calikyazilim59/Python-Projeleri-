# Öğrenci listesi
students = []

# Öğrenci ekleme fonksiyonu
def add_student(student_no, name, surname, class_name):
    # Yeni öğrenci bilgilerini içeren sözlük
    student = {
        "Öğrenci No": student_no,
        "Adı": name,
        "Soyadı": surname,
        "Sınıfı": class_name
    }
    # Öğrenciyi listeye ekle
    students.append(student)

# Öğrenci kaydı alma ve ekleme döngüsü
def add_students_loop():
    anahtar = True
    while anahtar:
        # Kullanıcıdan öğrenci bilgilerini alıyoruz
        ogrenci_no = input('Öğrenci numarası giriniz: ')
        ogrenci_adi = input('Öğrenci adını giriniz: ')
        ogrenci_soyadi = input('Öğrenci soyadını giriniz: ')
        ogrenci_sinif = input('Öğrenci sınıfını giriniz : ')

        # Öğrenciyi listeye ekle
        add_student(ogrenci_no, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif)

        # Kullanıcıya yeni öğrenci ekleyip eklemek istemediğini soralım
        yeni_kayit = input('Yeni öğrenci kaydı yapmak ister misiniz? (evet/hayır): ')
        if yeni_kayit.lower() == "evet":
            anahtar = True
        elif yeni_kayit.lower() == "hayır":
            anahtar = False
        else:
            print("Lütfen 'evet' ya da 'hayır' yazınız.")

# Öğrenci numarasına göre öğrenci bilgilerini gösterme fonksiyonu
def find_student_by_number(student_no):
    for student in students:
        if student['Öğrenci No'] == student_no:
            return student
    return None  # Öğrenci bulunamazsa None döner

# Öğrenci numarasını girip öğrenciyi bulma ve bilgilerini yazdırma
def search_student():
    ogrenci_no = input("Öğrenci numarasını giriniz: ")
    student = find_student_by_number(ogrenci_no)
    
    if student:
        print("\nÖğrenci Bilgileri:")
        print("Öğrenci No:",student['Öğrenci No'], "Adı:",student['Adı'],"Soyadı:",student['Soyadı'],"Sınıfı:",student['Sınıfı'])
    else:
        print("Öğrenci numarası bulunamadı.")
        
def student_update():
    ogrenci_no= input("Öğrenci numarasını giriniz: ")
    student = find_student_by_number(ogrenci_no)
    
    if student:
        print("Güncelenecek öğrencinin Bilgileri")
        print("Öğrenci No:",student['Öğrenci No'], "Adı:",student['Adı'],"Soyadı:",student['Soyadı'],"Sınıfı:",student['Sınıfı'])
        ogrenci_no2 = input('Öğrenci numarası giriniz: ')
        ogrenci_adi2 = input('Öğrenci adını giriniz: ')
        ogrenci_soyadi2 = input('Öğrenci soyadını giriniz: ')
        ogrenci_sinif2 = input('Öğrenci sınıfını giriniz : ')
        
        student['Öğrenci No'] = ogrenci_no2
        student['Adı'] = ogrenci_adi2
        student['Soyadı'] = ogrenci_soyadi2
        student['Sınıfı'] = ogrenci_sinif2
        
        print("Güncelenen öğrencinin Bilgileri")
        print("Öğrenci No:",student['Öğrenci No'], "Adı:",student['Adı'],"Soyadı:",student['Soyadı'],"Sınıfı:",student['Sınıfı'])
    else:
        print("Öğrenci numarası bulunamadı.")
        
        
anahtar_loop=True
while anahtar_loop:
    islem_secim=input("Yapmak istediğiniz işlemi seçiniz(kayıt_ekle/kayıt_gör/kayıt_güncelle): ")
    if islem_secim.lower() == "kayıt_ekle":
        # Öğrenciler eklenmeye başlandığında listeyi yazdıralım
        add_students_loop()
    elif islem_secim.lower() == "kayıt_gör":
        # Öğrenci arama işlemi yapalım
        search_student()
    elif islem_secim.lower() == "kayıt_güncelle":
        # Öğrenci bilgileri güncelleme 
        student_update()


