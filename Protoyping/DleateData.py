import sqlite3

def delete_rider(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from Rider where RiderID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_club(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from Club where ClubID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_event_type(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from EventType where EventTypeID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_course(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from Course where CourseID = ?"
        cursor.execute(sql,ID)
        db.commit
        
def delete_event_reference(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from EventReference where EventReferenceID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_event(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from Event where EventID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_record(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from Record where RecordID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_event_points(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from EventPoints where EventPointsID = ?"
        cursor.execute(sql,ID)
        db.commit

def delete_club_reference(ID):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "delete from ClubReference where ClubReferenceID = ?"
        cursor.execute(sql,ID)
        db.commit
