import random
import string

def generate_strong_password():
    # Karakter setlerini tanımlıyoruz
    upper_case = string.ascii_uppercase  # Büyük harfler
    lower_case = string.ascii_lowercase  # Küçük harfler
    digits = string.digits                # Rakamlar
    special_characters = string.punctuation  # Özel karakterler

    # Şifrede bulunması gereken minimum bir büyük harf, bir rakam
    password = [
        random.choice(upper_case),  # En az bir büyük harf
        random.choice(lower_case),
        random.choice(digits)       # En az bir rakam
    ]
    
    # Kalan karakterleri rastgele seç
    all_characters = upper_case + lower_case + digits + special_characters
    password += random.choices(all_characters, k=6)  # Toplamda 8 karakter olacak şekilde tamamlıyoruz
    
    # Karakterleri karıştırarak rastgele bir sıraya koyuyoruz
    random.shuffle(password)
    
    # Şifreyi birleştirip döndürüyoruz
    return ''.join(password)

# Şifreyi oluşturup yazdırıyoruz
strong_password = generate_strong_password()
print("Güçlü şifreniz:", strong_password)