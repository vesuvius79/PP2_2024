import datetime

today = datetime.datetime.now()
delta= datetime.timedelta(days=5)

print("Today:", today.strftime("%x"))
print("Five days ago:", (today-delta).strftime("%x"))