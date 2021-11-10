import datetime

#   current datetime instance
now = datetime.datetime.now()

#   creating date instance
new_year_day = datetime.date(2021, 1, 1)

#   creating datetime instance
some_day = datetime.datetime(2017, 4, 24, 14, 30, 0)

#   to format the output
#   https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(some_day.strftime('%A, %B'))

#   to convert from string
another_day = datetime.datetime.strptime('20-11-2016', "%d-%m-%Y")

#   adding days to a date instance
#   another_day is not modified, you may rebind if you wish
#   https://docs.python.org/3/library/datetime.html#timedelta-objects
#   parameters can be negative as well
date_1 = another_day + datetime.timedelta(days=10)
