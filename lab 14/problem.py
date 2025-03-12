from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", formatted_time)


#task 2
from datetime import datetime

today = datetime.today()

new_year = datetime(today.year + 1, 1, 1)

days_remaining = (new_year - today).days

print("Days until New Year's Eve:", days_remaining)


#task 3
import time
from datetime import datetime, timedelta

seconds = int(input("Enter countdown time in seconds: "))

end_time = datetime.now() + timedelta(seconds=seconds)

while seconds:
    print(f"Time remaining: {seconds} seconds")
    time.sleep(1)  # Ожидание 1 секунда
    seconds -= 1

print("Timer finished!")


#task 4
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print(calendar.month(year, month))


