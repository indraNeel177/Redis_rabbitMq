import datetime


g = "2022-01-07 08:43:47"
h = "2022-01-07 09:35:47"

j = datetime.datetime.strptime(h, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(g, "%Y-%m-%d %H:%M:%S")

print(j.total_seconds())