print("Türkçe dersinin karne notuna yansımasının hesaplanması")

sınav1=float(input('1. sınav notunuzu giriniz: '))
sınav2=float(input('2. sınav notunuzu giriniz: '))
sözlü1=float(input('1. sözlü notunuzu giriniz: '))
sözlü2=float(input('2. sözlü notunuzu giriniz: '))
konusma_sınavı=float(input('Konuşma sınav notunuzu giriniz: '))
dinleme_sınavı=float(input('Dinleme sınav notunuzu giriniz: '))

sözlü_ortalaması=(sözlü1+sözlü2)/2

karne_notu=(sınav1+sınav2+sözlü_ortalaması+konusma_sınavı+dinleme_sınavı)/5

print("Türkçe dersi karne notunuz: ",karne_notu)
    