# level6.py

import random


class StowawayEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║      LEVEL 6 - KAÇAK YOLCULAR        ║
╚══════════════════════════════════════╝

🌧️ Gece yarısı güvenlik görevlisi
boş bir yük vagonunda saklanan
5 kaçak yolcu buldu.

👨‍👩‍👧 İçlerinde çocuklar da var.

Yolcular:
🥶 Üşümüş
🍞 Aç
😨 Korkmuş

Ne yapacaksın?

1️⃣ Trende kalmalarına izin ver
   -200₺ erzak masrafı
   +15 itibar

2️⃣ Bir sonraki istasyonda teslim et
   +100₺ ödül
   -10 itibar

3️⃣ Gizlice indir
   Masraf yok
   Ama riskli
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.money -= 200
            train.reputation += 15

            print("""
❤️ Yardım etmeyi seçtin.

👨‍👩‍👧 Yolcular sana teşekkür etti.

-200₺
+15 İtibar
""")

        elif choice == "2":

            train.money += 100
            train.reputation -= 10

            print("""
👮 Güvenlik güçlerine teslim edildiler.

+100₺
-10 İtibar
""")

        elif choice == "3":

            if random.randint(1, 100) <= 50:

                print("""
😌 Kimse fark etmedi.

Olay kapandı.
""")

            else:

                train.reputation -= 20
                train.money -= 300

                print("""
📸 Olay basına yansıdı!

🚨 Şirket eleştiriliyor.

-300₺
-20 İtibar
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")