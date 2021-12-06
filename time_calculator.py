def add_time(start, duration, day=False):

    # VARIABLES & VALUES

    starting_hour = start.split(":")[0]
    starting_minute = start.split(":")[1].split()[0]
    meridiem = start.split(":")[1].split()[1]
    added_hours = duration.split(":")[0]
    added_minutes = duration.split(":")[1].split()[0]
    added_days = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    starting_day = ""
    final_day = ""
    new_time = ":"

    # ADDING TIME

    minutes_to_hours = 0
    final_minutes = int(starting_minute) + int(added_minutes)

    if final_minutes >= 60:
        final_minutes -= 60
        minutes_to_hours += 1
    if final_minutes < 10:
        new_time = new_time + "0" + str(final_minutes)
    else:
        new_time = new_time + str(final_minutes)

    final_hours = int(starting_hour) + int(added_hours) + minutes_to_hours


    if final_hours > 12:
        while final_hours > 12:
            final_hours -= 12
            if meridiem == "AM":
                meridiem = "PM"
            elif meridiem == "PM":
                meridiem = "AM"
                added_days += 1
    if final_hours == 12 and int(starting_hour) < 12:
        if meridiem == "AM":
            meridiem = "PM"
        elif meridiem == "PM":
            meridiem = "AM"
            added_days += 1
    new_time = str(final_hours) + new_time

    # FINAL DAY

    try:
        starting_day = day.lower().capitalize()
        final_day = (days.index(starting_day) + 1) + added_days
    
        while final_day > 7:
            final_day -= 7
    
        final_day = days[final_day - 1]
    except:
        AttributeError

    # RETURNING

    if starting_day in days:
        if added_days == 0:
            new_time += " " + meridiem + ", " + final_day
        elif added_days == 1:
            new_time += " " + meridiem + ", " + final_day + " " + "(next day)"
        else:
            new_time += " " + meridiem + ", " + final_day + " " + "({} days later)".format(added_days)

    else:
        if added_days == 0:
            new_time += " " + meridiem
        elif added_days == 1:
            new_time += " " + meridiem + " " + "(next day)"
        else:
            new_time += " " + meridiem + " " + "({} days later)".format(added_days)

    return new_time
