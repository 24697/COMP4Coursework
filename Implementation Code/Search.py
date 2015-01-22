from PyQt4.QtSql import *
import sqlite3

class Search:
    def __init__(self):
        self.search_query = QSqlQuery()

    def search_rider(self,setting,values):
        if setting == 1:
            self.hold = self.search_query.prepare("""SELECT * FROM Rider WHERE RiderID = ?""")
            print(self.hold)
            self.search_query.addBindValue(values)
            self.search_query.exec_()
            return self.search_query
