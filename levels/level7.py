import random


class MissingCargoEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Gece yapılan sayımda önemli bir\n"
            "kargonun kaybolduğu fark edildi.\n\n"
            " Kargo çok değerli ve sigortalı.\n"
            " Son teslim tarihi yaklaşıyor.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Dedektif Tut  (-500₺, yüksek başarı)"),
                ("2", "Sigortadan Karşıla  (itibar riski)"),
                ("3", "Personeli Sorgula  (ucuz, riskli)"),
            ],
            title="Kayıp Kargo",
        )

        if choice == "1":
            train.money -= 500
            if random.randint(1, 100) <= 85:
                train.money += 1000
                ui.show(" Dedektif başarılı!\n\n Kargo geri alındı.\n\n-500₺  +1000₺", title="Sonuç")
            else:
                ui.show(" Soruşturma başarısız.\n\n-500₺", title="Sonuç")
        elif choice == "2":
            train.reputation -= 15
            ui.show(" Sigorta devreye girdi.\n\n Zarar karşılandı ama müşteri memnuniyeti düştü.\n\n-15 itibar", title="Sonuç")
        elif choice == "3":
            if random.randint(1, 100) <= 50:
                train.money += 800
                ui.show(" Suçlu çalışan bulundu.\n\n Kargo kurtarıldı.\n\n+800₺", title="Sonuç")
            else:
                train.reputation -= 20
                ui.show(" Çalışanlar tepki gösterdi.\n\n İç huzursuzluk başladı.\n\n-20 itibar", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
