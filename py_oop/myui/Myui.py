import tkinter as tk

class Label():
    def __init__(self, text, pdx, pdy):
        root = tk.tk()
        label = tk.Label(root, text = text, pdx=pdx, pdy=pdy)
        label.mainloop()