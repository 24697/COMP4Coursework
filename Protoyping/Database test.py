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
    db_name = "Team Cambridge.db"
    table_name = "Event"
    sql = """create table Event(
    EventID integer,
    CircuitSeries integer,
    Handicap10 integer,
    Handicap25 integer,
    HillClimb integer,
    Transmedia integer,
    Juvenule integer,
    Code Text,
    Primary Key(EventID))"""
    create_table(db_name,table_name,sql)
    
    db_name = "Team Cambridge.db"
    table_name = "Rider"
    sql = """create table Rider(
    RiderID integer,
    Forename text,
    Surname text,
    Primary Key(RiderID))"""
    create_table(db_name,table_name,sql)
    
    db_name = "Team Cambridge.db"
    table_name = "Record"
    sql = """create table Record(
    RecordID integer,
    RideTime text,
    HandicapTime text,
    RacePostiton integer,
    Club text,
    Age integer,
    RiderID integer,
    EventID integer,
    Primary Key(RecordID),
    foreign Key(RiderID) referances Rider(RiderID),
    foreign Key(EventID) referances Event(EventID))"""
    create_table(db_name,table_name,sql)

    db_name = "Team Cambridge.db"
    table_name = "Team Cambridge Record"
    sql = """ create table Team Cambridge Record(
    TCID integer,
    Handicap10Points integer,
    CircuitPoints integer,
    TransmediaPoints integer,
    JuvenilePoints integer,
    RiderID integer,
    EventID integer,
    Primary Key(TCID),
    foreign Key(RiderID) referances Rider(RiderID),
    foreign Key(EventID) referances Event(EventID))"""
    create_table(db_name,table_name,sql)
