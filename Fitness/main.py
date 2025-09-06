from datetime import date, timedelta
from chrono_tools.time_intervals import full_weeks_to

bob_death_anniversary = '2025-11-28'
weeks_to = full_weeks_to(bob_death_anniversary)

print(f"{weeks_to} weeks until {bob_death_anniversary} ")