from CreatingNewRecords import *
from Search import *

from PyQt4.QtSql import *
from PyQt4.QtCore import *

class SQLConnection:
    def __init__(self,path):
        self.add = AddRecords()
        self.search = Search()
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
            self.query.prepare("""SELECT * FROM Rider""")
        elif current_table == 1:
            self.query.prepare("""SELECT * FROM Club""")

        elif current_table == 2:
            self.query.prepare("""SELECT * FROM EventType""")

        elif current_table == 3:
            self.query.prepare("""SELECT * FROM Course""")

        elif current_table == 4:
            self.query.prepare("""SELECT * FROM EventReference""")

        elif current_table == 5:
            self.hold = self.query.prepare("""SELECT * FROM Event""")

        elif current_table == 6:
            self.query.prepare("""SELECT * FROM Record""")

        elif current_table == 7:
            self.query.prepare("""SELECT * FROM EventPoints""")

        elif current_table == 8:
            self.query.prepare("""SELECT * FROM ClubReference""")

        self.query.exec_()
        
        return self.query

    #
    #add data
    #
    
    def add_rider(self,new_rider):
        self.add.create_new_rider(new_rider)

    def add_club(self,new_club):
        self.add.create_new_club(new_club)

    def add_event_type(self,new_event_type):
        self.add.create_new_event_type(new_event_type)

    def add_course(self,new_course):
        self.add.create_new_club(new_course)

    def add_event_reference(self,new_event_reference):
        self.add.create_new_event_reference(new_event_reference)
        
    def add_event(self,new_event):
        self.add.create_new_event(new_event)
        
    def add_new_record(self,new_record):
        self.add.create_new_record(new_record)
        
    def add_new_event_points(self,new_event_points):
        self.add.create_new_event_points(new_event_points)
        
    def add_new_club_reference(new_club_refernece):
        self.add.create_new_club_reference(new_reference)

    #
    #search database
    #
    
    def search_database(self,current_table,data):
        if current_table == 0:


            if data[0] != "Rider ID" and data[1] == "Forename" and data[2] == "Surname":
                self.values = (data[0],)
                self.setting = 1
                self.search_query = self.search.search_rider(self.setting,self.values)
                return self.search_query
            
        
