import sqlite3

from CreatingNewRecords import *
from DleateData import *
from EditClub import *
from EditRider import *
from EditEventType import *
from EditCourse import *
from EditEventReference import *
from EditEvent import *
from EditRecord import *
from EditClubReference import *
from EditEventPoints import *




def add_rider(values):
    create_new_rider(values)

def add_club(values):
    create_new_club(values)
    
def add_event_type(values):
    create_new_event_type(values)

def add_course(values):
    create_new_course(values)
    
def add_event_reference(values):
    create_new_event_reference(values)

def add_event(values):
    create_new_event(values)

def add_record(values):
    create_new_record(values)

def add_event_points(values):
    create_new_event_points(values)

def add_club_reference(values):
    create_new_club_refernce(values)
