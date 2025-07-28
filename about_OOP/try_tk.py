import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Hello World")
label2 = tk.Label(window, text="Hello World 2")
tombol = tk.Button(window, text="Click Me wkwkwkw")

# method positioning
label1.pack()
label2.pack()
tombol.pack()

# method show GUI
window.mainloop()