import sqlite3

def edit_course_code(values):
        with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Course set CouseCode = ? where CourseID = ?"
        cursor.execute(sql,values)
        db.commit()

def edit_course_distance(values):
        with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "update Couse set CouseDistance = ? where CourseID = ?"
        cursor.execute(sql,values)
        db.commit()
