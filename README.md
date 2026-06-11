# Train Simulator

Tkinter tabanlı, Türkçe bir tren simülasyon oyunu. 11 farklı seviyede,
her durakta karşılaştığın olaylara doğru kararlar vererek trenini hedefine ulaştır.

## Özellikler

- 11 seviyeli hikâye modu
- Her seviyede farklı olaylar (köprü çökmesi, fare istilası, motor arızası vb.)
- Para, itibar ve yakıt yönetimi
- 10 dakikalık süre sınırı
- Türkçe arayüz

## Ekran Görüntüleri

### Seviye 11 — Son Çarpışma


## Çalıştırma

```bash
cd /home/daisy/simulator
python3 game/main.py
```

Sanal ortam gerekmez (standart kütüphanedeki tkinter kullanılır).

## Oyun Kullanımı

- **Space** — bir sonraki kasabaya ilerle
- **BAŞLAT** butonu — oyunu başlatır, 10 dakikalık süre başlar
- **KONTROLLER** butonu — tuş bilgilerini gösterir
- Olay anında karşına çıkan pencerede **1**, **2** veya **3** tuşlarına bas
- Süre dolar veya kaynakların (para, itibar, yakıt) biri sıfırlanırsa oyun biter
- **TEKRAR DENE** butonu ile ana menüye dönüp yeniden başlayabilirsin

## Seviyeler

| #  | Olay                  | Açıklama                            |
|----|-----------------------|-------------------------------------|
| 1  | Köprü Çökmesi         | Köprü çöker, alternatif yol bul     |
| 2  | Fare İstilası         | Trende fareler yayılır              |
| 3  | Motor Aşırı Isınma    | Motor sıcaklığı kritik seviyede     |
| 4  | Demir Kasabası        | Özel bir durak etkinliği            |
| 5  | Tünel Çökmesi         | Tünel içinde göçük                  |
| 6  | Kaçak Yolcu           | Trende kaçak yolcu bulundu          |
| 7  | Kayıp Kargo           | Kargo kayboldu                      |
| 8  | Tipi                  | Şiddetli kar fırtınası              |
| 9  | Bilinmeyen Hastalık   | Yolcularda salgın                   |
| 10 | Tren Soygunu          | Haydutlar treni durdurdu            |
| 11 | Son Çarpışma          | Final sahnesi                       |

## Kaynaklar

- **Para (Money)** — her durak ilerledikçe artar, olaylarda harcanır
- **İtibar (Reputation)** — doğru kararlarla artar, yanlış kararlarla azalır
- **Yakıt (Fuel)** — her durakta azalır, sıfırlanırsa oyun biter
