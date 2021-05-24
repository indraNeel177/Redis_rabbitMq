import datetime

t = "2021-05-21 10:30:00"
f = "2021-05-21 10:05:47"

diff = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(f, "%Y-%m-%d %H:%M:%S")

print(diff.seconds)
