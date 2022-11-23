#Write a Python program to get week number from 16/06/2015
import datetime
date=datetime.date(2015,6,16)
week_num=date.isocalendar()[1]
print(week_num)