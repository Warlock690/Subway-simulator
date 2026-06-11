class BridgeCollapseEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Köprü çöktü!\n\n"
            " Tren durmak zorunda kaldı.\n"
            "Raylar hasarlı ve alternatif yol 40 km uzakta.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Ray tamiri  (-500₺, +15 dk)"),
                ("2", "Alternatif yol  (+30 dk, -20 yakıt)"),
                ("3", "Yolcuları indir  (-20 itibar)"),
            ],
            title="Köprü Çöktü",
        )

        if choice == "1":
            train.money -= 500
            train.time += 15
            ui.show(" Raylar tamir edildi.\nTren tekrar harekete geçti.", title="Sonuç")
        elif choice == "2":
            train.fuel -= 20
            train.time += 30
            ui.show(" Alternatif yol seçildi.\nYakıt daha hızlı tüketiliyor.", title="Sonuç")
        elif choice == "3":
            train.reputation -= 20
            ui.show(" Yolcular indirildi.\nİtibar kaybı yaşandı.", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim!\nHiçbir işlem yapılmadı.", title="Sonuç")
