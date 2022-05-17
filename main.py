from core.health_dep import HealthDep
from core.health_ner import HealthNER
from core.sentence_unit import SentenceUnit
from ui.ui import UserInterface
from ltp import LTP
from config import *
import mysql.connector as mysql
import tkinter as tk


def btn_event(ltp, hner):
    pass


if __name__ == '__main__':
    ltp = LTP()
    hner = HealthNER(hner_model_rel_path)
    hdep = HealthDep(hner=hner, ltp=ltp)
    ui = UserInterface(hdep)

    # print(dep.)
