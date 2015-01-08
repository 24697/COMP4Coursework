import sqlite3

def edit_event_points_type(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update EventPoints set EventPointsType = ? where EventPointsID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_event_points(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update EventPoints set EventPoints = ? where EventPointsID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_event_points_record_id(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update EventPoints set RecordID = ? where EventPointsID = ?"
        cursor.execute(sql,values)
        db.commit()
