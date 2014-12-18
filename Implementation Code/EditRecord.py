import sqlite3

def edit_record_ride_time(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Record set RiderTime = ? where RecordID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_record_Age(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Record set Age = ? where RecordID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_record_handicap_mod(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Record set HandicaoMod = ? where RecordID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_record_event_id(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Record set EventID = ? where RecordID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_record_rider_id(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Record set RiderID = ? where RecordID = ?"
        cursor.execute(sql,values)
        db.commit()
