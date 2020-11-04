def add_time(start, duration, day_of_week=False):

    # Extract values from the start time
    split_start_time = start.split(":")
    start_hours = int(split_start_time[0])
    start_minutes = int(split_start_time[1].split(" ")[0])
    am_or_pm = split_start_time[1].split(" ")[1]

    # Extract the values from the duration time
    split_duration_time = duration.split(":")
    duration_hours = int(split_duration_time[0])
    duration_minutes = int(split_duration_time[1])

    hours = int(start_hours + duration_hours)
    minutes = start_minutes + duration_minutes

    # Need to:
          
    
    # The function should add the duration time to the start time and return the result
    # If the result will be the next day, it should show (next day) after the time
    # If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later
    # If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result
    # The day of the week in the output should appear after the time and before the number of days later



    # print(hours)
    # print(minutes)
    # print(start_hours)
    # print(start_minutes)
    # print(start_hours + start_minutes)
    # print(am_or_pm)

    # print(duration_hours)
    # print(duration_minutes)
    # print(duration_hours + duration_minutes)

    return split_start_time

add_time("3:30 PM", "2:12")