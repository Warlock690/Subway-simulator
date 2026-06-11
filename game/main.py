import tkinter as tk
from tkinter import messagebox
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


class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tren Oyunu")
        self.root.configure(bg="#111111")
        self.root.geometry("1400x750")

        self.train = Train()
        self.line_index = 0
        self.town_index = 0

        self.event_town = {}
        for name in LINE_ORDER:
            line = lines[name]
            self.event_town[name] = random.randrange(len(line.towns))

        self.root.bind("<space>", self._on_space)

        self.canvases = {}
        self._build_ui()
        self.root.after(50, self._draw_all)

    def _build_ui(self):
        bar = tk.Frame(self.root, bg="#1a1a2e", height=36)
        bar.pack(fill=tk.X)

        self.status_label = tk.Label(
            bar, text="", fg="white", bg="#1a1a2e",
            font=("Consolas", 14, "bold")
        )
        self.status_label.pack(pady=6)

        main = tk.Frame(self.root, bg="#111111")
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=(4, 8))

        for i, line_name in enumerate(LINE_ORDER):
            row = tk.Frame(main, bg="#111111")
            row.pack(fill=tk.X, pady=2)

            tk.Label(
                row, text=f"L{i+1}", fg="#888888", bg="#111111",
                font=("Consolas", 10, "bold"), width=3, anchor=tk.W
            ).pack(side=tk.LEFT)

            c = tk.Canvas(
                row, bg="#1a1a2e", highlightbackground="#555555",
                highlightthickness=1, height=60
            )
            c.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(3, 0))
            c.bind("<Configure>", lambda e, ln=line_name: self._draw_line(ln))

            self.canvases[line_name] = c

        help_lbl = tk.Label(
            self.root, text="BOŞLUK (SPACE) ile ilerle",
            fg="#888888", bg="#111111", font=("Consolas", 11, "bold")
        )
        help_lbl.pack(pady=(0, 6))

    def _draw_all(self):
        for line_name in LINE_ORDER:
            self._draw_line(line_name)
        self._update_status()

    def _draw_line(self, line_name):
        c = self.canvases[line_name]
        c.delete("all")
        w = c.winfo_width()
        if w < 10:
            return

        line = lines[line_name]
        towns = line.towns
        n = len(towns)
        h = 60
        y = h // 2

        spacing = max(28, min(110, (w - 40) / max(1, n - 1)))
        start_x = (w - spacing * (n - 1)) / 2 if n > 1 else w // 2

        if n > 1:
            c.create_line(
                start_x, y, start_x + spacing * (n - 1), y,
                fill="#444444", width=4
            )

        line_idx = LINE_ORDER.index(line_name)
        is_current = line_idx == self.line_index
        is_done = line_idx < self.line_index

        for j, town in enumerate(towns):
            x = start_x + j * spacing

            if is_done:
                fill, out, tf = "#1a5a1a", "#5a9a5a", "#8aba8a"
            elif is_current and j == self.town_index:
                fill, out, tf = "#ffdd00", "#ffaa00", "white"
            elif is_current:
                fill, out, tf = "#666666", "#999999", "#cccccc"
            else:
                fill, out, tf = "#3a3a3a", "#666666", "#777777"

            r = 7 if (is_current and j == self.town_index) else 5
            c.create_oval(x - r, y - r, x + r, y + r, fill=fill, outline=out, width=2)

            short = town if len(town) <= 12 else town[:11] + "."
            c.create_text(x, y + 17, text=short, fill=tf, font=("Arial", 8, "bold"))

        if is_current and self.town_index < n:
            x = start_x + self.town_index * spacing
            c.create_text(x, y - 1, text="🚂", font=("Arial", 20))

    def _update_status(self):
        line_name = LINE_ORDER[self.line_index]
        line = lines[line_name]
        t = self.train
        self.status_label.config(
            text=f"  🚂 {line.name}  |  {self.town_index+1}/{len(line.towns)} "
                 f"{line.towns[self.town_index]}  |  "
                 f"💰 {t.money}₺  ⭐ {t.reputation}  ⛽ {t.fuel}  ⏱ {t.time}dk"
        )

    def trigger_event(self):
        cls = LEVEL_EVENT_CLASSES[self.line_index]
        messagebox.showwarning("SEVİYE OLAYI", f"{cls.__name__} başladı!")
        cls().play(self.train, self.root)

    def _on_space(self, e=None):
        line_name = LINE_ORDER[self.line_index]
        line = lines[line_name]

        if self.town_index == self.event_town[line_name]:
            self.trigger_event()

        if self.train.money <= 0 and self.train.reputation <= 0:
            messagebox.showerror("GAME OVER", "Para ve itibar bitti!")
            self.root.destroy()
            return

        self.town_index += 1

        if self.town_index >= len(line.towns):
            self.line_index += 1
            self.town_index = 0
            if self.line_index >= len(LINE_ORDER):
                messagebox.showinfo("BİTTİ", "Tüm hatlar tamamlandı!")
                self.root.destroy()
                return

        self._draw_all()


if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()
