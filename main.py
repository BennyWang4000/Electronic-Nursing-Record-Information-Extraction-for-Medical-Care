from core.health_dep import HealthDep
from core.health_ner import HealthNER
from core.sentence_unit import SentenceUnit
from db.dao.body_dao import BodyDao
from db.dao.symp_dao import SympDao
from db.dao.dise_dao import DiseDao
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

        self.body_dao= BodyDao(host=host, user=user, password=password, database='nutc')
        self.symp_dao= SympDao(host=host, user=user, password=password, database='nutc')
        self.dise_dao= DiseDao(host=host, user=user, password=password, database='nutc')

        self.model= HealthModel(self.hdep, self.body_dao, self.symp_dao, self.dise_dao)
        self.view_model= HealthViewModel(self.model)
        root= Tk()
        root.withdraw()
        self.view= HealthView(self.root, self.view_model, 600, 800)

        self.view.load_xml('/home/debian-root/Electronic-Nursing-Record-IE-for-WSL/ui/health_view.xml')
        self.view.mainloop()

if __name__ == '__main__':
    app= App()
