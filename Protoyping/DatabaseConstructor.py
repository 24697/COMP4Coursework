import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name)as db:
        cursor = db.cursor()
        cursor.execute('select name from sqlite_master where name = ?',(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            responce = input('The Table {0} already exists, do you want to recreate the table (y/n): '.format(table_name))
            if responce == 'y':
                keep_table = False
                print('The {0} table will be recreated - all existing data will be lost'.format(table_name))
                cursor.execute('drop table if exists {0}'.format(table_name))
            else:
                print('The table was kept')
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

if __name__ == "__main__":
    db_name = "TeamCambridge.db"
    table_name = "Rider"
    sql = """create table Rider(
    RiderID integer,
    Forename text,
    Surname text,
    Primary Key(RiderID))"""
    create_table(db_name,table_name,sql)

    table_name = "Club"
    sql="""create table Club(
    ClubID integer,
    Club text,
    Primary Key(ClubID))"""
    create_table(db_name,table_name,sql)
    
    table_name = "EventType"
    sql = """create table EventType(
    EventTypeID integer,
    EventType text,
    EventReferenceID integer,
    Primary Key(EventTypeID),
    foreign Key(EventReferenceID) references EventReference(EventReferenceID))"""
    create_table(db_name,table_name,sql)

    table_name = "Course"
    sql = """create table Course(
    CourseID integer,
    CourseCode text,
    CourseDistance intefer,
    Primary Key(CourseID))"""
    create_table(db_name,table_name,sql)

    table_name = "EventReference"
    sql = """create table EventReference(
    EventReferenceID integer,
    EventID intefer,
    Primary Key(EventReferenceID),
    foreign Key(EventID) references Event(EventID))"""
    create_table(db_name,table_name,sql)

    table_name = "Event"
    sql = """create table Event(
    EventID integer,
    Date text,
    CourseID integer,
    laps integer,
    Primary Key(EventID),
    foreign Key(CourseID) references Course(CourseID))"""
    create_table(db_name,table_name,sql)

    table_name = "Record"
    sql = """create table Record(
    RecordID integer,
    RideTime integer,
    Age integer,
    HandicapMod integer,
    EventID integer,
    RiderID integer,
    Primary Key(RecordID),
    foreign Key(EventID) references Event(EventID),
    foreign Key(RiderID) references Rdier(RiderID))"""
    create_table(db_name,table_name,sql)

    table_name = "EventPoints"
    sql = """create table EventPoints(
    EventPointsID integer,
    EventPointsType text,
    EventPoints integer,
    RecordID integer,
    Primary Key(EventPointsID),
    foreign Key(RecordID) references Record(RecordID))"""
    create_table(db_name,table_name,sql)

    table_name = "ClubReference"
    sql = """create table ClubReference(
    ClubReferenceID integer,
    DateJoined text,
    DateLeft text,
    RiderID integer,
    ClubID integer,
    Primary Key(ClubReferenceID),
    foreign Key(RiderID) references Rdier(RiderID),
    foreign Key(ClubID) references Club(ClubID))"""
    create_table(db_name,table_name,sql)
    
