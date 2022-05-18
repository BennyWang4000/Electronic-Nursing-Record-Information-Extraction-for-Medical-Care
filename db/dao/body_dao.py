from db.db_helper import DbHelper

class BodyDao:
    def __init__(self, host, user, database, password):
        self.db= DbHelper(host=host, user=user, password=password, database=database)

    def select_all(self):
        return self.db.query('SELECT * FROM BODY', None).fetchall()


    def select_where(self, body_tup, symp):
        '''
        param
            body_tup: list<str>
        '''
        where_clause= ' WHERE '
        for idx, body in enumerate(body_tup):
            where_clause+= '`name` = "'+ body+ '\r" OR '
        where_clause= where_clause[:-4]
        print('SELECT * FROM `body`'+ where_clause)


        return self.db.query('SELECT * FROM (SELECT * FROM `body`'+ where_clause +') AS b INNER JOIN (SELECT * FROM `symp` WHERE `name` = '+ symp+ ') AS s ON s.`id` = b.`id`' , None).fetchall()
