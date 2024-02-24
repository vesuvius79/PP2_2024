import datetime

d1 = datetime.datetime.now()
d2 = datetime.datetime(2024, 2, 12)
dif = d1-d2
print(int(dif.total_seconds()))