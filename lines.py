class Line:
    def __init__(self, name, towns):
        self.name = name
        self.towns = towns


LINE1_TOWNS = [
    "Yenikapı", "Aksaray", "Emniyet-Fatih", "Topkapı-Ulubatlı",
    "Bayrampaşa-Maltepe", "Sağmalcılar", "Kocatepe", "Otogar",
    "Terazidere", "Davutpaşa-YTÜ", "Merter", "Zeytinburnu",
    "Bakırköy-İncirli", "Bahçelievler", "Ataköy-Şirinevler",
    "Yenibosna", "DTM-İstanbul Fuar Merkezi", "Atatürk Havalimanı",
]

LINE2_TOWNS = [
    "Yenikapı", "Aksaray", "Emniyet-Fatih", "Topkapı-Ulubatlı",
    "Bayrampaşa-Maltepe", "Sağmalcılar", "Kocatepe", "Otogar",
    "Esenler", "Menderes", "Üçyüzlü", "Bağcılar Meydan", "Kirazlı",
]

LINE3_TOWNS = [
    "Yenikapı", "Vezneciler-İstanbul Ü.", "Haliç", "Şişhane",
    "Taksim", "Osmanbey", "Şişli-Mecidiyeköy", "Gayrettepe",
    "Levent", "4. Levent", "Sanayi Mahallesi", "Seyrantepe",
    "İTÜ-Ayazağa", "Atatürk Oto Sanayi", "Darüşşafaka", "Hacıosman",
]

LINE4_TOWNS = [
    "Bakırköy Sahil", "Özgürlük Meydanı", "İncirli", "Haznedar",
    "İlkyuva", "Molla Gürani", "Kirazlı-Bağcılar", "Yenimahalle",
    "Mahmutbey", "İSTOÇ", "İkitelli Sanayi", "Turgut Özal",
    "Siteler", "Başak Konutları", "Başakşehir-Metrokent",
    "Onurkent", "Şehir Hastanesi", "Toplu Konutlar", "Kayaşehir Merkez",
]

LINE5_TOWNS = [
    "Kadıköy", "Ayrılık Çeşmesi", "Acıbadem", "Ünalan",
    "Göztepe", "Yenisahra", "Pegasus-Kozyatağı", "Bostancı",
    "Küçükyalı", "Maltepe", "Huzurevi", "Gülsuyu",
    "Esenkent", "Hastane-Adliye", "Soğanlık", "Kartal",
    "Yakacık-Adnan Kahveci", "Pendik", "Tavşantepe",
    "Fevzi Çakmak-Hastane", "Yayalar-Şeyhli", "Kurtköy",
    "Sabiha Gökçen Havalimanı",
]

LINE6_TOWNS = [
    "Üsküdar", "Fıstıkağacı", "Bağlarbaşı", "Altunizade",
    "Kısıklı", "Bulgurlu", "Ümraniye", "Çarşı",
    "Yamanevler", "Çakmak", "Ihlamurkuyu", "Altınşehir",
    "İmam Hatip", "Dudullu", "Necip Fazıl", "Çekmeköy",
    "Taşdelen", "Sancaktepe", "Samandıra", "Sultanbeyli",
]

LINE7_TOWNS = [
    "Levent", "Nispetiye", "Etiler", "Boğaziçi Ü.-Hisarüstü",
]

LINE8_TOWNS = [
    "Yıldız", "Fulya", "Mecidiyeköy", "Çağlayan",
    "Kağıthane", "Nurtepe", "Alibeyköy", "Çırçır",
    "Veysel Karani", "Yeşilpınar", "Kâzım Karabekir", "Yenimahalle",
    "Karadeniz Mahallesi", "Giyimkent-Tekstilkent", "Oruçreis",
    "Göztepe Mahallesi", "Mahmutbey",
]

LINE9_TOWNS = [
    "Bostancı", "Emin Ali Paşa", "Ayşekadın", "Kozyatağı",
    "Küçükbakkalköy", "İçerenköy", "Kayışdağı", "Mevlana",
    "İMES", "MODOKO-KEYAP", "Dudullu", "Huzur", "Parseller",
]

LINE10_TOWNS = [
    "Ataköy", "Yenibosna", "Çobançeşme", "29 Ekim Cumhuriyet",
    "Doğu Sanayi", "Mimar Sinan", "15 Temmuz", "Halkalı Caddesi",
    "Atatürk Mahallesi", "Bahariye", "MASKO", "İkitelli Sanayi",
    "Ziya Gökalp Mahallesi", "Olimpiyat",
]

LINE11_TOWNS = [
    "Gayrettepe", "Kağıthane", "Hasdal", "Kemerburgaz",
    "Göktürk", "İhsaniye", "İstanbul Havalimanı",
    "Kargo Terminali", "Taşoluk", "Arnavutköy Hastane",
]

lines = {
    "LINE1": Line("LINE1", LINE1_TOWNS),
    "LINE2": Line("LINE2", LINE2_TOWNS),
    "LINE3": Line("LINE3", LINE3_TOWNS),
    "LINE4": Line("LINE4", LINE4_TOWNS),
    "LINE5": Line("LINE5", LINE5_TOWNS),
    "LINE6": Line("LINE6", LINE6_TOWNS),
    "LINE7": Line("LINE7", LINE7_TOWNS),
    "LINE8": Line("LINE8", LINE8_TOWNS),
    "LINE9": Line("LINE9", LINE9_TOWNS),
    "LINE10": Line("LINE10", LINE10_TOWNS),
    "LINE11": Line("LINE11", LINE11_TOWNS),
}

LINE_ORDER = [
    "LINE1", "LINE2", "LINE3", "LINE4", "LINE5", "LINE6",
    "LINE7", "LINE8", "LINE9", "LINE10", "LINE11",
]
