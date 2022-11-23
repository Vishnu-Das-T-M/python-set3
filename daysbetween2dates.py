#Write a Python program to get days between two dates
#Exampe: days between 28/02/2000 and  28/02/2001

from datetime import date
t1=date(year=2001,month=2,day=28)
t2=date(year=2000,month=2,day=28)
t3=t1-t2
print(t3)
