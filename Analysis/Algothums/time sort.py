times = [] # list of all the events times
changes = True
while changes != False:
    changes = False
    for count in range(len(times)):
        if times[count] > times[count + 1]:
            hold_times = times[count]
            times[count] = times[count + 1]
            times[count + 1] = hold_times
            changes = True
        
            
