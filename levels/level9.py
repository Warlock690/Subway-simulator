# level9.py

import random


class UnknownDiseaseEvent:
    def play(self, train):

        print("""
╔══════════════════════════════════════╗
║    LEVEL 9 - BİLİNMEYEN HASTALIK     ║
╚══════════════════════════════════════╝

😷 Birkaç yolcu yüksek ateş şikayetiyle
revir vagonuna getirildi.

Saatler içinde vaka sayısı arttı.

🚂 En yakın hastane 120 km uzakta.

1️⃣ Karantina
2️⃣ Devam Et
3️⃣ Hastane Rotası
""")

        choice = input("\nSeçim > ")

        if choice == "1":

            train.time += 20
            train.reputation -= 5

            print("""
🚪 Karantina uygulandı.

🛑 Vagon izole edildi.

+20 dakika
-5 itibar
""")

        elif choice == "2":

            if random.randint(1, 100) <= 50:

                print("""
😌 Yanlış alarm.

🚂 Yolculuk devam ediyor.
""")

            else:

                train.reputation -= 25

                print("""
☣️ Hastalık yayıldı!

🚨 Durum kontrol dışı.

-25 itibar
""")

        elif choice == "3":

            train.time += 30
            train.fuel -= 10

            print("""
🏥 Hastane rotasına girildi.

🚂 Alternatif güzergah seçildi.

+30 dakika
-10 yakıt
""")

        else:

            print("""
❌ Geçersiz seçim.
Hiçbir işlem yapılmadı.
""")