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


if __name__ == "__main__":
    value = get_input_time()
    print(value)
