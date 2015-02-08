import sqlite3

def edit_event_id(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update EventReference set EventID = ? where EventReferneceID = ?"
        cursor.execute(sql,values)
        db.commit()
