# level10.py

import random


class TrainRobberyEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║       LEVEL 10 - TREN SOYGUNU        ║
╚══════════════════════════════════════╝

🌙 Gece yarısı...

🚂 Tren dar bir kanyondan geçerken
rayların üzerine büyük kayalar bırakılmış.

Tren durmak zorunda kaldı.

🔫 Silahlı haydutlar ortaya çıktı.

👤 Haydut Lideri:
"Parayı ve değerli kargoyu verin,
kimse zarar görmesin."

Durum:

💰 Para az
📦 Kargo değerli
😨 Yolcular panikte

Ne yapacaksın?

1️⃣ Kargoyu Teslim Et
2️⃣ Pazarlık Yap
3️⃣ Kaçmaya Çalış
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.reputation -= 10

            print("""
📦 Kargo teslim edildi.

🔫 Haydutlar treni bıraktı.

😔 Yolcular kurtuldu.

-10 İtibar
""")

        elif choice == "2":

            if random.randint(1, 100) <= 55:

                train.reputation += 10

                print("""
🤝 Pazarlık başarılı.

📦 Kargonun bir kısmı verildi.

👍 Yolcular seni alkışladı.

+10 İtibar
""")

            else:

                train.time += 20
                train.reputation -= 15

                print("""
😡 Pazarlık başarısız.

🔫 Haydutlar sinirlendi.

+20 dakika
-15 İtibar
""")

        elif choice == "3":

            if random.randint(1, 100) <= 35:

                train.reputation += 20

                print("""
🚂 Tam güç ileri!

💨 Tren engeli aştı.

🏃 Haydutlar geride kaldı.

+20 İtibar
""")

            else:

                train.time += 40
                train.reputation -= 25

                if hasattr(train, "fuel"):
                    train.fuel = max(0, train.fuel - 15)

                print("""
💥 Kaçış başarısız!

🚂 Vagon hasar aldı.

-25 İtibar
-15 Yakıt
+40 dakika
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")