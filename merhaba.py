import requests

def kur_getir():
    print("🌐 Merkez Bankası verilerine bağlanılıyor...")
    
    # Döviz kurlarını veren ücretsiz bir adrese gidiyoruz
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        cevap = requests.get(url)
        veriler = cevap.json() # Gelen karmaşık yazıyı Python'ın anlayacağı sözlüğe çeviriyoruz
        
        dolar_tl = veriler["rates"]["TRY"]
        
        print("---------------------------")
        print("💵 1 ABD Doları = " + str(dolar_tl) + " TL")
        print("---------------------------")
        
    except:
        print("❌ İnternet bağlantısı kurulamadı veya bir hata oluştu.")

kur_getir()