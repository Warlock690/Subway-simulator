class FinalCrashEvent:
    def play(self, train, ui, town_name=None):
        choice = ui.choose(
            " Saat 03:17\n\n"
            " Son istasyona sadece 5 km kaldı.\n\n"
            "Aniden...\n\n"
            " KORKUNÇ BİR PATLAMA!\n\n"
            " Önündeki köprü çökmeye başladı.\n"
            " Fren sistemi cevap vermiyor.\n"
            " Yakıt hattı hasar gördü.\n\n"
            "Ne yapacaksın?",
            [
                ("1", "Acil Tahliye Başlat"),
                ("2", "Motoru Zorla Durdur"),
                ("3", "Son Anonsu Yap"),
            ],
            title="Son Köprü",
        )

        rescued = 0

        if choice == "1":
            rescued = 80
            ui.show(" Acil tahliye başlatıldı.\n\n Yolcuların büyük kısmı\nvagonlardan atlamayı başardı.", title="Sonuç")
        elif choice == "2":
            rescued = 30
            ui.show(" Motor zorlandı.\n\n Bir anlığına yavaşladı...\nAma artık çok geç.", title="Sonuç")
        elif choice == "3":
            rescued = 60
            ui.show(" Son anons yapıldı.\n\n Yolcular sakinleşti.\nPanik büyük ölçüde önlendi.", title="Sonuç")
        else:
            rescued = 10
            ui.show(" Kararsız kaldın.\n\n⏳ Zaman tükendi.", title="Sonuç")

        ui.show(" KÖPRÜ ÇÖKÜYOR...\n\n RAY TEMASI KAYBEDİLDİ...\n\n SİSTEM HATASI...\n\n\n\n\n UÇURUM!", title="Son")

        ui.show(
            " Tren Kara Vadi uçurumundan düştü.\n\n"
            " Yolculuk burada sona erdi.\n\n"
            f" Para: {train.money}₺\n"
            f" İtibar: {train.reputation}\n"
            f"⏰ Süre: {train.time} dk\n\n"
            f" Kurtarılan Yolcu: {rescued}/100\n\n"
            "Teşekkürler oynadığın için.",
            title="SON",
        )
