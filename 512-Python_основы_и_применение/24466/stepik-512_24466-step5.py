import datetime

y, m, n = str(input()).split()
y, m, n = int(y), int(m), int(n)
d = int(input())
date = datetime.date(y, m, n) + datetime.timedelta(days=d)
print(date.year, date.month, date.day)
