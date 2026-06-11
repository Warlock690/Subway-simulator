# level5.py

import random


class TunnelCollapseEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║       LEVEL 5 - TÜNEL GÖÇÜĞÜ         ║
╚══════════════════════════════════════╝

💥 Büyük bir gürültü duyuldu!

🏔️ Tünelin ön kısmı çöktü.
🚂 Tren durmak zorunda kaldı.

Durum:
⛏️ Yol kapalı
⏰ Yolcular huzursuz
💰 Kargo teslim süresi yaklaşıyor

Ne yapacaksın?

1️⃣ Kurtarma Ekibi Çağır
   -700₺
   +25 dakika

2️⃣ İşçileri Gönder
   -300₺
   Başarı garantili değil

3️⃣ Risk Al ve Dar Geçitten İlerle
   Süre kaybetmezsin
   Ama kaza olabilir
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.money -= 700
            train.time += 25

            print("""
🚧 Profesyonel ekip geldi.

🏔️ Tünel güvenli şekilde açıldı.

-700₺
+25 dakika
""")

        elif choice == "2":

            train.money -= 300

            if random.randint(1, 100) <= 60:

                train.time += 15

                print("""
⛏️ İşçiler başarılı oldu.

🏔️ Tünel temizlendi.

-300₺
+15 dakika
""")

            else:

                train.time += 35
                train.reputation -= 10

                print("""
💥 İşçiler başarısız oldu!

🚧 Sonunda yine ekip çağırmak zorunda kaldın.

-300₺
+35 dakika
-10 İtibar
""")

        elif choice == "3":

            if random.randint(1, 100) <= 30:

                print("""
😎 Büyük risk aldın.

🚂 Tren dar geçitten geçti.

Kayıp yok.
""")

            else:

                train.money -= 1000
                train.time += 40
                train.reputation -= 25

                print("""
💀 Kaza!

🚂 Vagonlardan biri raydan çıktı.

-1000₺
+40 dakika
-25 İtibar
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")