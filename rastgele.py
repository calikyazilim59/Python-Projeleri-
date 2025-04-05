students=[]


def add_student(student_no,name,surname,class_name):
    
    student={
        "öğrenci no":student_no,
        "adı":name,
        "soyadı":surname,
        "sınıfı":class_name
        }
    
    students.append(student)
    
    
def add_students_lopp():
    anahtar=True
    while anahtar:
            
        ogrenci_no=input('öğrenci numarası giriniz:')
        ogrenci_adi=input('öğrenci adını giriniz:')
        ogrenci_soyadi=input('öğrenci soyadını giriniz:')
        ogrenci_sinif=input('öğrenci sınıfını giriniz:')
            
            
        add_student(ogrenci_no,ogrenci_adi,ogrenci_soyadi,ogrenci_sinif)
            
            
        yeni_kayit=input("yeni öğrenci kaydı yapmak ister misiniz? (evet/hayır)
        if yeni_kayit.lower()=="evet":
            anahtar=true
            elif yeni_kayit.lower()=="hayır":
                anahtar=False