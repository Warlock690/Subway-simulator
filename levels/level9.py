import random


class UnknownDiseaseEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Birkaç yolcu yüksek ateş şikayetiyle\n"
            "revir vagonuna getirildi.\n\n"
            "Saatler içinde vaka sayısı arttı.\n\n"
            " En yakın hastane 120 km uzakta.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Karantina  (+20 dk, -5 itibar)"),
                ("2", "Devam Et  (riskli)"),
                ("3", "Hastane Rotası  (+30 dk, -10 yakıt)"),
            ],
            title="Bilinmeyen Hastalık",
        )

        if choice == "1":
            train.time += 20
            train.reputation -= 5
            ui.show(" Karantina uygulandı.\n\n Vagon izole edildi.\n\n+20 dk  -5 itibar", title="Sonuç")
        elif choice == "2":
            if random.randint(1, 100) <= 50:
                ui.show(" Yanlış alarm.\n\n Yolculuk devam ediyor.", title="Sonuç")
            else:
                train.reputation -= 25
                ui.show(" Hastalık yayıldı!\n\n Durum kontrol dışı.\n\n-25 itibar", title="Sonuç")
        elif choice == "3":
            train.time += 30
            train.fuel -= 10
            ui.show(" Hastane rotasına girildi.\n\n Alternatif güzergah seçildi.\n\n+30 dk  -10 yakıt", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
