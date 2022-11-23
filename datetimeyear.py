# Write a Python script to display the

#1)Current date and time
from datetime import datetime
current_datetime=datetime.today()
print("The current date and time is:",current_datetime)

#2)Current year
print("The current year is:",current_datetime.year)

#3)Month of year
print("The current month is:",current_datetime.month)

#4)Week number of the year
from datetime import date
today=date.today()
print("Week number of the year is:",today.isocalendar()[1])

#5) Weekday of the week
week_day=today.strftime("%w")
week_day_name=today.strftime("%A")
print("Weekday is:",week_day," and weekday name is:",week_day_name)

#6)Day of year
day_year=today.strftime("%j")
print("Day of the year is:",day_year)

#7)Day of the month
day_month=today.strftime("%d")
print("Day of the month is:",day_month)

#8)Day of week
print("Day of the week is:",week_day_name)
