import math

from PyQt4.QtSql import *
from PyQt4.QtCore import *

def open_database(path):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(path)
        opened_ok = db.open()
        print(opened_ok)

def get_event_type(eventID):
    query = QSqlQuery()
    query.prepare("""
        SELECT *
        FROM EventType,EventReference
        WHERE EventReference.EventID = ? AND
        EventType.EventReferenceID = EventReference.EventID
    """)
    query.addBindValue(eventID)
    hold = query.exec_()
    print(hold)
    query.first()
    value = query.value(1)
    print(value)
    
    return value

def get_fast_time(event_type,riderID):
    if event_type == "cir":
        query.clear()
        query.prepare("""
        SELECT *
        FROM Record
        WHERE Record.EventID  = (SELECT Event.EventID
        FROM Event
        WHERE Event.CourseID = (SELECT Course.CourseID
        FROM Course
        WHERE CourseCode = "E33/10"))
        AND RiderID = ?
        """)
        query.addBindValue(riderID)
        hold = query.exec_()
        print(hold)
        query.first()
        value = query.value(1)
        print(value)
    elif event_type = "10":
        query.clear()
        query.prepare("""
        SELECT * 
        FROM Record
        WHERE Record.EventID = (SELECT EventReference.EventID
	FROM EventReference
	WHERE EventRefernce.EventReferenceID = (SELECET EventType.EventRefrenceID
	FROM EventType
	WHERE EventType = 10))
        AND Record.RiderID
        """)
        

def cal_handicap(eventID,riderID,path):
    open_database(path)
    event_type = get_event_type(eventID)
    fast_time = get_fast_time(event_type,riderID)

    #
    #10 Cal
    #
    
    if event_type == "10":
        #slice time sting to components
        fast_hour = int(fast_time[0:2])
        fast_min = int(fast_time[3:5])
        fast_sec = int(fast_time[6:8])
        print("{0}:{1}:{2}".format(fast_hour,fast_min,fast_sec))

        #get the difference
        dif_min = fast_min - 17
        print(dif_min)

        #convert time to seconds
        hour_min = fast_hour * 60
        full_min = dif_min + hour_min
        min_sec = full_min *60
        full_sec = fast_sec + min_sec
        print(full_sec)

        #find the change for handicap
        change = full_sec // 15
        print(change)
        handicap = full_sec - change
        print(handicap)
        
        #convert handicap from seconds to Hours ,Minuets and Seconds
        h_sec,h_min = math.modf(handicap / 60)
        h_min = int(h_min)
        h_sec = (h_sec * 60)
        print(h_min)
        print(h_sec)
        h_sec = round(h_sec)
        print(h_sec)
        if h_min > 60:
            h_min, h_hour = math.modf(h_min / 60)
            h_hour = int(h_hour)
            h_min = round(h_min)
        else:
            h_hour = "00"
            
        #Reformat handicap to HH:MM:SS
        h_min = str(h_min)
        if len(h_min) < 2:
            h_min = ("0{0}".format(h_min))
        handicap = ("{0}:{1}:{2}".format(h_hour,h_min,h_sec))
        print(handicap)

  #
  #25 Cal
  #
    elif event_type == "25":
        #slice time sting to components
        fast_hour = int(fast_time[0:2])
        fast_min = int(fast_time[3:5])
        fast_sec = int(fast_time[6:8])
        print("{0}:{1}:{2}".format(fast_hour,fast_min,fast_sec))

        #get the difference
        dif_min = fast_min - 45
        print(dif_min)

        #convert time to seconds
        hour_min = fast_hour * 60
        full_min = dif_min + hour_min
        min_sec = full_min *60
        full_sec = fast_sec + min_sec
        print(full_sec)

        #find the change for handicap
        change = full_sec // 15
        print(change)
        handicap = full_sec - change
        print(handicap)
        
        #convert handicap from seconds to Hours ,Minuets and Seconds
        h_sec,h_min = math.modf(handicap / 60)
        h_min = int(h_min)
        h_sec = (h_sec * 60)
        print(h_min)
        print(h_sec)
        h_sec = round(h_sec)
        print(h_sec)
        if h_min > 60:
            h_min, h_hour = math.modf(h_min / 60)
            h_hour = int(h_hour)
            h_min = round(h_min)
        else:
            h_hour = "00"
            
        #Reformat handicap to HH:MM:SS
        h_min = str(h_min)
        if len(h_min) < 2:
            h_min = ("0{0}".format(h_min))
        handicap = ("{0}:{1}:{2}".format(h_hour,h_min,h_sec))
        print(handicap)

        #
        #Cir Cal
        #


    elif event_type == "cir":
        #slice time sting to components
        fast_hour = int(fast_time[0:2])
        fast_min = int(fast_time[3:5])
        fast_sec = int(fast_time[6:8])
        print("{0}:{1}:{2}".format(fast_hour,fast_min,fast_sec))

        #get the difference
        dif_min = fast_min - 11
        print(dif_min)

        #convert time to seconds
        hour_min = fast_hour * 60
        full_min = dif_min + hour_min
        min_sec = full_min *60
        full_sec = fast_sec + min_sec
        print(full_sec)

        #find the change for handicap
        change = full_sec // 15
        print(change)
        handicap = full_sec - change
        print(handicap)
        
        #convert handicap from seconds to Hours ,Minuets and Seconds
        h_sec,h_min = math.modf(handicap / 60)
        h_min = int(h_min)
        h_sec = (h_sec * 60)
        print(h_min)
        print(h_sec)
        h_sec = round(h_sec)
        print(h_sec)
        if h_min > 60:
            h_min, h_hour = math.modf(h_min / 60)
            h_hour = int(h_hour)
            h_min = round(h_min)
        else:
            h_hour = "00"
            
        #Reformat handicap to HH:MM:SS
        h_min = str(h_min)
        if len(h_min) < 2:
            h_min = ("0{0}".format(h_min))
        handicap = ("{0}:{1}:{2}".format(h_hour,h_min,h_sec))
        print(handicap)

    return handicap



