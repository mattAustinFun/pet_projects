from datetime import date, timedelta


def weekday_names():
    """return list of weekdays"""
    return ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']


def weekdays_dict_iso():
    """return dictionary of weekdays,keys weekday shortname, values iso numbers """
    return {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7}


def weekdays_dict_name():
    """return dictionary of weekdays,keys weekday ISO number 1 for Monday and onwards, values are full names """
    return {1: 'MONDAY', 2: 'TUESDAY', 3: 'WEDNESDAY', 4: 'THURSDAY', 5: 'FRIDAY', 6: 'SATURDAY', 7: 'SUNDAY'}


def days_to(end_date: str):
    """return data on the time gap in days
    args:
        start_date(str): iso date format string
        end_date(str): iso date format string
    returns (int): days between not including end date
        """
    interval = date.fromisoformat(end_date) - date.today()
    return interval.days


def full_weeks_to(end_date: str):
    """return data on the time gap in days
    args:
        start_date(str): iso date format string
        end_date(str): iso date format string
    returns (int): complete weeks between,from first Monday
                   to last Sunday
        """

    today = date.today()

    end = date.fromisoformat(end_date)
    interval_days = (end - today).days
    week_started = False
    weeks = 0
    for day in range(1, interval_days):
        the_date = today + timedelta(days=day)
        weekday = the_date.isoweekday()
        if weekday == 1:
            week_started = True
        elif week_started and weekday == 7:
            weeks += 1
    return weeks


def weekday_name_to_iso(weekday_name: str) -> int:
    """return iso integer for a named day of week
    args:
        weekday_name(str): short 3 letter or full name in upper or lowercase
    """
    weekdays = weekdays_dict_iso()
    return weekdays.get(weekday_name.upper()[0:3])


def weekday_iso_to_name(iso_weekday: int) -> str:
    """return weekday full name from iso integer day of week
    args:
        iso_weekday (int):ISO number for day of week starting at 1 for Monday
    """
    weekdays = weekdays_dict_name()
    return weekdays.get(iso_weekday)


def is_weekday(weekday: str) -> bool:
    """return True if a named day of week
        args:
            weekday(str): short 3 letter or full name in upper or lowercase
        """
    weekdays = weekday_names()
    if weekday in weekdays:
        return True
    else:
        return False


def next_weekday_date(weekday: str, date_from: str = date.today().strftime("%Y-%m-%d")) -> str:
    """get date for nearest day of given day of the week """
    the_date = date.fromisoformat(date_from)
    counter = 0
    if is_weekday(weekday):
        while weekday_iso_to_name(the_date.isoweekday()) != weekday:
            counter = + 1
            the_date = the_date + timedelta(days=counter)

    return the_date.strftime("%Y-%m-%d")


def get_weekly_dates(date_to: str
                     , weekday: str = 'NONE'
                     , date_from: str = date.today().strftime("%Y-%m-%d")
                     ) -> list[str]:
    """return a list of dates as iso format string

        ,weekday(str) day of week to filter to, from first instance post date_from
    """
    date_list = []
    iso_start_date = date.fromisoformat(next_weekday_date(weekday, date_from))
    iso_end_date = date.fromisoformat(next_weekday_date(weekday, date_to))
    interval = iso_end_date - iso_start_date
    days_span = interval.days
    for day in range(0, days_span):
        the_date = iso_start_date + timedelta(days=day)
        if the_date.isoweekday() == iso_start_date.isoweekday():
            date_list.append(the_date.strftime("%Y-%m-%d"))
    return date_list


def get_weekly_dates_no_weeks(week_span: int
                              , weekday: str = 'NONE'
                              , date_from: str = date.today().strftime("%Y-%m-%d")
                              ) -> list[str]:
    """return a list of dates as iso format string

        ,weekday(str) day of week to filter to, from first instance post date_from
    """
    date_list = []
    iso_date = date.fromisoformat(next_weekday_date(weekday, date_from))
    days_span = week_span * 7
    for day in range(0, days_span):
        the_date = iso_date + timedelta(days=day)
        if the_date.isoweekday() == iso_date.isoweekday():
            date_list.append(the_date.strftime("%Y-%m-%d"))
    return date_list


def convert_str_to_timedelta(time_string):
    """get a timedelta object from HH:MI:SS"""

    time_values = time_string.split(':')
    hrs = int(time_values[0])
    mins = int(time_values[1])
    secs = int(time_values[2])

    return timedelta(hours=hrs, minutes=mins, seconds=secs)


def get_time_diff_intervals(time_from:str,time_to:str,interval_steps:int = 1)->list[str]:
    """return list of intervening times in between two values entered"""

    timedelta_from = convert_str_to_timedelta(time_from)
    timedelta_to = convert_str_to_timedelta(time_to)
    return_list = [time_from]
    if timedelta_from > timedelta_to:
        time_step = (timedelta_from - timedelta_to)/(interval_steps + 1)
        for idx in range(interval_steps):
            time_interval = timedelta_from-time_step
            return_list.append(str(time_interval))
    elif timedelta_from < timedelta_to:
        time_step = (timedelta_to - timedelta_from)/(interval_steps + 1)
        for idx in range(interval_steps):
            time_interval = timedelta_from+time_step
            return_list.append(str(time_interval))
    else:
        for idx in range(interval_steps):
            return_list.append(time_from)
    return_list.append(time_to)
    return return_list