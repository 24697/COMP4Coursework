import sqlite3
from Modle import *

def display_main_menu():
    print("1.  Add Data")
    print("2.  Delete Data")
    print("3.  Edit Data")
    print("4.  Exit")
    print("")
    print("Please select an option")
    print("")

def display_data_menu():
    print("1.  Rider")
    print("2.  Club")
    print("3.  Event Type")
    print("4.  Course")
    print("5.  Event Reference")
    print("6.  Event")
    print("7.  Record")
    print("8.  Event Points")
    print("9.  Club Reference")
    print("10. Back")
    print("")
    print("Please select an option")
    print("")

def get_input_str():
    done = False
    while done == False:
        try:
            value = str(input(">>> "))
            print("")
            done = True
        except ValueError:
            print("Value not correct data type, please try again")
            print("")
    return value

def get_input_int():
    done = False
    while done == False:
        try:
            value = int(input(">>> "))
            print("")
            done = True
        except ValueError:
            print("Value not correct data type, please try again")
            print("")
    return value

def get_input_date():
    done1 = False
    done2 = False
    fin_test = 0
    while done1 == False:
        while done2 == False:
            try:
                value = str(input(">>> "))
                print("")
                done2 = True
            except ValueError:
                print("Value not correct data type, please try again")
                print("")
        if len(value) != 10:
            print("The data is not the correct length \nPlease use the format DD/MM/YYYY TYPE 1")
            print("")
            done2 = False
        else:
            for count in range(10):
                if count == 0 or count == 1 or count == 3 or count == 4 or count == 6 or count == 7 or count == 8 or count == 9:
                    if value[count] == "0" or value[count] == "1" or value[count] == "2" or value[count] == "3" or value[count] == "4" or value[count] == "5" or value[count] == "6" or value[count] == "7" or value[count] == "8" or value[count] == "9":
                        fin_test += 1
                elif count == 2 or count == 5:
                    if value[count] == "/":
                        fin_test +=1
            if fin_test == 10:
                done1 = True
            else:
                print("The data is not in the correct format \nPlease use the format DD/MM/YYYY TYPE 2")
                print("")
                done2 = False
    return value

def get_input_time():
    done1= False
    done2 = False
    fin_test = 0
    while done1 == False:
        while done2 == False:
            try:
                value = str(input(">>> "))
                print("")
                done2 = True
            except ValueError:
                print("Data not correct type, Please try again")
                print("")
        if len(value) == 8:
            for count in range(8):
                if count == 0 or count == 1 or count == 3 or count ==  4 or count ==  6 or count == 7:
                    if value[count] == "0" or value[count] == "1" or value[count] == "2" or value[count] == "3" or value[count] == "4" or value[count] == "5" or value[count] == "6" or value[count] == "7" or value[count] == "8" or value[count] == "9":
                        fin_test += 1
                elif count == 2 or count == 5:
                    if value[count] == ":":
                        fin_test += 1
            if fin_test == 8:
                done1 = True
            else:
                print("Data not in the correct format, Please use HH:MM:SS TYPE 1")
                print("")
                done2 = False
        else:
            print("Data not in the correct format, Please use HH:MM:SS TYPE 2")
            print("")
            done2 = False
    return value

def add_menu():
    display_data_menu()
    value = get_input_int()
    if value == 1:
        print("Please enter the forename of the rider")
        forename = get_input_str()
        print("Please enter the Surename of the rider")
        surname = get_input_str()
        values = (forename,surname)
        add_rider(values)
        
    elif value == 2:
        print("Please enter the name of the club")
        club = get_input_str()
        values = (club,)
        add_club(values)
        
    elif value == 3:
        print("Please enter the ID of the reference")
        ID = get_input_int()
        print("Please enter the event type")
        event_type = get_input_str()
        values = (event_type,ID)
        
    elif value == 4:
        print("Please enter the course code")
        course_code = get_input_str()
        print("Please enter the course distance")
        course_distance = get_input_str()
        values = (course_code,course_distance)
        add_course(values)
        
    elif value == 5:
        print("Please enter the ID of the Event")
        ID = get_input_int()
        values = (ID,)
        add_event_reference(values)
        
    elif value == 6:
        print("Please enter the ID of the course that the event used")
        courseID = get_input_int()
        print("Please enter the number of laps used")
        laps = get_input_int()
        print("Please enter the date of the event")
        date = get_input_date()
        values = (date,laps,courseID)
        add_event(values)
        
    elif value == 7:
        print("Please enter the ID of the event")
        event_ID = get_input_int()
        print("Please enter the ID of the rider")
        rider_ID = get_input_int()
        print("Please enter the ride time")
        ride_time = get_input_time()
        print("Please enter the handicap modifyer")
        handicap_mod = get_input_time()
        print("Please enter the age of the rider")
        age = get_input_int()
        values = (ride_time,age,handicap_mod,event_ID,rider_ID)
        add_record(values)
        
    elif value == 8:
        print("Please enter the type of the points")
        event_points_type = get_input_str()
        print("Please enter the points awared")
        event_points = get_input_int()
        print("Please enter the ID of the record")
        ID = get_input_int()
        values = (event_points_type,event_points,ID)
        add_event_points(values)
        
    elif value == 9:
        print("Please enter the date joined")
        joined = get_input_date()
        print("please enter the date left")
        left = get_input_date()
        print("Please enter the ID of the rider")
        rider_ID = get_input_int()
        print("Please enter the ID the club")
        club_ID = get_input_int()
        values = (joined,left,rider_ID,club_ID)
        add_club_reference(values)
    else:
        pass

def delete_menu():    
    display_data_menu()
    value = get_input_int()
    if value == 1:
        print("Please enter ID of the rider that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_rider(values)
    elif value == 2:
        print("Please enter ID of the club that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_club(values)
    elif value == 3:
        print("Please enter ID of the event type that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_event_type(values)
    elif value == 4:
        print("Please enter ID of the course that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_course(values)
    elif value == 5:
        print("Please enter ID of the event reference that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_event_reference(values)
    elif value == 6:
        print("Please enter ID of the event that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_event(values)
    elif value == 7:
        print("Please enter ID of the record that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_record(values)
    elif value == 8:
        print("Please enter ID of the event points that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_event_points(values)
    elif value == 9:
        print("Please enter ID of the club reference that you wish to delete")
        ID = get_input_int()
        values = (ID,)
        delete_club_reference(values)
    else:
        pass

def edit_menu():
    display_data_menu()
    value = get_input_int()
    if value == 1:
        print("Which stribute would you like to edit")
        print("1. Forename")
        print("2. Surname")
        print("3. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the rider that you wish to edit")
            ID = get_input_int()
            print("Please enter the new forename of the rider")
            name = get_input_str()
            values = (name,ID)
            edit_rider_forename(values)
        elif value == 2:
            print("Please enter the ID of the rider that you wish to edit")
            ID = get_input_int()
            print("Please enter the new surname of the rider")
            name = get_input_str()
            values = (name,ID)
            edit_rider_surname(values)
        else:
            pass
    elif value == 2:
        print("Please enter the ID of the club that you wish to edit")
        ID = get_input_int()
        print("Please enter the new club name of the club")
        name = get_input_str()
        values = (name,ID)
        edit_club(values)
    elif value == 3:
        print("Which stribute would you like to edit")
        print("1. Event Type")
        print("2. Event Reference ID")
        print("3. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the Event Type you wish to edit")
            ID = get_input_int()
            print("Please enter the new Type")
            Type = get_input_str()
            values = (Type,ID)
            edit_event_type_type(values)
        elif value == 2:
            print("Please enter the ID of the Event Type you wish to edit")
            ID = get_input_int()
            print("Please enter the new referenceID")
            RID = get_input_str()
            values = (RID,ID)
            edit_event_type_type(values)
        else:
            pass
    elif value == 4:
        print("Which stribute would you like to edit")
        print("1. Course Code")
        print("2. Course Distance")
        print("3. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the course you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the code")
            code = get_input_str()
            values = (code,ID)
            edit_course_code(values)
        elif value == 2:
            print("Please enter the ID of the course you wish to edit")
            ID = get_intput_int()
            print("Please enter the new value of the distance")
            distance = get_input_int()
            values = (distance,ID)
            edit_course_distance(values)
        else:
            pass
    elif value == 5:
        print("Please enter the ID of the event reference that you wish to edit")
        ID = get_input_int()
        print("Please enter the new value of the eventID")
        ID2 = get_input_int()
        values = (ID2,ID)
        edit_event_id(values)
    elif value == 6:
        print("Which stribute would you like to edit")
        print("1. Date")
        print("2. Laps")
        print("3. Course ID")
        print("4. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the event you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the date")
            date = get_input_date()
            values = (date,ID)
            edit_event_date(values)
        elif value == 2:
            rint("Please enter the ID of the event you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the laps")
            laps = get_input_int()
            values = (laps,ID)
            edit_event_laps(values)
        elif value == 3:
            print("Please enter the ID of the event you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the courseID")
            ID2 = get_input_int()
            values = (ID2,ID)
            edit_event_course_id(values)
        else:
            pass
    elif value == 7:
        print("Which stribute would you like to edit")
        print("1. Ride Time")
        print("2. Age")
        print("3. Handicap Mod")
        print("4. Event ID")
        print("5. Rider ID")
        print("6. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the ride time")
            time = get_input_time()
            values = (time,ID)
            edit_record_ride_time(values)
        elif value == 2:
            print("Please enter the ID of the record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the Age")
            age = get_input_int()
            values = (age,ID)
            edit_record_age(values)
        elif value == 3:
            print("Please enter the ID of the record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the handicap mod")
            handicap_mod = get_input_time()
            values = (handicap_mod,ID)
            edit_record_handicap_mod(values)
        elif value == 4:
            print("Please enter the ID of the record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the eventID")
            ID2 = get_input_int()
            values = (ID2,ID)
            edit_record_event_id(values)
        elif value == 5:
            print("Please enter the ID of the record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the ride time")
            time = get_input_time()
            values = (time,ID)
            edit_record_ride_time(values)
        else:
            pass
    elif value == 8:
        print("Which stribute would you like to edit")
        print("1. Event Points Type")
        print("2. Event Points")
        print("3. Record ID")
        print("4. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the event points record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the type")
            Type = get_input_str()
            values = (Type,ID)
            edit_event_points_type(values)
        elif value == 2:
            rint("Please enter the ID of the event points record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the pionts")
            points = get_input_int()
            values = (points,ID)
            edit_event_points(values)
        elif value == 3:
            print("Please enter the ID of the event points record you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the recordID")
            ID2 = get_input_int()
            values = (ID2,ID)
            edit_event_points_record_id(values)
        else:
            pass
    elif value == 9:
        print("Which stribute would you like to edit")
        print("1. Date Joined")
        print("2. Date Left")
        print("3. Rider ID")
        print("4. Club ID")
        print("5. Back")
        print("")
        print("Please select an option")
        print("")
        value = get_input_int()
        if value == 1:
            print("Please enter the ID of the club reference you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the date joined")
            date = get_input_date()
            values = (date,ID)
            edit_club_refernce_date_joined(values)
        elif value == 2:
            print("Please enter the ID of the club reference you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the date left")
            date = get_input_date()
            values = (date,ID)
            edit_club_refernce_date_left(values)
        elif value == 3:
            print("Please enter the ID of the club reference you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the riderID")
            ID2 = get_input_int()
            values = (ID2,ID)
            edit_club_reference_rider_id(values)
        elif value == 4:
            print("Please enter the ID of the club reference you wish to edit")
            ID = get_input_int()
            print("Please enter the new value of the clubID")
            ID2 = get_input_int()
            values = (ID2,ID)
            edit_club_reference_club_id(values)
        else:
            pass
    elif value == 10:
        pass

def main():
    end = False
    while end == False:
        display_main_menu()
        value = get_input_int()
        if value == 1:
            add_menu()
        elif value == 2:
            delete_menu
        elif value == 3:
            edit_menu()
        elif value == 4:
            end = True
            print("Exiting Program")




if __name__ == "__main__":
    main()
