# level7.py

import random


class MissingCargoEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║        LEVEL 7 - KAYIP KARGO         ║
╚══════════════════════════════════════╝

📦 Gece yapılan sayımda önemli bir
kargonun kaybolduğu fark edildi.

💎 Kargo çok değerli ve sigortalı.
🚂 Son teslim tarihi yaklaşıyor.

📹 Güvenlik kameraları içeriden
bir müdahale olabileceğini gösteriyor.

Ne yapacaksın?

1️⃣ Dedektif Tut
   -500₺
   Kargoyu bulma şansı yüksek

2️⃣ Sigortadan Karşıla
   Hızlı çözüm
   İtibar riski var

3️⃣ Personeli Sorgula
   Ucuz
   Ama çalışanlar rahatsız olabilir
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.money -= 500

            if random.randint(1, 100) <= 85:

                train.money += 1000

                print("""
🕵️ Dedektif başarılı!

📦 Kargo geri alındı.

-500₺
+1000₺
""")

            else:

                print("""
🕵️ Soruşturma başarısız.

-500₺
""")

        elif choice == "2":

            train.reputation -= 15

            print("""
📄 Sigorta devreye girdi.

💼 Zarar karşılandı ama
müşteri memnuniyeti düştü.

-15 İtibar
""")

        elif choice == "3":

            if random.randint(1, 100) <= 50:

                train.money += 800

                print("""
👨‍🔧 Suçlu çalışan bulundu.

📦 Kargo kurtarıldı.

+800₺
""")

            else:

                train.reputation -= 20

                print("""
😡 Çalışanlar tepki gösterdi.

🚨 İç huzursuzluk başladı.

-20 İtibar
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")