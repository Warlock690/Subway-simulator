import random


class TrainRobberyEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Gece yarısı...\n\n"
            " Tren dar bir kanyondan geçerken\n"
            "rayların üzerine büyük kayalar bırakılmış.\n\n"
            " Silahlı haydutlar ortaya çıktı.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Kargoyu Teslim Et  (-10 itibar)"),
                ("2", "Pazarlık Yap  (riskli)"),
                ("3", "Kaçmaya Çalış  (çok riskli)"),
            ],
            title="Tren Soygunu",
        )

        if choice == "1":
            train.reputation -= 10
            ui.show(" Kargo teslim edildi.\n\n Haydutlar treni bıraktı.\n Yolcular kurtuldu.\n\n-10 itibar", title="Sonuç")
        elif choice == "2":
            if random.randint(1, 100) <= 55:
                train.reputation += 10
                ui.show(" Pazarlık başarılı.\n\n Kargonun bir kısmı verildi.\n Yolcular seni alkışladı.\n\n+10 itibar", title="Sonuç")
            else:
                train.time += 20
                train.reputation -= 15
                ui.show(" Pazarlık başarısız.\n\n Haydutlar sinirlendi.\n\n+20 dk  -15 itibar", title="Sonuç")
        elif choice == "3":
            if random.randint(1, 100) <= 35:
                train.reputation += 20
                ui.show(" Tam güç ileri!\n\n Tren engeli aştı.\n Haydutlar geride kaldı.\n\n+20 itibar", title="Sonuç")
            else:
                train.time += 40
                train.reputation -= 25
                if hasattr(train, "fuel"):
                    train.fuel = max(0, train.fuel - 15)
                ui.show(" Kaçış başarısız!\n\n Vagon hasar aldı.\n\n-25 itibar  -15 yakıt  +40 dk", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
