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


    def get_body_all(self):
        return self.body_dao.select_all()
    
    def integrated_output(self):
        content= ''
        id_set= set()
        where_lst= [self.get_body_where(), self.get_symp_where(), self.get_body_where()]
        for where in where_lst:
            for i in where[0]:
                id_set.add(i['id'])
        print(id_set)

        title= self.get_pdf_where(id_set)

        #TODO not implemented yet! title to string

        return content

    def get_pdf_where(self, id_set):
        self.pdf_dao.select_where(id_set)

    def get_body_where(self):
        print(self.body_lst)
        where= []
        for body_tup in self.body_lst:
            symp= body_tup[-1]
            body_tup= body_tup[:-1]
            where.append(self.body_dao.select_where(body_tup, symp))
        return where

    def get_symp_where(self):
        '''
        return
            list<list<dict<>>>
        '''
        print(self.symp_lst)
        where= []
        for symp_tup in self.symp_lst:
            symp= symp_tup[0]
            where.append(self.symp_dao.select_where(symp))
        return where
        
    def get_dise_where(self):
        '''
        return 
        '''
        print(self.dise_lst)
        where= []
        for dise_tup in self.dise_lst:
            dise= dise_tup[0]
            where.append(self.dise_dao.select_where(dise))
        return where
