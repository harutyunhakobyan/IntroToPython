import datetime
import time
import calendar

tday = datetime.date.today()

print(datetime.datetime.now())
print('Current year:', tday.year)
print('Current month: ', tday.month)
print('Day of the week:', tday.isoweekday())

tdelta = datetime.timedelta(days = 5)

print('Date today + 5 days: ', datetime.datetime.now() + tdelta)
print('Date today - 5 days: ', datetime.datetime.now() - tdelta)