from datetime import date, timedelta

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
    for day_int in range(1, interval_days):
        the_date = today + timedelta(days=day_int)
        weekday = the_date.isoweekday()
        if weekday == 1:
            week_started = True
        elif week_started and weekday == 7:
            weeks += 1
    return weeks
