from datetime import datetime, timedelta


# date = datetime.now() 
# h = []


# for x in range(97):
#     date = datetime.now().date()- timedelta(days=x)
#     h.append(str(date))

# print(h)
def time_z ():
    v = datetime.strptime("2022-01-17 16:56:00", '%Y-%m-%d %H:%M:%S')
    c = datetime.strptime("2022-01-17 13:20:15", "%Y-%m-%d %H:%M:%S")
    return (v-c).seconds

# print(time_z())

print(int(datetime.now().timestamp())- 1646390650 > 43200)

j = 1646637566 + 900

print(j)

g = "2022-03-07"


to_time  = datetime.strptime(g+" "+ "23:59:59", '%Y-%m-%d %H:%M:%S')

from_date = datetime.strptime(g+" "+ "00:00:00", '%Y-%m-%d %H:%M:%S')-timedelta(hours=5,minutes=30)

print(to_time,  from_date)