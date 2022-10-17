import datetime
from datetime import date

mytime = datetime.time(18, 20, 31, 2)
print(mytime.minute)
print(mytime)

today = datetime.date.today()
print("Today is", today)
print(today.ctime())

date1 = date(2024,11,2)
date2 = date(2022,10,17)
result = date1-date2
print(result.days)

datetime1 = datetime.datetime(2024,11,2,22)
datetime2 = datetime.datetime(2022,10,17,12)
result = datetime1-datetime2
print(result)


