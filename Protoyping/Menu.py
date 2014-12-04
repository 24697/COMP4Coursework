def display_database_menu():
    print("")
    print("1. Open Database")
    print("2. Close Database")
    print("3. Save Dataabse")
    print("")

def display_action_menu():
    print("")
    print("1. Create New Event")
    print("2. Edit Event")
    print("")

def record_menu():
    print("")
    print("1. Add Record")
    print("2. Edit Record")
    print("3. Dellete Record")
    print("")

def rider_menu():
    print("")
    print("1. Add Rider")
    print("2. Edit Rider")
    print("3. Add Club Reference")
    print("4. Edit Club Reference")
    print("")

def get_input_text():
    done = False
    while done == False:
        try:
            value = str(input("Please enter an option: "))
            done = True
        except ValueError:
            print("Value not correct data type, please try again")

def get_input_int():
    done = False
    while done == False:
        try:
            value = int(input("Please enter an option: "))
            done = True
        except ValueError:
            print("Value not correct data type, please try again")
