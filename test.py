from datetime import datetime
from pytz import timezone

# Timezone string
tz_string = 'Europe/Bucharest'

# Datetime string
dt_string = '2023-09-07 21:16:00'

# Create a timezone object
tz = timezone(tz_string)

# Parse the datetime string
dt = datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')

dt_aware = tz.localize(dt)

print(dt_aware)