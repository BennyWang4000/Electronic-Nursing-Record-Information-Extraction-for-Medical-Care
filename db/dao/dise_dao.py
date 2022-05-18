from db.db_helper import DbHelper

class DiseDao:
    def __init__(self, host, user, database, password):
        self.db= DbHelper(host=host, user=user, password=password, database=database)

    def select_where(self, where):
        return self.db.query('SELECT `id` FROM `dise` WHERE `name` = '+ where, None).fetchall()