from db.db_helper import DbHelper

class PdfDao:
    def __init__(self, host, user, database, password):
        self.db= DbHelper(host=host, user=user, password=password, database=database)

    def select_where(self, id_set):
        where_clause= ' WHERE '
        for i in id_set:
            where_clause+= '`name` = "'+ i+ '" OR '
        where_clause= where_clause[:-4]

        return self.db.query('SELECT * FROM `pdf`'+ where_clause, None).fetchall()