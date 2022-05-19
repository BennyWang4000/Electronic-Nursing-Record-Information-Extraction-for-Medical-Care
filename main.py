from core.health_dep import HealthDep
from core.health_ner import HealthNER
from core.sentence_unit import SentenceUnit
from db.dao.health_dao import HealthDao
from ui.health_view import HealthView
from ui.health_viewmodel import HealthViewModel
from ui.health_model import HealthModel
from ltp import LTP
from tkinter import Tk

from config import *



class App(object):
    def __init__(self):    
        self.ltp = LTP()
        self.hner = HealthNER(hner_model_rel_path)
        self.hdep = HealthDep(hner=self.hner, ltp=self.ltp)

        self.health_dao= HealthDao(host=host, user=user, password=password, database=database)

        # self.model= HealthModel(self.hdep)
        self.model= HealthModel(self.hdep, self.health_dao)
        self.view_model= HealthViewModel(self.model)
        self.root= Tk()
        self.root.withdraw()
        self.root.withdraw()
        self.view= HealthView(self.root, self.view_model, height, width)

        self.view.load_xml('/home/debian-root/Electronic-Nursing-Record-IE-for-WSL/ui/health_view.xml')
        self.view.mainloop()

if __name__ == '__main__':
    app= App()
