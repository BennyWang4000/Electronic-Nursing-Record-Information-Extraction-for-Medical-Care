from db.db_helper import DbHelper

class HealthDao:
    def __init__(self, host, user, database, password):
        self.db= DbHelper(host=host, user=user, password=password, database=database)

    def select_body_all(self):
        return self.db.query('SELECT * FROM `body`', None).fetchall()

    def select_body_where(self, body_tup, symp):
        '''
        param
            body_tup: list<str>
        return
            list<list<dict<'id': str, 'name': str>>>
        '''
        where_clause= ' WHERE '
        for body in body_tup:
            where_clause+= '`name` = "'+ body+ '\r" OR '
        where_clause= where_clause[:-4]
        symp= symp+'\r'
        # return self.db.query('SELECT * FROM `BODY`'+ where_clause, None).fetchall()
        return self.db.query('SELECT s.`id` FROM (SELECT * FROM `BODY`'+ where_clause +') AS b INNER JOIN (SELECT * FROM `SYMP` WHERE `name` = "'+ symp+ '" ) AS s ON s.`id` = b.`id`', None).fetchall()

    def select_dise_where(self, where):
        return self.db.query('SELECT * FROM `DISE` WHERE `name` = "'+ where+ '\r"', None).fetchall()

    def select_symp_where(self, where):
        return self.db.query('SELECT * FROM `SYMP` WHERE `name` = "'+ where+ '\r"', None).fetchall()

    def select_pdf_where(self, id_set):
        # print(self.db.query('SELECT * FROM `body`', None).fetchall())
        # return self.db.query('SELECT * FROM `body`', None).fetchall()
        where_clause= ''
        for i in id_set:
            where_clause+= "'"+ i+ "',"
        where_clause= where_clause[:-1] 
        print("SELECT * FROM `PDF2` WHERE `id` IN ("+ where_clause+ ")")
        self.db.connection.commit()
        return self.db.query("SELECT * FROM `PDF2` WHERE `id` IN (%s)", where_clause).fetchall()