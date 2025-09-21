from datetime import timedelta

from Tools.time_tools.time_intervals import full_weeks_to, get_weekly_dates_no_weeks
from Tools.num_tools.calculations import diff_intervals_list

bob_death_anniversary = '2025-11-28'
weeks_to = full_weeks_to(bob_death_anniversary)

current_time_5k = timedelta(minutes=33, seconds=33)
goal_time_5k = timedelta(minutes=29, seconds=59)

diff_intervals_list


print(f"{weeks_to} weeks until {bob_death_anniversary}")
print(f"5k time in seconds : {current_time_5k.total_seconds()}\n"
      f"Goal time in seconds: {goal_time_5k.total_seconds()}\n"
      f"Goal time diff in seconds: {(current_time_5k - goal_time_5k).total_seconds()}")

# get_weekly_dates('2025-11-29', 'SATURDAY')
