from db.db_helper import DbHelper

class SympDao:
    def __init__(self, host, user, database, password):
        self.db= DbHelper(host=host, user=user, password=password, database=database)

    def select_where(self, where):
        where= where+'\r'
        return self.db.query('SELECT `id` FROM `symp` WHERE `name` = "'+ where+ '"', None).fetchall()
