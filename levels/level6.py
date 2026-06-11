import random


class StowawayEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Gece yarısı güvenlik görevlisi\n"
            "boş bir yük vagonunda saklanan\n"
            "5 kaçak yolcu buldu.\n\n"
            " İçlerinde çocuklar da var.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Trende kalmalarına izin ver  (-200₺, +15 itibar)"),
                ("2", "Bir sonraki istasyonda teslim et  (+100₺, -10 itibar)"),
                ("3", "Gizlice indir  (riskli)"),
            ],
            title="Kaçak Yolcular",
        )

        if choice == "1":
            train.money -= 200
            train.reputation += 15
            ui.show(" Yardım etmeyi seçtin.\n\n Yolcular sana teşekkür etti.\n\n-200₺  +15 itibar", title="Sonuç")
        elif choice == "2":
            train.money += 100
            train.reputation -= 10
            ui.show(" Güvenlik güçlerine teslim edildiler.\n\n+100₺  -10 itibar", title="Sonuç")
        elif choice == "3":
            if random.randint(1, 100) <= 50:
                ui.show(" Kimse fark etmedi.\n\nOlay kapandı.", title="Sonuç")
            else:
                train.reputation -= 20
                train.money -= 300
                ui.show(" Olay basına yansıdı!\n\n Şirket eleştiriliyor.\n\n-300₺  -20 itibar", title="Sonuç")
        else:
            ui.show(" Geçersiz seçim.\nHiçbir işlem yapılmadı.", title="Sonuç")
