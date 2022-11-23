#Write a Python program to subtract five days from current date

from datetime import date, timedelta
d = date.today() - timedelta(days=5)
print("Five days before current date is:",d)
