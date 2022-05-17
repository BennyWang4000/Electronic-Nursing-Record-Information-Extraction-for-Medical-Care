import mysql.connector as mysql
# * ===== file path =====
hner_model_rel_path = r'data\model\model_ner_adam_1e-06_2.pt'

'''
schema



'''
# * ===== mysql database =====
host = ''
database = ''
user = ''
password = ''
db_connection = mysql.connect(
    host=host, database=database, user=user, password=password)
