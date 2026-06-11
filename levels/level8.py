# level8.py

import random


class BlizzardEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║       LEVEL 8 - TİPİ FELAKETİ        ║
╚══════════════════════════════════════╝

❄️ Şiddetli bir tipi başladı.

🌨️ Görüş mesafesi neredeyse sıfır.
🚂 Rayların bir kısmı kar altında kaldı.

Yolcular:
🥶 Üşüyor
😟 Endişeli

Durum:
⛽ Yakıt sınırlı
⏰ Teslimat gecikiyor

Ne yapacaksın?

1️⃣ Treni Durdur ve Bekle
   Güvenli
   +40 dakika

2️⃣ Kar Temizleme Ekibi Çağır
   -600₺
   +15 dakika

3️⃣ Yavaş İlerle
   Riskli
   Yakıt tüketir
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.time += 40
            train.reputation -= 5

            print("""
🛑 Tren durduruldu.

❄️ Tipinin geçmesi beklendi.

+40 dakika
-5 İtibar
""")

        elif choice == "2":

            train.money -= 600
            train.time += 15

            print("""
🚜 Kar temizleme araçları geldi.

🚂 Raylar açıldı.

-600₺
+15 dakika
""")

        elif choice == "3":

            train.fuel -= 20

            if random.randint(1, 100) <= 60:

                train.time += 10

                print("""
🚂 Dikkatli şekilde ilerledin.

🌨️ Fırtına atlatıldı.

-20 Yakıt
+10 dakika
""")

            else:

                train.money -= 800
                train.time += 30
                train.reputation -= 15

                print("""
💥 Tren kara saplandı!

🚨 Kurtarma ekibi çağrıldı.

-800₺
+30 dakika
-15 İtibar
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")