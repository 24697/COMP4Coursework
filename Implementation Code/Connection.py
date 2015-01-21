from CreatingNewRecords import *

from PyQt4.QtSql import *
from PyQt4.QtCore import *

class SQLConnection:
    def __init__(self,path):
        self.add = AddRecords()
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
    
    def get_all(self,current_table):
        self.query = QSqlQuery()
        
        if current_table == 0:
            self.hold = self.query.prepare("""SELECT * FROM Rider""")
        elif current_table == 1:
            self.hold = self.query.prepare("""SELECT * FROM Club""")

        elif current_table == 2:
            self.hold = self.query.prepare("""SELECT * FROM EventType""")

        elif current_table == 3:
            self.hold = self.query.prepare("""SELECT * FROM Course""")

        elif current_table == 4:
            self.hold = self.query.prepare("""SELECT * FROM EventReference""")

        elif current_table == 5:
            self.hold = self.query.prepare("""SELECT * FROM Event""")

        elif current_table == 6:
            self.hold = self.query.prepare("""SELECT * FROM Record""")

        elif current_table == 7:
            self.hold = self.query.prepare("""SELECT * FROM EventPoints""")

        elif current_table == 8:
            self.hold = self.query.prepare("""SELECT * FROM ClubReference""")

        self.query.exec_()
        
        return self.query

    def add_rider(self,new_rider):
        self.add.create_new_rider(new_rider)
        
        
