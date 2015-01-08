import sqlite3

def edit_rider_forename(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Rider set Forename = ? where RiderID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_rider_surname(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Rider set Surname = ? where RiderID = ?"
        cursor.execute(sql,values)
        db.commit()
