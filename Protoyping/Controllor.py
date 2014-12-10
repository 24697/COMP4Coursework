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

def display_add_data_menu():
    print("1.  Rider")
    print("2.  Club")
    print("3.  Event Type")
    print("4.  Course")
    print("5.  Event Reference")
    print("6.  Event")
    print("7.  Record")
    print("8.  Event Points")
    print("9.  Club Refernce")
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
    tests_passed = 0
    tests_run = 0
    while done1 == False:
        while done2 == False:
            try:
                value = str(input(  ">>> "))
                print("")
                done2 = True
            except ValueError:
                print("Value not correct data type, please try again")
                print("")
    if len(value) != 10:
        print("The data is not the correct length \nPlease use the format DD/MM/YYYY")
        print("")
    else:
        for count in range(1,10):
            if count == 1 or count == 2 or count == 4 or count == 5 or count == 7 or count == 8 or count == 9 or count == 10:
                if value[:count] == "0" or value[:count] == "1" or value[:count] == "2" or value[:count] == "3" or value[:count] == "4" or value[:count] == "5" or value[:count] == "6" or value[:count] == "7" or value[:count] == "8" or value[:count] == "9":
                    tests_passed += 1
            elif count == 3 or count == 6:
                if value[:count] == "/":
                    tests_passed +=1
        if tests_passed == 10:
            done1 = True
        else:
            print("The data is not in the correct format \nPlease use the format DD/MM/YYYY")
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
            for count in range(1,8):
                if count == 1 or count == 2 or count == 4 or count ==  5 or count ==  7 or count == 8:
                    if value[:count] == "0" or value[:count] == "1" or value[:count] == "2" or value[:count] == "3" or value[:count] == "4" or value[:count] == "5" or value[:count] == "6" or value[:count] == "7" or value[:count] == "8" or value[:count] == "9":
                        fin_test += 1
                elif count == 3 or count == 6:
                    if value[:count] == ":":
                        fin_test += 1
            if fin_test == 8:
                done1 = True
            else:
                print("Data not in the correct format, Please use HH:MM:SS")
                print("")
                done2 = False
        else:
            print("Data not in the correct format, Please use HH:MM:SS")
            print("")
            done2 = False
    return value


def main():
    end = False
    while end == False:
        display_main_menu()
        value = get_input_int()
        if value == 1:
            display_add_data_menu()
            value = get_input_int()
            if value == 1:
                print("Please enter the forename of the rider")
                forename = get_input_str()
                print("Please enter the Surename fo the rider")
                surname = get_input_str()
                values = (forename,surname)
                add_rider(values)
            elif value == 2:
                print("Please enter the name of the club")
                club = get_input_str()
                values = (club,)
                add_club(values)
            elif value == 3:
                pass
            elif value == 4:
                print("Please enter the course code")
                course_code = get_input_str()
                print("Please enter the course distance")
                course_distance = get_input_str()
                values = (course_code,course_distance)
                add_course(values)
            elif value == 5:
                pass
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
                pass
            elif value == 8:
                pass
            elif value == 9:
                pass
        elif value == 2:
            pass
        elif value == 3:
            pass
        elif value == 4:
            end = True
            print("Exiting Program")




if __name__ == "__main__":
    main()
