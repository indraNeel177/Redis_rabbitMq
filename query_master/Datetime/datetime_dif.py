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

print(time_z())