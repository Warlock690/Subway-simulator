class IronTownEvent:
    def play(self, train, ui, town_name="Demirkoy"):
        choice = ui.choose(
            f" {town_name}'e ulaştın.\n\n"
            f" Mevcut Paran: {train.money}₺\n\n"
            "Ne yapacaksın?",
            [
                ("1", f"Tamirhane  (-300₺)" + ("  (yetersiz bakiye)" if train.money < 300 else "")),
                ("2", f"Market  (-200₺, +10 itibar)" + ("  (yetersiz bakiye)" if train.money < 200 else "")),
                ("3", "Dinlen ve Yola Devam Et  (ücretsiz)"),
            ],
            title="Istasyon",
        )

        if choice == "1":
            if train.money >= 300:
                train.money -= 300
                if hasattr(train, "engine_health"):
                    train.engine_health = min(100, train.engine_health + 30)
                ui.show(" Tamir tamamlandı.\n\n Motor durumu iyileştirildi.\n\n-300₺", title="Sonuç")
            else:
                ui.show(" Yetersiz para.", title="Sonuç")
        elif choice == "2":
            if train.money >= 200:
                train.money -= 200
                train.reputation += 10
                ui.show(" Market alışverişi yapıldı.\n\n Erzaklar yenilendi.\n Yolcular memnun.\n\n-200₺  +10 itibar", title="Sonuç")
            else:
                ui.show(" Yetersiz para.", title="Sonuç")
        elif choice == "3":
            ui.show(" Kısa bir moladan sonra yolculuk devam ediyor.", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.", title="Sonuç")
