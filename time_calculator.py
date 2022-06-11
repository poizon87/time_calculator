def add_time(start_time,added_time,weekday=None):

    start = start_time.replace(' ',':')
    st_time = start.split(':')
    st_hour = st_time[0]
    st_minute = st_time[1]
    added = added_time.split(':')
    add_hour = added[0]
    add_minute = added[1]
    of_day = st_time[2]
    over_count = 0
    day_count = 0
    zero = 0
    minutes = 0
    hours = 0
    mil_start = 0

    total_mil_hours = 0

    calc_minutes = int(st_minute) + int(add_minute)

    while calc_minutes >= 60:
        calc_minutes = calc_minutes - 60
        over_count = over_count + 1
    if calc_minutes < 10:
        minutes = f"{zero}{calc_minutes}"#
    else:#
        minutes = calc_minutes#  minutes done

    if of_day == 'PM':
        mil_start = int(st_hour) + 12
        total_mil_hours = mil_start + int(add_hour) + over_count
    else:
        mil_start = int(st_hour)
        total_mil_hours = mil_start + int(add_hour) + over_count

    while total_mil_hours >= 24:
        total_mil_hours = total_mil_hours - 24
        day_count = day_count + 1

    if 0 <= total_mil_hours < 12:
        of_day = "AM"
    else:
        of_day = 'PM'



    #calc_hours = int(st_hour) + int(add_hour) # non military time
    
    #mil_count = calc_hours / 12

    #if calc_hours + over_count <= 24:
        #mil_hours = calc_hours + over_count + 12

    if 13 <= total_mil_hours <= 24:
        hours = total_mil_hours - 12
    
    if hours == 0:
        hours = 12

        #if of_day == 'PM':
            #of_day = 'AM'
        #elif of_day == 'AM':
            #of_day = 'PM'
    #else:
        #hours = calc_hours + over_count

    #print(mil_count)
    #print(mil_hours)
    print(f"{hours}:{minutes} {of_day}")
    #print(total_mil_hours)



    #print(st_hour,st_minute,add_hour,add_minute)
    #print(f"{calc_hour}:{calc_minutes}") # working for low numbers
#add_time("3:00 PM", "3:10")
#add_time("11:43 AM", "0:20")
add_time("10:10 PM", "3:30")