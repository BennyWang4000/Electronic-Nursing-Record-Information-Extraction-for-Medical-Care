from ui.tkmvvm.viewmodel import ViewModel
from ui.tkmvvm.model import Model
import webbrowser

class HealthViewModel(ViewModel):

    def __init__(self, model: Model):
        super(HealthViewModel, self).__init__(model)
        self.model= model

    def submit(self):
        #*** self.model.cal_dep_lst(self.model.inputtext)
        #*** content= self.model.integrated_output()
        content= [['1', 'https://www.youtube.com/'], ['2', 'https://www.twitter.com/'], ['3', 'https://www.google.com/']]
        self.update_output(content)

    def search(self):
        print(self.outputbox)
        # self.open_url()

    def update_output(self, content):
        self.model.outputtext= content
        self.on_property_changed('outputbox')

    def open_url(self, url):
        webbrowser.open_new(url)

    @property
    def outputbox(self):
        print('out', self.model.outputtext)
        return self.model.outputtext

    @outputbox.setter
    def outputbox(self, lst):
        self.model.outputtext= lst
        self.on_property_changed('outputbox')

    @property
    def inputbox(self):
        print('in', self.model.inputtext)
        return self.model.inputtext

    @inputbox.setter
    def inputbox(self, text):
        self.model.inputtext= text
        self.on_property_changed('inputbox')


