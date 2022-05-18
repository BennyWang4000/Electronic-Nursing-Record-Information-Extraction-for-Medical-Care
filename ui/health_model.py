from ui.tkmvvm.model import Model
from core.health_dep import HealthDep

class HealthModel(Model):
    outputtext= ""
    inputtext= ""

    def __init__(self, hdep: HealthDep):
        self.hdep= hdep
        self.body_lst= []
        self.symp_lst= []
        self.dise_lst= []

    def cal_dep_lst(self, sentence):
        self.body_lst, self.symp_lst, self.dise_lst= self.hdep.get_dep(sentence)

    def get_output_dep(self):
        output_str= ""
        print('lst', self.body_lst)
        for body in self.body_lst:
            output_str+= str(body)+ '\n'
        for symp in self.symp_lst:
            output_str+= str(symp)+ '\n'
        for dise in self.dise_lst:
            output_str+= str(dise)+ '\n'
        print(output_str)
        return output_str
    