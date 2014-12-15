import sqlite3

def edit_event_type_type(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update EventType set EventType = ? where EventTypeID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_event_type_referenceID(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update EventType set EventReferenceID = ? where EventTypeID = ?"
        cursor.execute(sql,values)
        db.commit()
