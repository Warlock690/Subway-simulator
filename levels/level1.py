

class BridgeCollapseEvent:
    def play(self, train):

        print("""
🌉 Köprü çöktü!

🚂 Tren durmak zorunda kaldı.
Raylar hasarlı ve alternatif yol 40 km uzakta.

Şu an seçeneklerin:

1) Ray tamiri (-500₺, +15 dk)
2) Alternatif yol (+30 dk, -20 yakıt)
3) Yolcuları indir (-20 itibar)
""")

        choice = input("\nSeçim: ")

        if choice == "1":
            train.money -= 500
            train.time += 15

            print("""
🔧 Raylar tamir edildi.
Tren tekrar harekete geçti.
""")

        elif choice == "2":
            train.fuel -= 20
            train.time += 30

            print("""
🚂 Alternatif yol seçildi.
Yakıt daha hızlı tüketiliyor.
""")

        elif choice == "3":
            train.reputation -= 20

            print("""
😡 Yolcular indirildi.
İtibar kaybı yaşandı.
""")

        else:
            print("""
❌ Geçersiz seçim!
Hiçbir işlem yapılmadı.
""")