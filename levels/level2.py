import random


class RatInfestationEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Gece vardiyası sırasında yük vagonundan\n"
            "garip sesler geliyor.\n\n"
            "Kontrol ettiğinde onlarca farenin\n"
            "erzak kolilerini kemirdiğini fark ettin.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "İlaçlama Ekibi Çağır  (-300₺, +10 dk)"),
                ("2", "Vagonu Mühürle  (-100₺, +20 dk)"),
                ("3", "Hiçbir Şey Yapma  (riskli)"),
            ],
            title="Fare İstilası",
        )

        if choice == "1":
            train.money -= 300
            train.time += 10
            ui.show(" İlaçlama başarılı!\n\n Fareler temizlendi.\n Kargo kurtarıldı.\n\n-300₺  +10 dk", title="Sonuç")
        elif choice == "2":
            train.money -= 100
            train.time += 20
            ui.show(" Vagon mühürlendi.\n\n Kargonun çoğu kurtarıldı.\n Yolculuk gecikti.\n\n-100₺  +20 dk", title="Sonuç")
        elif choice == "3":
            if random.randint(1, 100) <= 50:
                ui.show(" Şanslısın.\n\n Fareler fazla yayılmadı.\n\nKayıp yok.", title="Sonuç")
            else:
                train.money -= 500
                train.reputation -= 15
                ui.show(" Felaket!\n\n Fareler tüm vagona yayıldı.\n Kargonun yarısı zarar gördü.\n\n-500₺  -15 itibar", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
