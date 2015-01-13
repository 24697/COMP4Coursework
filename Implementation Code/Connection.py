from PyQt4.QtSql import *
from PyQt4.QtCore import *

class SQLConnection:
    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        opened_ok = self.db.open()
        return opened_ok

    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self,event):
        self.close_database()
    
    def get_all(self):
        self.model = QSqlQueryModel()
        print("pass3-1-1")
        self.query = QSqlQuery()
        print("pass3-1-2")
        #cant be a float
        self.hold = self.query.prepare("""SELECT * FROM EventType WHERE EventTypeID = 1""")
        print("pass3-1-3")
        print(self.hold)
        self.query.exec_()
        print("pass3-1-4")
        self.model.setQuery(self.query)
        print("pass3-1-5")
        return self.model
