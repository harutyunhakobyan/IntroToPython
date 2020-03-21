import datetime
import time
import calendar

bday = datetime.date(1986, 1, 15)
print('Birthday:', bday)
print('Year:', bday.year)
print('Month:', bday.month)
print('Day:', bday.day)
print('Day of the week :', bday.isoweekday())

bday_next = datetime.date(2021, 1, 15)
tday = datetime.date.today()
print('Days left till upcoming birthday:', bday_next - tday)

print ("The calendar of May 2017:")
print(calendar.month(2017, 5))

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)

print('Yesterday: ', yesterday)
print('2 days to yesterday’s date: ',yesterday + datetime.timedelta(days = 2))
print('3 days from yesterday’s date: ',yesterday - datetime.timedelta(days = 3))