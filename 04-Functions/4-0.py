def time_string(hours,minutes,time_format):
    
    if not (0 <= hours <= 23):
        return "Enter valid hours"
    elif not (0 <= minutes <= 59):
        return "Enter valid minutes"

    if time_format == '24':
        return f"{hours:02}:{minutes:02}, {time_format}"
    elif time_format == '12':
        if hours == 0:
            formated_hour=12
            suffix = 'am'
        elif hours < 12:
            formated_hour = hours
            suffix = 'am'
        elif hours == 12:
            formated_hour=hours
            suffix='am'
        else:
            formated_hour=hours-12
            suffix='pm'
        return f"{formated_hour}:{minutes} {suffix},{time_format}"
    else:
        return "Enter valid time format, use 12 or 24"
print(time_string(15, 38, '24'))  # '15:38'
print(time_string(8, 3, '24'))    # '08:03'
print(time_string(0, 5, '24'))    # '00:05'
print(time_string(11, 15, '12'))  # '11:15am'
print(time_string(0, 7, '12'))    # '12:07am'
print(time_string(7, 30, '12'))   # '7:30am'
print(time_string(12, 46, '12'))  # '12:46pm'
print(time_string(13, 10, '12'))  # '1:10pm'
print(time_string(19, 2, '12'))   # '7:02pm'