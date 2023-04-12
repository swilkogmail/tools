#!/usr/bin/env python3
import datetime
from datetime import date as dt

print(f" dir list of strings for datetime {dir(datetime)}")
print(f" dir list of strings for datetime.date {dir(datetime.date)}")

" datetime has no __init__"

# fully qualified from the root of the module
today = datetime.date.today()
print(today)
# from the 'from' import using an alias
today = dt.today()
print(today)
# day of the week
weekday = dt.weekday(today)
print(f"{dt.weekday.__doc__} i.e. Today is: {weekday}")
# timetuple although time is truncated
tt = dt.timetuple(today)
print(f"{dt.timetuple.__doc__} i.e. Today is: {tt}")

x = datetime.datetime.now()
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%c"))
print(x.strftime("%B"))