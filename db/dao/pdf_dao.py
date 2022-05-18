from db.db_helper import DbHelper

class PdfDao:
    def __init__(self, host, user, database, password):
        self.db= DbHelper(host=host, user=user, password=password, database=database)

    def select_all(self):
        return self.db.query('SELECT * FROM `pdf`', None).fetchall()
        

    def select_where(self, id_set):
        where_clause= ' WHERE '
        for i in id_set:
            where_clause+= '`id` = "'+ i+ '\r" OR '
            break
        where_clause= where_clause[:-4]
        print('SELECT `id`, `title`, `html` FROM `pdf`'+ where_clause.replace('\r', '@@'))
        return self.db.query('SELECT * FROM `pdf`'+ where_clause, None).fetchall()