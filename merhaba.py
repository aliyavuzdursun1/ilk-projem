# Başkasının yazdığı 'random' (rastgelelik) paketini içeri çağırıyoruz
import random

def oyun_baslat():
    # Bilgisayar 1 ile 20 arasında gizli bir sayı tutsun
    gizli_sayi = random.randint(1, 20)
    tahmin_hakki = 3
    
    print("🤖: 1 ile 20 arasında bir sayı tuttum. 3 hakkın var!")

    while tahmin_hakki > 0:
        tahmin = int(input("Tahminin nedir?: "))
        
        if tahmin == gizli_sayi:
            print("🎉 Tebrikler! Bilgisayar mühendisi zekasıyla doğru bildin!")
            break
        elif tahmin < gizli_sayi:
            print("🔼 Daha büyük bir sayı dene.")
        else:
            print("🔽 Daha küçük bir sayı dene.")
            
        tahmin_hakki -= 1
        print("Kalan hakkın: " + str(tahmin_hakki))

    if tahmin_hakki == 0:
        print("💀 Maalesef hakkın bitti. Sayı şuydu: " + str(gizli_sayi))

# Oyunu çalıştıralım
oyun_baslat()