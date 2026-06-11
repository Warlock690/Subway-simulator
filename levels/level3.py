import random


class EngineOverheatEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Tren normal hızda ilerlerken\n"
            "motor bölümünden alarm sesi geliyor.\n\n"
            " Sıcaklık kritik seviyeye ulaştı.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Acil Bakım Yap  (-400₺, +15 dk)"),
                ("2", "Hızı Düşür  (+10 dk, risk devam eder)"),
                ("3", "Devam Et  (motor patlayabilir)"),
            ],
            title="Motor Aşırı Isındı",
        )

        if choice == "1":
            train.money -= 400
            train.time += 15
            ui.show(" Bakım tamamlandı.\n\n Motor tekrar güvenli çalışıyor.\n\n-400₺  +15 dk", title="Sonuç")
        elif choice == "2":
            train.time += 10
            if random.randint(1, 100) <= 70:
                ui.show(" Hız düşürüldü.\n\n Motor soğumaya başladı.\n\n+10 dk", title="Sonuç")
            else:
                train.money -= 250
                ui.show(" Sorun büyüdü.\n\n Ek bakım gerekti.\n\n-250₺  +10 dk", title="Sonuç")
        elif choice == "3":
            if random.randint(1, 100) <= 40:
                ui.show(" Risk aldın ve kazandın.\n\n Tren yoluna devam etti.", title="Sonuç")
            else:
                train.money -= 800
                train.reputation -= 20
                train.time += 30
                ui.show(" MOTOR ARIZASI!\n\n Tren yolda kaldı.\n Yolcular şikayetçi.\n\n-800₺  -20 itibar  +30 dk", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
