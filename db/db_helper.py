import mysql.connector as mysql
from src.config import config


class DbHelper:
    '''
    param
        host: str
        user: str
        db: str
        password: str
    '''
    def __init__(self, host, user, db, password):
        self.host= host
        self.user= user
        self.db= db
        self.password= password
        self.connection = pymysql.connect(host=__db_config['host'],
                                            user = __db_config['user'],
                                            password = __db_config['password'],
                                            db = __db_config['db'],
                                            charset = 'utf8',
                                            cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.__connection.cursor()
        
    def query(self, query, params):
       self.cursor.execute(query, params)
       return self.cursor

    def close(self):
        self.connection.close()