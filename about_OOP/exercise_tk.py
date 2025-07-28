import tkinter as tk

class Hero:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def attack(self, musuh, log_text):
        log_text.insert(tk.END, f"{self.name} attacking {musuh.name}\n")
        musuh.defend(self, self.power, log_text)

    def defend(self, musuh, power_musuh, log_text):
        log_text.insert(tk.END, f"{self.name} defending {musuh.name}\n")
        rasa_serangan = power_musuh / self.armor
        log_text.insert(tk.END, f"rasa serangannya: {rasa_serangan:.2f}\n")
        self.health -= rasa_serangan
        self.health = max(0, self.health)
        log_text.insert(tk.END, f"jadi health {self.name}: {self.health:.2f}\n\n")

# GUI
def create_gui():
    window = tk.Tk()
    window.title("Hero Battle")

    # Hero objects
    L7 = Hero("L7", 200, 177, 77)
    suki = Hero("Suki", 150, 100, 50)

    # Log output
    log_text = tk.Text(window, height=20, width=60)
    log_text.pack(pady=10)

    # Button actions
    def L7_attacks_suki():
        L7.attack(suki, log_text)

    def suki_attacks_L7():
        suki.attack(L7, log_text)

    # Buttons
    frame = tk.Frame(window)
    frame.pack()

    button1 = tk.Button(frame, text="L7 Attacks Suki", command=L7_attacks_suki)
    button1.grid(row=0, column=0, padx=10)

    button2 = tk.Button(frame, text="Suki Attacks L7", command=suki_attacks_L7)
    button2.grid(row=0, column=1, padx=10)

    window.mainloop()

create_gui()
