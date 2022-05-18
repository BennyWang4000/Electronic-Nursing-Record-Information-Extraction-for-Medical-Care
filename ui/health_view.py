from ui.tkmvvm.view import View
from ui.tkmvvm.viewmodel import ViewModel
import tkinter

class HealthView(View):
    def __init__(self, parent: tkinter.Tk, context: ViewModel, height: int, width: int, debug: bool = True):
        super().__init__(parent, context, height, width)
        self.window = tkinter.Toplevel(self.parent)
        self.center_window(self.window)
        self.window.protocol('WM_DELETE_WINDOW', self.window.quit)



# class UserInterface:
#     def __init__(self, hdep=None):
#         self.window = tk.Tk()
#         self.window.title(title)
#         self.window.geometry(str(width)+'x'+str(height))
#         self.window.configure(background='white')

#         self.top_frame = tk.Frame(self.window, bg='white')
#         self.bot_frame = tk.Frame(self.window, bg='white')

#         self.window.columnconfigure(0, weight=1)
#         self.window.rowconfigure(0, weight=25)
#         self.window.rowconfigure(1, weight=1)
#         self.top_frame.grid(column=0, row=0, padx=pad, pady=pad, sticky='NSEW')
#         self.bot_frame.grid(column=0, row=1, padx=pad, pady=pad, sticky='NSEW')

#         self.label= tk.Text(self.top_frame, font=('Microsoft JhengHei', '12'), padx=pad, pady=pad)

#         self.input_bar = tk.Entry(self.bot_frame)
#         self.submit_btn = tk.Button(
#             self.bot_frame, text='Submit', command=self.submit_btn_click)

#         self.top_frame.columnconfigure(0, weight=1)
#         self.top_frame.rowconfigure(0, weight=1)
#         self.bot_frame.columnconfigure(0, weight=4)
#         self.bot_frame.columnconfigure(1, weight=1)

#         self.label.grid(column=0, row=0, padx=pad, pady=pad, sticky='NSEW')
#         self.input_bar.grid(column=0, row=0, padx=pad, pady=pad, sticky='NSEW')
#         self.submit_btn.grid(column=1, row=0, padx=pad, pady=pad, sticky='NSEW')


#         self.window.mainloop()

#     def submit_btn_click(self):
#         print(self.input_bar.get())
#         self.update_text_label(self.input_bar.get())

#     def update_text_label(self, content):
#         self.label.insert(tk.END, content)
