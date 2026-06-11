import random


class BlizzardEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Şiddetli bir tipi başladı.\n\n"
            " Görüş mesafesi neredeyse sıfır.\n"
            " Rayların bir kısmı kar altında kaldı.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Treni Durdur ve Bekle  (+40 dk, -5 itibar)"),
                ("2", "Kar Temizleme Ekibi Çağır  (-600₺, +15 dk)"),
                ("3", "Yavaş İlerle  (-20 yakıt, riskli)"),
            ],
            title="Tipi Felaketi",
        )

        if choice == "1":
            train.time += 40
            train.reputation -= 5
            ui.show(" Tren durduruldu.\n\n Tipinin geçmesi beklendi.\n\n+40 dk  -5 itibar", title="Sonuç")
        elif choice == "2":
            train.money -= 600
            train.time += 15
            ui.show(" Kar temizleme araçları geldi.\n\n Raylar açıldı.\n\n-600₺  +15 dk", title="Sonuç")
        elif choice == "3":
            train.fuel -= 20
            if random.randint(1, 100) <= 60:
                train.time += 10
                ui.show(" Dikkatli şekilde ilerledin.\n\n Fırtına atlatıldı.\n\n-20 yakıt  +10 dk", title="Sonuç")
            else:
                train.money -= 800
                train.time += 30
                train.reputation -= 15
                ui.show(" Tren kara saplandı!\n\n Kurtarma ekibi çağrıldı.\n\n-800₺  +30 dk  -15 itibar", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
