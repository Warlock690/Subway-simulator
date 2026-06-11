# level11.py

import time


class FinalCrashEvent:

    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║         LEVEL 11 - SON KÖPRÜ         ║
╚══════════════════════════════════════╝

🌑 Saat 03:17

🚂 Son istasyona sadece 5 km kaldı.

Aniden...

💥 KORKUNÇ BİR PATLAMA!

🌉 Önündeki köprü çökmeye başladı.
⚙️ Fren sistemi cevap vermiyor.
⛽ Yakıt hattı hasar gördü.

Hız: 120 km/s
""")

        time.sleep(2)

        print("""
Ne yapacaksın?

1️⃣ Acil Tahliye Başlat
2️⃣ Motoru Zorla Durdur
3️⃣ Son Anonsu Yap
""")

        choice = input("Seçim > ")

        rescued = 0

        if choice == "1":

            rescued = 80

            print("""
🚨 Acil tahliye başlatıldı.

👥 Yolcuların büyük kısmı
vagonlardan atlamayı başardı.
""")

        elif choice == "2":

            rescued = 30

            print("""
⚙️ Motor zorlandı.

🚂 Bir anlığına yavaşladı...

Ama artık çok geç.
""")

        elif choice == "3":

            rescued = 60

            print("""
📻 Son anons yapıldı.

😌 Yolcular sakinleşti.
Panik büyük ölçüde önlendi.
""")

        else:

            rescued = 10

            print("""
⚠️ Kararsız kaldın.

⏳ Zaman tükendi.
""")

        time.sleep(2)

        print("""
⚠️ KÖPRÜ ÇÖKÜYOR...
""")

        time.sleep(1)

        print("""
⚠️ RAY TEMASI KAYBEDİLDİ...
""")

        time.sleep(1)

        print("""
⚠️ SİSTEM HATASI...
""")

        time.sleep(2)

        print("""
🚂═══════════════▶
""")

        time.sleep(0.5)

        print("""
🚂════════════▶
""")

        time.sleep(0.5)

        print("""
🚂════════▶
""")

        time.sleep(0.5)

        print("""
🚂════▶
""")

        time.sleep(0.5)

        print("""
🚂══▶
""")

        time.sleep(0.5)

        print("""
🚂
""")

        time.sleep(1)

        print("""
💥
💥💥
💥💥💥

🌉 UÇURUM!
""")

        time.sleep(2)

        print("""
██████████████████████████████

📡 SİNYAL KAYBI...

██████████████████████████████
""")

        time.sleep(2)

        print(f"""
╔══════════════════════════════════════╗
║               SON                    ║
╚══════════════════════════════════════╝

🚂 Tren Kara Vadi uçurumundan düştü.

💀 Yolculuk burada sona erdi.

📊 SON İSTATİSTİKLER

💰 Para: {train.money}₺
⭐ İtibar: {train.reputation}
⏰ Süre: {train.time} dk

👥 Kurtarılan Yolcu: {rescued}/100

Teşekkürler oynadığın için.
""")