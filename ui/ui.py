import tkinter as tk
from ui.config import *


class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(str(height)+'x'+str(width))
        self.window.configure(background='white')

        self.text_view = tk.Frame(self.window)
        self.input_bar = tk.Frame(self.window, bg='gray')
        self.commit_btn = tk.Button(self.window, text='Commit', bg='gray')

        self.text_view.grid(column=0, row=0, padx=pad, pady=pad, columnspan=2)
        self.input_bar.grid(column=0, row=1, padx=pad, pady=pad)
        self.commit_btn.grid(column=1, row=1, padx=pad, pady=pad)

        self.text_view.rowconfigure(0, weight=8)
        self.input_bar.rowconfigure(1, weight=1)
        self.commit_btn.rowconfigure(1, weight=1)

        self.input_bar.columnconfigure(0, weight=8)
        self.commit_btn.rowconfigure(1, weight=1)
        self.window.mainloop()
    def show_():
        pass
