import tkinter as tk
from car_logic import car_logic

class car_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Performance Dashboard")
        self.root.geometry("400x350")
        self.root.configure(bg="#1a1a1b")  

        self.my_car = car_logic(2026, "Nirvana Cyber-GT")

        self.setup_ui()

    def setup_ui(self):
        """Creates the visual elements for the dashboard."""
        self.label_info = tk.Label(
            self.root, text=self.my_car.get_info().upper(),
            font=("Courier New", 14, "bold"), fg="#d4af37", bg="#1a1a1b"
        )
        self.label_info.pack(pady=20)

        self.label_speed = tk.Label(
            self.root, text="0",
            font=("Impact", 60), fg="#00ff41", bg="#1a1a1b"
        )
        self.label_speed.pack()

        self.label_unit = tk.Label(self.root, text="KM/H", fg="white", bg="#1a1a1b")
        self.label_unit.pack()

        self.frame_controls = tk.Frame(self.root, bg="#1a1a1b")
        self.frame_controls.pack(pady=30)