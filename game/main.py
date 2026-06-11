import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[0]
for path in (str(HERE), str(ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

from train import Train
from lines import lines, LINE_ORDER
from levels.level1 import BridgeCollapseEvent
from levels.level2 import RatInfestationEvent
from levels.level3 import EngineOverheatEvent
from levels.level4 import IronTownEvent
from levels.level5 import TunnelCollapseEvent
from levels.level6 import StowawayEvent
from levels.level7 import MissingCargoEvent
from levels.level8 import BlizzardEvent
from levels.level9 import UnknownDiseaseEvent
from levels.level10 import TrainRobberyEvent
from levels.level11 import FinalCrashEvent

LEVEL_EVENT_CLASSES = [
    BridgeCollapseEvent,
    RatInfestationEvent,
    EngineOverheatEvent,
    IronTownEvent,
    TunnelCollapseEvent,
    StowawayEvent,
    MissingCargoEvent,
    BlizzardEvent,
    UnknownDiseaseEvent,
    TrainRobberyEvent,
    FinalCrashEvent,
]


def show_status(train):
    print("\n=== TREN DURUMU ===")
    print(f" Para: {train.money}₺")
    print(f" İtibar: {train.reputation}")
    print(f" Yakıt: {train.fuel}")
    print(f" Süre: {train.time} dk")
    print("====================\n")


def choose_event_town(line):
    if not line.towns:
        return None
    return random.randrange(len(line.towns))


def main():
    train = Train()
    event_towns = {}
    for index, line_name in enumerate(LINE_ORDER):
        line = lines[line_name]
        event_towns[line_name] = choose_event_town(line)

    print("\n=== TREN HAYATINA HOŞ GELDİNİZ ===")
    print("Her hatta yalnızca kendi olayınız var. Kaynaklar tüm seviyeler boyunca kalıcı.")
    show_status(train)
    input("Başlamak için ENTER'a basın...")

    for line_index, line_name in enumerate(LINE_ORDER):
        line = lines[line_name]
        event_class = LEVEL_EVENT_CLASSES[line_index]
        event_triggered = False
        event_town_index = event_towns[line_name]

        print(f"\n===== {line.name} SEFERİ BAŞLIYOR =====")
        print(f"Hattaki durak sayısı: {len(line.towns)}")

        for town_index, town in enumerate(line.towns):
            print(f"\n-- {line.name} | Durak {town_index + 1}/{len(line.towns)}: {town}")
            print(f"Mevcut kaynaklar: Para {train.money}₺ | İtibar {train.reputation} | Yakıt {train.fuel} | Süre {train.time} dk")

            if not event_triggered and town_index == event_town_index:
                print("\n*** SEVİYE OLAYI! ***")
                print(f"Bu hat için seviye: {event_class.__name__}\n")
                event = event_class()
                event.play(train)
                event_triggered = True
                show_status(train)
                if train.money <= 0 and train.reputation <= 0:
                    print("\nOYUN BİTTİ: Para ve itibarınız tükendi.")
                    return
            else:
                print("Tren ilerliyor...")

            if town_index + 1 < len(line.towns):
                input("Sonraki durağa devam etmek için ENTER... ")

        print(f"\n{line.name} rotası tamamlandı. Kaynaklar saklanıyor, bir sonraki hatta devam ediliyor.")
        if line_index + 1 < len(LINE_ORDER):
            input("Sonraki hatta geçmek için ENTER... ")

    print("\n🏁 TÜM HATLAR TAMAMLANDI. OYUN BİTTİ.")
    show_status(train)


if __name__ == "__main__":
    main()
