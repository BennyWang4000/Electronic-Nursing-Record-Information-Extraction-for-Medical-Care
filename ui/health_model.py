from ui.tkmvvm.model import Model
from core.health_dep import HealthDep

class HealthModel(Model):
    outputtext= ""
    inputtext= ""

    def __init__(self, hdep: HealthDep, body_dao, symp_dao, dise_dao):
        self.hdep= hdep
        self.body_lst= []
        self.symp_lst= []
        self.dise_lst= []

        self.body_dao= body_dao
        self.symp_dao= symp_dao
        self.dise_dao= dise_dao

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

    def get_body_all(self):
        return self.body_dao.select_all()
    
    def get_body_where(self):
        print(self.body_lst)
        where= []
        for body_tup in self.body_lst:
            symp= body_tup[-1]
            body_tup= body_tup[:-1]
            where.append(self.body_dao.select_where(body_tup, symp))
        return where
