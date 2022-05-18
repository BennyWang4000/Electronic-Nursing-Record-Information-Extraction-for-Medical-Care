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
        # self.ltp = LTP()
        # self.hner = HealthNER(hner_model_rel_path)
        # self.hdep = HealthDep(hner=self.hner, ltp=self.ltp)

        # self.body_dao= BodyDao()
        # self.symp_dao= SympDao()
        # self.dise_dao= DiseDao()
        model= HealthModel
        view_model= HealthViewModel(model)
        root= Tk()
        root.withdraw()
        view= HealthView(root, view_model, 600, 800)

        view.load_xml('/home/debian-root/Electronic-Nursing-Record-IE-for-WSL/ui/health_view.xml')
        view.mainloop()

        # self.ui= UserInterface(hdep=hdep)

if __name__ == '__main__':
    app= App()



    # print(dep.)
