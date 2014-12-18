import sqlite3

def edit_club(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Club set Club = ? where ClubID = ?"
        cursor.execute(sql,values)
        db.commit()
