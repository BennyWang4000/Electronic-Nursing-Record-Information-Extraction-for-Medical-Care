from ui.tkmvvm.model import Model
from core.health_dep import HealthDep
from db.dao.health_dao import HealthDao

class HealthModel(Model):
    outputtext = ""
    inputtext = ""

    def __init__(self, hdep: HealthDep, health_dao: HealthDao=None):
        self.hdep = hdep
        self.body_lst = []
        self.symp_lst = []
        self.dise_lst = []

        self.health_dao = health_dao

    def cal_dep_lst(self, sentence):
        self.body_lst, self.symp_lst, self.dise_lst = self.hdep.get_dep(
            sentence)

    def integrated_output(self):
        content = ''
        id_set = set()
        where_lst = [self.get_symp_where(), self.get_body_where(),
                     self.get_dise_where()]
        for where in where_lst:
            for lst in where:
                for dct in lst:
                    id_set.add(dct['id'])
        # print(id_set)

        pdf_lst = self.get_pdf_where(id_set)
        for dct in pdf_lst:
            dct.pop('id')
        return pdf_lst

    def get_pdf_where(self, id_set):
        return self.health_dao.select_pdf_where(id_set)

    def get_body_where(self):
        print('body:\t', self.body_lst)
        where = []
        for body_tup in self.body_lst:
            if len(body_tup)<= 0:
                continue
            symp = body_tup[-1]
            body_tup = body_tup[:-1]
            where_cur=self.health_dao.select_body_where(body_tup, symp)
            if len(where_cur)> 0:
                where.append(where_cur)
            
        return where

    def get_symp_where(self):
        '''
        return
            list<list<dict<>>>
        '''
        
        print('symp:\t', self.symp_lst)
        where = []
        for symp in self.symp_lst:
            where_cur= self.health_dao.select_symp_where(symp)
            if len(where_cur)> 0:
                where.append(where_cur)
        
        return where

    def get_dise_where(self):
        '''
        return 
        '''
        where = []
        print('dise:\t', self.dise_lst)
        for dise in self.dise_lst:
            where_cur= self.health_dao.select_dise_where(dise)
            if len(where_cur)> 0:
                where.append(where_cur)
        return where


    def get_body_all(self):
        return self.health_dao.select_body_all()

    def get_pdf_all(self):
        return self.health_dao.select_pdf_all()