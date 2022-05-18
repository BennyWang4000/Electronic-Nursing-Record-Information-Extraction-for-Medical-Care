import pymysql

class DbHelper:
    '''
    param
        host: str
        user: str
        db: str
        password: str
    '''
    def __init__(self, host, user, database, password):
        self.host= host
        self.user= user
        self.database= database
        self.password= password
        self.connection = pymysql.connect(host=host,
                                            user=user,
                                            password=password,
                                            db=database,
                                            charset = 'utf8',
                                            cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        
    def query(self, query, params):
       self.cursor.execute(query, params)
       return self.cursor

    def close(self):
        self.connection.close()