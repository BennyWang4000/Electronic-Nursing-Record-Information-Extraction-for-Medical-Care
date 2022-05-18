from db.db_helper import DbHelper

class BodyDao:
    def __init__():
        self.db= DbHelper()

    def select_where(self, where):
        return self.db.query('SELECT * FROM ')