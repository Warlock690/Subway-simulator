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


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tren Oyunu")
        self.root.configure(bg="#111111")
        self.root.geometry("1400x750")

        self.timer_remaining = 600
        self.timer_job = None
        self.game = None

        self.show_start()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

    def show_start(self):
        self.clear()
        self.timer_remaining = 600
        StartScreen(self.root, self)

    def start_game(self):
        self.clear()
        self.game = GameScreen(self.root, self)
        self._tick()

    def _tick(self):
        if self.timer_remaining > 0:
            self.timer_remaining -= 1
            if self.game:
                self.game.update_timer()
            self.timer_job = self.root.after(1000, self._tick)
        else:
            self.game_over()

    def game_over(self, won=False):
        self.game = None
        self.clear()
        LoseScreen(self.root, self, won=won)


class StartScreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        frame = tk.Frame(root, bg="#111111")
        frame.pack(fill=tk.BOTH, expand=True)

        ascii_art = (
            " _    _     _______     __\n"
            "/ \\  | |   | ____\\ \\   / /\n"
            "/ _ \\ | |   |  _|  \\ \\ / /\n"
            "/ ___ \\| |___| |___  \\ V /\n"
            "/_/   \\_\\_____|_____|  \\_/"
        )
        tk.Label(
            frame, text=ascii_art, fg="#ff6600", bg="#111111",
            font=("Consolas", 20, "bold"), justify=tk.CENTER
        ).pack(pady=(80, 10))

        self.timer_label = tk.Label(
            frame, text="KALAN SÜRE  10:00", fg="white", bg="#111111",
            font=("Consolas", 22, "bold")
        )
        self.timer_label.pack(pady=20)

        btn_frame = tk.Frame(frame, bg="#111111")
        btn_frame.pack(pady=20)

        _make_button(
            btn_frame, text="BAŞLAT", bg="#2a6a2a", fg="white",
            activebackground="#3a8a3a",
            font=("Consolas", 18, "bold"), width=12, height=1,
            command=app.start_game,
        ).pack(pady=6)

        _make_button(
            btn_frame, text="KONTROLLER", bg="#333366", fg="white",
            activebackground="#444488",
            font=("Consolas", 14, "bold"), width=12, height=1,
            command=self.show_controls,
        ).pack(pady=6)

        self._update_timer()

    def _update_timer(self):
        m, s = divmod(self.app.timer_remaining, 60)
        self.timer_label.config(text=f"KALAN SÜRE  {m:02d}:{s:02d}")

    def show_controls(self):
        win = tk.Toplevel(self.root)
        win.title("Kontroller")
        win.configure(bg="#111111")
        win.geometry("500x350")
        win.resizable(False, False)

        tk.Label(
            win, text="KONTROLLER", fg="#ff6600", bg="#111111",
            font=("Consolas", 18, "bold")
        ).pack(pady=(25, 15))

        controls = [
            ("SPACE", "Treni bir sonraki durağa ilerlet"),
        ]

        for key, desc in controls:
            row = tk.Frame(win, bg="#111111")
            row.pack(fill=tk.X, padx=40, pady=6)

            tk.Label(
                row, text=key, fg="#ff9944", bg="#111111",
                font=("Consolas", 14, "bold"), width=12, anchor=tk.W
            ).pack(side=tk.LEFT)

            tk.Label(
                row, text=desc, fg="white", bg="#111111",
                font=("Consolas", 12), anchor=tk.W
            ).pack(side=tk.LEFT, fill=tk.X, expand=True)

        _make_button(
            win, text="KAPAT", bg="#444444", fg="white",
            activebackground="#555555",
            font=("Consolas", 12, "bold"),
            command=win.destroy,
        ).pack(pady=20)


class GameScreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.train = Train()
        self.line_index = 0
        self.town_index = 0

        self.event_town = {}
        for name in LINE_ORDER:
            line = lines[name]
            self.event_town[name] = random.randrange(len(line.towns))

        self._busy = False
        self.root.bind("<space>", self._on_space)

        self.canvases = {}
        self._build_ui()
        self.root.after(50, self._draw_all)

    def _build_ui(self):
        bar = tk.Frame(self.root, bg="#1a1a2e", height=36)
        bar.pack(fill=tk.X)

        self.status_label = tk.Label(
            bar, text="", fg="white", bg="#1a1a2e",
            font=("Consolas", 13, "bold")
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=6)

        self.timer_label = tk.Label(
            bar, text="", fg="#ff9944", bg="#1a1a2e",
            font=("Consolas", 13, "bold")
        )
        self.timer_label.pack(side=tk.RIGHT, padx=10, pady=6)

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

    def update_timer(self):
        m, s = divmod(self.app.timer_remaining, 60)
        self.timer_label.config(text=f"⏱ {m:02d}:{s:02d}")

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
            c.create_text(x, y - 1, text="T", font=("Arial", 16, "bold"), fill="#ffdd00")

    def _update_status(self):
        line_name = LINE_ORDER[self.line_index]
        line = lines[line_name]
        t = self.train
        self.status_label.config(
            text=f"  {line.name}  |  {self.town_index+1}/{len(line.towns)} "
                 f"{line.towns[self.town_index]}  |  "
                 f"Para: {t.money}  Itibar: {t.reputation}  Yakit: {t.fuel}"
        )

    def trigger_event(self):
        cls = LEVEL_EVENT_CLASSES[self.line_index]
        ui = EventUI(self.root)
        town_name = lines[LINE_ORDER[self.line_index]].towns[self.town_index]
        cls().play(self.train, ui, town_name)

    def _on_space(self, e=None):
        if self._busy:
            return
        self._busy = True

        line_name = LINE_ORDER[self.line_index]
        line = lines[line_name]

        if self.town_index == self.event_town[line_name]:
            self.trigger_event()

        if self.train.money <= 0 or self.train.reputation <= 0 or self.train.fuel <= 0:
            self.app.game_over()
            self._busy = False
            return

        self.town_index += 1

        if self.town_index >= len(line.towns):
            self.line_index += 1
            self.town_index = 0
            if self.line_index >= len(LINE_ORDER):
                self.app.game_over(won=True)
                self._busy = False
                return

        self._draw_all()
        self._busy = False


class LoseScreen:
    def __init__(self, root, app, won=False):
        self.root = root
        self.app = app

        frame = tk.Frame(root, bg="#111111")
        frame.pack(fill=tk.BOTH, expand=True)

        if won:
            title_t = "TÜM HATLAR\nTAMAMLANDI!"
            title_f = "#44dd44"
            sub_t = "Tebrikler, oyunu kazandın!"
            sub_f = "#88ff88"
        else:
            title_t = "OYUN BİTTİ"
            title_f = "#dd4444"
            sub_t = "Süre doldu veya kaynakların tükendi."
            sub_f = "#ff8888"

        tk.Label(
            frame, text=title_t, fg=title_f, bg="#111111",
            font=("Arial Black", 48, "bold"), justify=tk.CENTER
        ).pack(pady=(120, 10))

        tk.Label(
            frame, text=sub_t, fg=sub_f, bg="#111111",
            font=("Consolas", 14, "bold")
        ).pack(pady=10)

        m, s = divmod(app.timer_remaining, 60)
        tk.Label(
            frame, text=f"KALAN SÜRE: {m:02d}:{s:02d}",
            fg="white", bg="#111111",
            font=("Consolas", 16, "bold")
        ).pack(pady=5)

        _make_button(
            frame, text="TEKRAR DENE", bg="#2a6a2a", fg="white",
            activebackground="#3a8a3a",
            font=("Consolas", 18, "bold"), width=14, height=1,
            command=app.show_start,
        ).pack(pady=30)


def _make_button(parent, text, bg, fg, command, **kwargs):
    """Label tabanlı buton — macOS'ta tk.Button renkleri çalışmaz."""
    lbl = tk.Label(
        parent, text=text, fg=fg, bg=bg,
        cursor="hand2", padx=10, pady=6,
        **kwargs,
    )
    lbl.bind("<Button-1>", lambda e: command())
    lbl.bind("<Enter>", lambda e: lbl.config(bg=kwargs.get("activebackground", bg)))
    lbl.bind("<Leave>", lambda e: lbl.config(bg=bg))
    return lbl


class EventUI:
    def __init__(self, root):
        self.root = root

    def show(self, text, title="Bilgi"):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.configure(bg="#000000")
        win.geometry("1000x650")
        win.resizable(False, False)

        frame = tk.Frame(win, bg="#000000")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        tk.Label(
            frame, text=text, fg="white", bg="#000000",
            font=("Consolas", 14), justify=tk.LEFT, wraplength=900
        ).pack(expand=True)

        _make_button(
            win, text="TAMAM", bg="#222222", fg="white",
            activebackground="#333333",
            command=win.destroy,
            font=("Consolas", 14, "bold"),
        ).pack(pady=20)

        win.grab_set()
        win.transient(self.root)
        self.root.wait_window(win)

    def choose(self, text, choices, title="Seçim"):
        result = [None]

        win = tk.Toplevel(self.root)
        win.title(title)
        win.configure(bg="#000000")
        win.geometry("1000x700")
        win.resizable(False, False)

        tk.Label(
            win, text=text, fg="white", bg="#000000",
            font=("Consolas", 14), justify=tk.LEFT, wraplength=920
        ).pack(padx=30, pady=(30, 15))

        for key, label in choices:
            _make_button(
                win, text=f"  {key}  {label}",
                bg="#1a1a2e", fg="white",
                activebackground="#2a2a4e",
                command=lambda k=key: [result.__setitem__(0, k), win.destroy()],
                font=("Consolas", 13, "bold"),
            ).pack(fill=tk.X, padx=40, pady=4)

        win.grab_set()
        win.transient(self.root)
        self.root.wait_window(win)

        return result[0]


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
