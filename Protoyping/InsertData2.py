import sqlite3

#insert Course Data
def insert_course_code(values):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Course(CourseCode = ?) where (CourseID = ?) values(?,?)"
        cursor.execute(sql,values)
        db.commit()
        
def insert_course_distance(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Course (CourseDistance) values(?)"
        cursor.execute(sql,values)
        db.commit

#insert Event Data
def insert_event_date(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Event (Date) values(?)"
        cursor.execute(sql,values)
        db.commit()

def insert_event_Laps(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Event (Laps) values(?)"
        cursor.execute(sql,values)
        db.commit()

def insert_event_course_id(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Event (CourseID) values(?)"
        cursor.execute(sql,values)
        db.commit()

#insert Type Reference Data
def insert_type_reference_event_id(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventReference (EventID) values(?)"
        cursor.execute(sql,values)
        db.commit()

#insert Event Type
def insert_event_type_type(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventType (EventType) values(?)"
        cursor.execute(sql,values)
        db.commit()

def insert_event_type_reference(value):
    with sqlite3.connect("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into EventType (EventTypeReferenceID) values(?)"
        cursor.execute(sql,values)
        db.commit()

#insert Rider Data
def insert_rider_forename(value):
    with sqlite3("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Rider (Forename) values(?)"
        cursor.execute(sql,values)
        db.commit()
        
def insert_rider_surname(value):
    with sqlite3("TeamCambridge.db") as db:
        cursor = db.cursor()
        sql = "insert into Rider (Surname) values(?)"
        cursor.execute(sql,values)
        db.commit()


if __name__ == "__main__":
    values = ("E33/10",1)
    insert_course_code(values)
