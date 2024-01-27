from datetime import datetime

def date_passed(todays_date, scheduled_date):
    format_pattern = "%dth %B"
    todays_date_parsed = datetime.strptime(todays_date, format_pattern)
    scheduled_date_parsed = datetime.strptime(scheduled_date, format_pattern)
    difference = todays_date_parsed - scheduled_date_parsed

    if difference.days <0:
        print("Scheduled date has passed")
    elif difference.days >0:
        print("Scheduled date is yet to pass")
    else:
        print("Scheduled date is today")

date_passed("26th March", "25th March") 
date_passed("26th March", "26th March") 
date_passed("26th March", "27th March")