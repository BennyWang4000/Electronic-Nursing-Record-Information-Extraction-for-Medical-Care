from ui.tkmvvm.view import View
from ui.tkmvvm.viewmodel import ViewModel
import tkinter

class HealthView(View):
    def __init__(self, parent: tkinter.Tk, context: ViewModel, height: int, width: int):
        super().__init__(parent, context, height, width)
        self.window = tkinter.Toplevel(self.parent)
        self.center_window(self.window)
        self.window.protocol('WM_DELETE_WINDOW', self.window.quit)