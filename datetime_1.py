import datetime
import pytz

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2008, 8, 19)

print(x)
print(x.strftime("%B"))


# tz = pytz.timezone("Europe/Paris")
# tz = pytz.timezone("Asia/Dubai")
tz = pytz.timezone("Asia/Shanghai")
now_date = datetime.datetime.now(tz)

print(now_date)

# tz = pytz.timezone("Europe/Paris")
# tz = pytz.timezone("Asia/Dubai")
# tz = pytz.timezone("Asia/Shanghai")
# tz = pytz.timezone("Asia/Seoul")
tz = pytz.timezone("Asia/Tashkent")

now_date = datetime.datetime.now(tz)


print(now_date.strftime("%Y-%m-%d"))
print(now_date.strftime("%a"))
print(now_date.strftime("%A"))

print(now_date.strftime("%B %d %H:%M"))