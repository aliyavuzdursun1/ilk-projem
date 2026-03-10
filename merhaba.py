
# 1. MAKİNEYİ KURUYORUZ (Tanımlama)
def selam_ver():
    print("Merhaba Aliya!")
    print("Bugün Python öğreniyorsun.")

# 2. DÜĞMEYE BASIYORUZ (Çalıştırma)
selam_ver()
selam_ver()
def toplama_yap(a, b):
    sonuc = a + b
    return sonuc  # Sonucu elimize teslim etti

# Şimdi o sonucu alıp ekrana yazdıralım
hesap = toplama_yap(10, 20)
print(hesap)
