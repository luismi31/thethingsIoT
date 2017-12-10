import MySQLdb
import datetime

class Database:

    host = 'localhost'
    user = 'root'
    password = 'smonker'
    db = 'IOTDB'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message

    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
        
    def insertData(self,db,value,name,type): 
        query = "INSERT INTO IOTDB.data (value, name, timestamp, type) VALUES (" + "'" + value + "','" + name + "','" + str(datetime.datetime.now()) + "','" + type + "');"
        if self.insert(query):
            print 'STORED: ' + value
