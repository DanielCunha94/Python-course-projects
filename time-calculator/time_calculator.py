def add_time(start, duration, day="today"):
    days = [
        "monday", "tuesday", "wednesday", "thusrday", "friday", "saturday",
        "sunday"
    ]
    #destructuring start time
    [start_time, start_period] = start.split(" ")
    [start_h, start_m] = start_time.split(":")

    #destructuring duration
    [duration_h, duration_m] = duration.split(":")

    #add minutes
    minutes_final= (int(start_m)+int(duration_m))%60 
    hours_past = (int(start_m)+int(duration_m))//60

    #add hours
    total_hours = int(duration_h)+hours_past
    days_past = total_hours//24
    hours_to_add = total_hours%24
    start_h =int(start_h)
    if start_period == "PM":
        start_h +=12

    hours_final= (start_h + hours_to_add)%24
    if hours_final >12:
      hours_final -=12
      period = "PM"
    elif hours_final == 12:
      period = "PM"
    elif hours_final == 0:
      hours_final = 12
      period= "AM"
    else:
      period ="AM"

    days_past += (start_h + hours_to_add)//24
    
    if day !="today":
      day = day.lower()
      final_day= days[(days.index(day)+days_past)%7]
      final_day = ", "+ final_day.capitalize() 
    else:
      final_day = ""

    if days_past == 0:
      days_past="";
    elif days_past == 1:
      days_past=" (next day)";
    else:
      days_past = f" ({days_past} days later)"

    minutes_final = minutes_final if minutes_final > 9 else "0"+ str(minutes_final)

    return f"{hours_final}:{minutes_final} {period}{final_day}{days_past}"
