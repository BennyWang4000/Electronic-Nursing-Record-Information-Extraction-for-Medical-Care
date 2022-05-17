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

        self.text_label = tk.StringVar(self.top_frame)
        self.input_bar = tk.Entry(self.bot_frame)
        self.submit_btn = tk.Button(
            self.bot_frame, text='Submit', bg='gray', command=self.submit_btn_click)

        self.input_bar.grid(column=0, row=0, padx=pad, pady=pad)
        self.submit_btn.grid(column=1, row=0, padx=pad, pady=pad)

        self.input_bar.columnconfigure(0, weight=6)
        self.submit_btn.columnconfigure(1, weight=1)

        self.window.mainloop()

    def submit_btn_click(self):
        self.update_text_label()

    def update_text_label(self):
        self.text_label.set('安安')
