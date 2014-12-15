import sqlite3

def edit_event_date(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Event set Date = ? where EventID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_event_laps(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Event set Laps = ? where EventID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_event_course_id(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Event set CourseID = ? where EventID = ?"
        cursor.execute(sql,values)
        db.commit()
