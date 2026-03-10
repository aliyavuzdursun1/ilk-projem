def gunluk_yaz():
    not_icerigi = input("Bugün ne öğrendin? : ")
    
    # 'a' (append) modu: Dosyanın sonuna ekleme yapar, eskiyi silmez.
    with open("gunluk.txt", "a", encoding="utf-8") as dosya:
        dosya.write("- " + not_icerigi + "\n")
    print("✅ Notun 'gunluk.txt' dosyasına kaydedildi!")

def gunluk_oku():
    print("\n--- SENİN MÜHENDİSLİK GÜNLÜĞÜN ---")
    try:
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            print(icerik)
    except FileNotFoundError:
        print("⚠️ Henüz bir günlük dosyası oluşturulmamış.")
    print("---------------------------------")

# Programı çalıştıralım
gunluk_yaz()
gunluk_oku()