from core.dep import Dep
from core.ner import HealthNER
from core.sentence_unit import SentenceUnit
from ltp import LTP
from config import *
import mysql.connector as mysql
import tkinter as tk


def main():
    pass


if __name__ == '__main__':
    ltp = LTP()
    hner = HealthNER(hner_model_rel_path)
    dep = Dep(hner=hner, ltp=ltp)

    window = tk.Tk()
    window.title('NUTC')
    window.geometry('800x600')
    window.configure(background='white')
    window.mainloop()

    # print(dep.)
