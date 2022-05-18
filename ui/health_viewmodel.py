from ui.tkmvvm.viewmodel import ViewModel
from ui.tkmvvm.model import Model

class HealthViewModel(ViewModel):

    def __init__(self, model: Model):
        super(HealthViewModel, self).__init__(model)
        self.model= model

    @property
    def outputbox(self):
        print('out', self.model.outputtext)
        return self.model.outputtext

    @outputbox.setter
    def outputbox(self, text):
        self.model.outputtext= text
        self.on_property_changed('outputbox')

    @property
    def inputbox(self):
        print('in', self.model.inputtext)
        return self.model.inputtext

    @inputbox.setter
    def inputbox(self, text):
        self.model.inputtext= text
        self.on_property_changed('inputbox')

    def submit(self):
        self.model.cal_dep_lst(self.model.inputtext)
        self.model.outputtext= self.model.get_output_dep()
        self.on_property_changed('outputbox')