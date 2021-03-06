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
    #Delete data
    #

    def delete_data(self,current_table,data):
        if current_table == 0:
            self.ok = self.query.prepare("""DELETE FROM Rider WHERE RiderID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 1:
            self.ok = self.query.prepare("""DELETE FROM Club WHERE ClubID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 2:
            self.ok = self.query.prepare("""DELETE FROM EventType WHERE EventTypeID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 3:
            self.ok = self.query.prepare("""DELETE FROM Course WHERE CourseID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 4:
            self.ok = self.query.prepare("""DELETE FROM EventReference WHERE EventReferenceID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 5:
            self.ok = self.query.prepare("""DELETE FROM Event WHERE EventID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 6:
            self.ok = self.query.prepare("""DELETE FROM Record WHERE RecordID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 7:
            self.ok = self.query.prepare("""DELETE FROM EventPoints WHERE EventPointsID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
        elif current_table == 8:
            self.ok = self.query.prepare("""DELETE FROM ClubReference WHERE ClubReferenceID = ?""")
            print(self.ok)
            self.query.addBindValue(data[0])
            self.query.exec_()
    

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
        self.add.create_new_course(new_course)

    def add_new_event_reference(self,new_event_reference):
        self.add.create_new_event_reference(new_event_reference)
        
    def add_event(self,new_event):
        self.add.create_new_event(new_event)
        
    def add_record(self,new_record):
        self.add.create_new_record(new_record)
        
    def add_event_points(self,new_event_points):
        self.add.create_new_event_points(new_event_points)
        
    def add_club_reference(self,new_club_reference):
        self.add.create_new_club_reference(new_club_reference)

    #
    #search database
    #
    
    def search_database(self,current_table,data):
        self.search_query = QSqlQuery()
        #
        #Rider Searcing
        #
        if current_table == 0:
            if (data[0] != "Rider ID" or data[0] != "") and (data[1] == "Forename" or data[1] == "") and (data[2] == "Surname" or data[2] == ""):
                self.ok = self.search_query.prepare("""SELECT * FROM Rider WHERE Rider.RiderID LIKE ? """)
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.exec_()
                return self.search_query
            
            elif (data[0] == "Rider ID" or data[0] == "") and (data[1] != "Forename" or data[1] != "") and (data[2] == "Surname" or data[2] == ""):
                self.ok = self.search_query.prepare("SELECT * FROM Rider WHERE Forename LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "Rider ID" or data[0] == "") and (data[1] == "Forename" or data[1] == "") and (data[2] != "Surname" or data[2] != ""):
                self.ok = self.search_query.prepare("""SELECT * FROM Rider WHERE Rider.Surname LIKE ? """)
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query
            
            elif (data[0] != "Rider ID" or data[0] != "") and (data[1] != "Forename" or data[1] != "") and (data[2] == "Surname" or data [2] ==  ""):
                self.ok = self.search_query.prepare("SELECT * FROM Rider WHERE RiderID LIKE ? AND Forename LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "Rider ID" or data[0] == "") and (data[1] != "Forename" or data[1] != "") and (data[2] != "Surname" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Rider WHERE Forename LIKE ? AND Surname LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "Rider ID" or data[0] != "") and (data[1] == "Forename" or data[1] == "") and (data[2] != "Surname" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Rider WHERE RiderID LIKE ? AND Surname LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "Rider ID" or data[0] != "") and (data[1] != "Forename" or data[1] != "") and (data[2] != "Surname" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Rider WHERE RiderID LIKE ? AND Forename LIKE ? AND Surname LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query
        
        #
        #Club Search
        #

        elif current_table == 1:
            if (data[0] != "ClubID" or data[0] != "") and (data[1] == "Club Name" or data[1] == ""):
                self.ok = self.search_query.prepare("SELECT * FROM Club WHERE ClubID LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "ClubID" or data[0] == "") and (data[1] != "Club Name" or data[1] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Club WHERE Club LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "ClubID" or data[0] != "") and (data[1] != "Club Name" or data[1] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Club WHERE ClubID LIKE ? AND Club LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

        #
        #Event Type
        #
        
        elif current_table == 2:
            if (data[0] != "Event TypeID" or data[0] != "") and (data[1] == "Event Type" or data[1] == "") and (data[2] == "Event ReferenceID" or data[2] == ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventTypeID LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.exec_()
                return self.search_query
            
            elif (data[0] == "Event TypeID" or data[0] == "") and (data[1] != "Event Type" or data[1] != "") and (data[2] == "Event ReferenceID" or data[2] == ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventType LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "Event TypeID" or data[0] == "") and (data[1] == "Event Type" or data[1] == "") and (data[2] != "Event ReferenceID" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventReferenceID LIKE ?")
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query
            
            elif (data[0] != "Event TypeID" or data[0] != "") and (data[1] != "Event Type" or data[1] != "") and (data[2] == "Event ReferenceID" or data [2] ==  ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventTypeID LIKE ? AND EventType LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "Event TypeID" or data[0] == "") and (data[1] != "Event Type" or data[1] != "") and (data[2] != "Event ReferenceID" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventType LIKE ? AND EventReferenceID LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "Event TypeID" or data[0] != "") and (data[1] == "Event Type" or data[1] == "") and (data[2] != "Event ReferenceID" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventTypeID LIKE ? AND EventReferenceID LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "Event TypeID" or data[0] != "") and (data[1] != "Event Type" or data[1] != "") and (data[2] != "Event ReferenceID" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM EventType WHERE EventTypeID LIKE ? AND EventType LIKE ? AND EventReferenceID LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query
        #
        #Course
        #
        elif current_table == 3:
            if (data[0] != "CourseID" or data[0] != "") and (data[1] == "Course Code" or data[1] == "") and (data[2] == "Course Distance" or data[2] == ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseID LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.exec_()
                return self.search_query
            
            elif (data[0] == "CourseID" or data[0] == "") and (data[1] != "Course Code" or data[1] != "") and (data[2] == "Course Distance" or data[2] == ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseCode LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "CourseID" or data[0] == "") and (data[1] == "Course Code" or data[1] == "") and (data[2] != "Course Distance" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseDistance LIKE ?")
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query
            
            elif (data[0] != "CourseID" or data[0] != "") and (data[1] != "Course Code" or data[1] != "") and (data[2] == "Course Distance" or data [2] ==  ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseID LIKE ? AND CourseCode LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] == "CourseID" or data[0] == "") and (data[1] != "Course Code" or data[1] != "") and (data[2] != "Course Distance" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseCode LIKE ? AND CourseDistance LIKE ?")
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[1])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "CourseID" or data[0] != "") and (data[1] == "Course Code" or data[1] == "") and (data[2] != "Course Distance" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseID LIKE ? AND CourseDistance LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query

            elif (data[0] != "CourseID" or data[0] != "") and (data[1] != "Course Code" or data[1] != "") and (data[2] != "Course Distance" or data[2] != ""):
                self.ok = self.search_query.prepare("SELECT * FROM Course WHERE CourseID LIKE ? AND CourseCode LIKE ? AND CourseDistance LIKE ?")
                self.hold = ("%{0}%".format(data[0]))
                data[0] = self.hold
                self.hold = ("%{0}%".format(data[1]))
                data[1] = self.hold
                self.hold = ("%{0}%".format(data[2]))
                data[2] = self.hold
                print(self.ok)
                self.search_query.addBindValue(data[0])
                self.search_query.addBindValue(data[1])
                self.search_query.addBindValue(data[2])
                self.search_query.exec_()
                return self.search_query
