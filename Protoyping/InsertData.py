import sqlite3
       
def insert_data_course(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Course (CourseCode,CourseDistance) values(?,?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_event(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Event (Date,Laps,CourseID) values(?,?,?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_event_type_reference(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventReference (EventID) values(?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_event_type(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventType (EventType,EventTypeReferenceID) values(?,?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_rider(values):
    with sqlite3("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Rider (Forename,Surname) values(?,?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_club(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Club (Club) values(?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_club_reference(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into ClubReference (DateJoined,DateLeft,RiderID,ClubID) values(?,?,?,?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_record(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Record (RideTime,Age,HandicapMod,EventID,RiderID) values(?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit

def insert_data_event_points(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventPoints (EventPointsType,EventPoints,RecordID) values(?,?,?)"
        cursor.execute(sql,values)
        db.commit
if __name__ == "__main__":
    values = ("E33\10",10)
    insert_data_course(values)

    values("17/10/1995",2,1)
    insert_data_event(values)

    values(0,)
    insert_data_event_type_reference(values)

    values("Handicap10",0)
    insert_data_event_type(values)

    values("Peter","Millard")
    insert_data_rider(values)

    values("Team Cambridge Cycling Club",)
    insert_data_club(values)

    values("17/10/1995","NA",0,0)
    insert_data_club_reference(values)

    values("1:00:00",19,"00:02:05",0)
    insert_data_record(values)

    values("Handicap10",20,0)
    insert_data_event_points(values)
