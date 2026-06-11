# level4.py

class IronTownEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║      LEVEL 4 - DEMİRKÖY İSTASYONU    ║
╚══════════════════════════════════════╝

🏘️ Tren Demirköy'e ulaştı.

Kasaba sakin görünüyor ancak burada
çeşitli hizmetler satın alabilirsin.

💰 Mevcut Paran: {}₺

1️⃣ Tamirhane
   Motor bakımı
   -300₺

2️⃣ Market
   Erzak al
   +10 İtibar
   -200₺

3️⃣ Dinlen ve Yola Devam Et
   Ücretsiz
""".format(train.money))

        choice = input("\nSeçim > ")

        if choice == "1":

            if train.money >= 300:

                train.money -= 300

                if hasattr(train, "engine_health"):
                    train.engine_health = min(100, train.engine_health + 30)

                print("""
🔧 Tamir tamamlandı.

⚙️ Motor durumu iyileştirildi.

-300₺
""")

            else:

                print("""
❌ Yetersiz para.
""")

        elif choice == "2":

            if train.money >= 200:

                train.money -= 200
                train.reputation += 10

                print("""
🛒 Market alışverişi yapıldı.

🍞 Erzaklar yenilendi.
😊 Yolcular memnun.

-200₺
+10 İtibar
""")

            else:

                print("""
❌ Yetersiz para.
""")

        elif choice == "3":

            print("""
🚂 Kısa bir moladan sonra
yolculuk devam ediyor.
""")

        else:

            print("""
❌ Geçersiz seçim.
""")