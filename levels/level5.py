import random


class TunnelCollapseEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Büyük bir gürültü duyuldu!\n\n"
            " Tünelin ön kısmı çöktü.\n"
            " Tren durmak zorunda kaldı.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Kurtarma Ekibi Çağır  (-700₺, +25 dk)"),
                ("2", "İşçileri Gönder  (-300₺, riskli)"),
                ("3", "Risk Al ve Dar Geçitten İlerle  (kaza olabilir)"),
            ],
            title="Tünel Göçüğü",
        )

        if choice == "1":
            train.money -= 700
            train.time += 25
            ui.show(" Profesyonel ekip geldi.\n\n Tünel güvenli şekilde açıldı.\n\n-700₺  +25 dk", title="Sonuç")
        elif choice == "2":
            train.money -= 300
            if random.randint(1, 100) <= 60:
                train.time += 15
                ui.show(" İşçiler başarılı oldu.\n\n Tünel temizlendi.\n\n-300₺  +15 dk", title="Sonuç")
            else:
                train.time += 35
                train.reputation -= 10
                ui.show(" İşçiler başarısız oldu!\n\n Sonunda yine ekip çağırmak zorunda kaldın.\n\n-300₺  +35 dk  -10 itibar", title="Sonuç")
        elif choice == "3":
            if random.randint(1, 100) <= 30:
                ui.show(" Büyük risk aldın.\n\n Tren dar geçitten geçti.\n\nKayıp yok.", title="Sonuç")
            else:
                train.money -= 1000
                train.time += 40
                train.reputation -= 25
                ui.show(" Kaza!\n\n Vagonlardan biri raydan çıktı.\n\n-1000₺  +40 dk  -25 itibar", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
