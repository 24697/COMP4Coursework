import sqlite3
class AddRecords():
        def __init__(self):
                pass
        
        def create_new_rider(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = self.db.cursor()
                self.sql = "insert into Rider(Forename,Surname) values(?,?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_course(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into Course(CourseCode,CourseDistance) values(?,?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_club(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into Club(Club) values(?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_event(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into Event(Date,Laps,CourseID) values(?,?,?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_event_reference(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into EventReference(EventID) values(?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_event_type(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into EventType(EventType,EventReferenceID) values(?,?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_record(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into Record(RideTime,Age,HandicapMod,EventID,RiderID) values(?,?,?,?,?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

        def create_new_event_points(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into EventPoints(EventPointsType,EventPoints,RecordID) values(?,?,?)"
                self.cursor.execute(sql,values)
                self.db.commit()

        def create_new_club_refernce(self,values):
            with sqlite3.connect("TeamCambridge.db") as self.db:
                self.cursor = db.cursor()
                self.sql = "insert into ClubReference(DateJoined,DateLeft,RiderID,ClubID) values(?,?,?,?)"
                self.cursor.execute(self.sql,values)
                self.db.commit()

