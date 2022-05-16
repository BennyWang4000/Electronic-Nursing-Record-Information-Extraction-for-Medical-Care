from core.dep import Dep
from core.ner import HealthNER
from core.sentence_unit import SentenceUnit
from ltp import LTP
from config import *


def main():
    pass


if __name__ == '__main__':
    ltp = LTP()
    hner = HealthNER(hner_model_rel_path)
    dep = Dep(hner=hner, ltp=ltp)
