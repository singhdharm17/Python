# Weather forecasting organization wants to show is it day or night. So, write a program for such organization to
# find whether is it dark outside or not. Hint: Use time module.

import time
from datetime import datetime

current_time = time.localtime()
current_time = time.strftime("%HH:%MM", current_time)
print("The current time in your Timezone is: ", current_time)


def part_of_day(c_hour):
    return (
        "Its Bright at the moment" if c_hour >= 5 or c_hour <= 18
        else "Its dark at the moment"
    )


c_hour = datetime.now().hour
print(part_of_day(c_hour))
