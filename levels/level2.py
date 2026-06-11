# level2.py

import random


class RatInfestationEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║       LEVEL 2 - FARE İSTİLASI        ║
╚══════════════════════════════════════╝

🐀 Gece vardiyası sırasında yük vagonundan
garip sesler geliyor.

Kontrol ettiğinde onlarca farenin
erzak kolilerini kemirdiğini fark ettin.

Şu an:
📦 Erzaklar risk altında
😷 Hastalık yayılabilir
💰 Kargonun değeri yüksek

Ne yapacaksın?

1️⃣ İlaçlama Ekibi Çağır
   -300₺
   +10 dakika

2️⃣ Vagonu Mühürle
   Kargo kurtulur
   Yolculuk gecikir

3️⃣ Hiçbir Şey Yapma
   Para kaybetmezsin
   Ama fareler çoğalabilir
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.money -= 300
            train.time += 10

            print("""
🧪 İlaçlama başarılı!

🐀 Fareler temizlendi.
📦 Kargo kurtarıldı.

-300₺
+10 dakika
""")

        elif choice == "2":

            train.money -= 100
            train.time += 20

            print("""
🔒 Vagon mühürlendi.

📦 Kargonun çoğu kurtarıldı.
🚂 Yolculuk gecikti.

-100₺
+20 dakika
""")

        elif choice == "3":

            if random.randint(1, 100) <= 50:

                print("""
😌 Şanslısın.

🐀 Fareler fazla yayılmadı.

Kayıp yok.
""")

            else:

                train.money -= 500
                train.reputation -= 15

                print("""
💥 Felaket!

🐀 Fareler tüm vagona yayıldı.
📦 Kargonun yarısı zarar gördü.

-500₺
-15 itibar
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")