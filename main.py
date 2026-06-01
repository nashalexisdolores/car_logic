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

        self.btn_gas = tk.Button(
            self.frame_controls, text="ACCELERATE", width=12, bg="#2e7d32", fg="white",
            command=self.handle_acceleration, font=("Arial", 10, "bold"), relief="flat"
        )
        self.btn_gas.grid(row=0, column=0, padx=10)

        self.btn_brake = tk.Button(
            self.frame_controls, text="BRAKE", width=12, bg="#c62828", fg="white",
            command=self.handle_braking, font=("Arial", 10, "bold"), relief="flat"
        )
        self.btn_brake.grid(row=0, column=1, padx=10)

    def handle_acceleration(self):
        """Triggers speed increase and updates UI."""
        self.my_car.accelerate()
        self.refresh_dashboard()

    def handle_braking(self):
        """Triggers speed decrease and updates UI."""
        self.my_car.brake()
        self.refresh_dashboard()

    def refresh_dashboard(self):
        """Updates the speed label and changes color based on speed."""
        speed = self.my_car.get_speed()
        self.label_speed.config(text=str(speed))
        
        if speed > 120:
            self.label_speed.config(fg="#ff1744")  
        elif speed > 60:
            self.label_speed.config(fg="#ffea00")  
        else:
            self.label_speed.config(fg="#00ff41") 

if __name__ == "__main__":
    root_window = tk.Tk()
    app_instance = car_app(root_window)
    root_window.mainloop() 