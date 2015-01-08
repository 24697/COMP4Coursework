import sqlite3

def create_new_rider(values):
        with sqlite3.connect("TeamCambridge.db") as db:
            cursor = db.cursor()
            sql = "insert into Rider(Forename,Surname) values(?,?)"
            cursor.execute(sql,values)
            db.commit()

def create_new_course(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Course(CourseCode,CourseDistance) values(?,?)"
        cursor.execute(sql,values)
        db.commit()

def create_new_club(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Club(Club) values(?)"
        cursor.execute(sql,values)
        db.commit()

def create_new_event(values):
        with sqlite3.connect("TeamCambridge.db") as db:
            cursor = db.cursor()
            sql = "insert into Event(Date,Laps,CourseID) values(?,?,?)"
            cursor.execute(sql,values)
            db.commit()

def create_new_event_reference(values):
        with sqlite3.connect("TeamCambridge.db") as db:
            cursor = db.cursor()
            sql = "insert into EventReference(EventID) values(?)"
            cursor.execute(sql,values)
            db.commit()

def create_new_event_type(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventType(EventType,EventReferenceID) values(?,?)"
        cursor.execute(sql,values)
        db.commit()

def create_new_record(values):
        with sqlite3.connect("TeamCambridge.db") as db:
            cursor = db.cursor()
            sql = "insert into Record(RideTime,Age,HandicapMod,EventID,RiderID) values(?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()

def create_new_event_points(values):
        with sqlite3.connect("TeamCambridge.db") as db:
            cursor = db.cursor()
            sql = "insert into EventPoints(EventPointsType,EventPoints,RecordID) values(?,?,?)"
            cursor.execute(sql,values)
            db.commit()

def create_new_club_refernce(values):
        with sqlite3.connect("TeamCambridge.db") as db:
            cursor = db.cursor()
            sql = "insert into ClubReference(DateJoined,DateLeft,RiderID,ClubID) values(?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()
