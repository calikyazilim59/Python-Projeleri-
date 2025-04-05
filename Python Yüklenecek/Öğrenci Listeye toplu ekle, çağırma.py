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

    # Öğrenciler ekleyelim
    anahtar=True
    while anahtar:
        ogrenci_no=input('Öğrenci numarası giriniz: ')
        ogrenci_adi=input('Öğrenci adını giriniz: ')
        ogrenci_soyadi=input('Öğrenci soyadını giriniz: ')
        ogrenci_sinif=input('Öğrenci sınıfını giriniz (format:7X): ')

        add_student(ogrenci_no, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif)

        yeni_kayit=input('Yeni öğrenci kaydı yapmak ister misiniz(evet/hayır): ')
        if(yeni_kayit=="evet"):
            anahtar=True
        elif(yeni_kayit=="hayır"):
            anahtar=False

# Öğrenci listesini yazdırma
print("Öğrenci Listesi:")
for student in students:
    print(student)
    
 