import sqlite3

def edit_club_reference_date_joined(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update ClubRefernece set DateJoined = ? where ClubReferenceID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_club_reference_date_left(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update ClubRefernece set DateLeft = ? where ClubReferenceID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_club_reference_riderID(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update ClubRefernece set RiderID = ? where ClubReferenceID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_club_reference_club_id(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update ClubRefernece set ClubID = ? where ClubReferenceID = ?"
        cursor.execute(sql,values)
        db.commit()
