import datetime

today = datetime.datetime.now()
a = today.replace(microsecond=0)

print(a)