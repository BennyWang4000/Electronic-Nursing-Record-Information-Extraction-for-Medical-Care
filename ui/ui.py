import tkinter as tk
from ui.config import *


class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(str(width)+'x'+str(height))
        self.window.configure(background='white')

        self.top_frame = tk.Frame(self.window, width=width, height=height*0.9)
        self.bot_frame = tk.Frame(self.window, width=width, height=height*0.1)

        self.top_frame.grid(column=0, row=0, padx=pad, pady=pad)
        self.bot_frame.grid(column=0, row=1, padx=pad, pady=pad)

        self.top_frame.rowconfigure(0, weight=9)
        self.bot_frame.rowconfigure(1, weight=1)

        self.text_label = tk.Label(self.top_frame)
        self.input_bar = tk.Entry(self.bot_frame)
        self.commit_btn = tk.Button(self.bot_frame, text='Commit', bg='gray')

        self.input_bar.grid(column=0, row=0, padx=pad, pady=pad)
        self.commit_btn.grid(column=1, row=0, padx=pad, pady=pad)

        self.input_bar.columnconfigure(0, weight=6)
        self.commit_btn.columnconfigure(1, weight=1)

        self.window.mainloop()

    def commit_btn_click():
        pass

    def update_text_label():
        pass
