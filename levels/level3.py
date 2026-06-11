# level3.py

import random


class EngineOverheatEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║      LEVEL 3 - MOTOR AŞIRI ISINDI    ║
╚══════════════════════════════════════╝

⚙️ Tren normal hızda ilerlerken
motor bölümünden alarm sesi geliyor.

🌡️ Sıcaklık kritik seviyeye ulaştı.

Eğer müdahale edilmezse motor tamamen
kullanılamaz hale gelebilir.

Şu an:
⚙️ Motor risk altında
⏰ Zaman önemli
💰 Tamir masrafları yüksek olabilir

Ne yapacaksın?

1️⃣ Acil Bakım Yap
   -400₺
   +15 dakika

2️⃣ Hızı Düşür
   +10 dakika
   Arıza riski devam eder

3️⃣ Devam Et
   Süre kaybetmezsin
   Ama motor patlayabilir
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.money -= 400
            train.time += 15

            print("""
🔧 Bakım tamamlandı.

⚙️ Motor tekrar güvenli çalışıyor.

-400₺
+15 dakika
""")

        elif choice == "2":

            train.time += 10

            if random.randint(1, 100) <= 70:

                print("""
🚂 Hız düşürüldü.

🌡️ Motor soğumaya başladı.

+10 dakika
""")

            else:

                train.money -= 250

                print("""
⚠️ Sorun büyüdü.

🔧 Ek bakım gerekti.

-250₺
+10 dakika
""")

        elif choice == "3":

            if random.randint(1, 100) <= 40:

                print("""
😎 Risk aldın ve kazandın.

🚂 Tren yoluna devam etti.
""")

            else:

                train.money -= 800
                train.reputation -= 20
                train.time += 30

                print("""
💥 MOTOR ARIZASI!

🚂 Tren yolda kaldı.
😡 Yolcular şikayetçi.

-800₺
-20 itibar
+30 dakika
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")