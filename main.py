from core.health_dep import HealthDep
from core.health_ner import HealthNER
from core.sentence_unit import SentenceUnit
from db.dao.body_dao import BodyDao
from db.dao.symp_dao import SympDao
from db.dao.dise_dao import DiseDao
from tk.ui import UserInterface
from ltp import LTP

from config import *



class App(object):
    def __init__(self):    
        self.ltp = LTP()
        self.hner = HealthNER(hner_model_rel_path)
        self.hdep = HealthDep(hner=self.hner, ltp=self.ltp)

        self.body_dao= BodyDao()
        self.symp_dao= SympDao()
        self.dise_dao= DiseDao()

        self.ui= UserInterface(hdep=hdep)

if __name__ == '__main__':
    app= App()



    # print(dep.)
