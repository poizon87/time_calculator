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
    mil_start = 0
    total_mil_hours = 0

    weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


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

    if 13 <= total_mil_hours <= 24:
        total_mil_hours = total_mil_hours - 12

    if total_mil_hours == 0:
        total_mil_hours = 12

    
    if day_count > 1:
        days = f"{' ('}{day_count}{' days later'}{')'}"
    elif day_count == 1:
        days = 'next day'

    print(f"{total_mil_hours}:{minutes} {of_day}{','}{days}")
    #print(total_mil_hours)
    #print(hours)


#add_time("3:00 PM", "3:10")
#add_time("11:43 AM", "0:20")
#add_time("10:10 PM", "3:30")
#add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")