import datetime
import time
import calendar

num_y = int(input("Number of years: "))
num_d = int(input("Number of days: "))

tdelta_years = datetime.timedelta(days = num_y*365)
tdelta_days = datetime.timedelta(days = num_d)


print("Current date:",datetime.datetime.now())
print('Given years:', num_y)
print('Given days:', num_d)
print('Final date:', datetime.datetime.now() + tdelta_years + tdelta_days)