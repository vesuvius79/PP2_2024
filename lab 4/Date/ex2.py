import datetime

today = datetime.datetime.now()
delta = datetime.timedelta(days=1)

print("yesterday:", (today - delta).strftime("%x"))
print("today:", today.strftime("%x"))
print("tomorrow:", (today + delta).strftime("%x"))