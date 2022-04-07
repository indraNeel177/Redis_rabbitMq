from numpy import dtype
import pandas as pd
from sqlalchemy import table
from math import isnan
from datetime import datetime, timedelta


at= pd.read_csv("/home/indraneel/Pictures/DailyFlightScheduleDeparture_GMR (8).csv")
# 'schedule_date'  'Category'

print(list(at.columns))


l = [ 'STD', 'ETD', 'ATD', 'Sensor_ATD', 'Off_Block_Time', 'Sensor_Off_Block_Time',  'schedule_date',  'created_at', 'modified_at']


for j in l:
    at[j].str

# print(at.info())
# at['STA'] = at['STA'].fillna('')
# at['STA'] = at['STA'].apply(lambda x : ((datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S")) if x != '' else x))

for name in l:
    try:
        at[name] = at[name].fillna('')
        at[name] = at[name].apply(lambda x : ((datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S")+ timedelta(days=365)) if x != '' else x))
    except Exception as e:
        try:
            at[name] = at[name].fillna('')
            at[name] = at[name].apply(lambda x : ((datetime.strptime(str(x), "%Y-%m-%d") + timedelta(days=365))) if x != '' else x) 
        except:
            continue

# at['Category'].loc[(at['Category'] )] = "platform"

at['Category'] = at['Category'].apply(lambda x : "platfrom")


print(at)

at.to_csv("/home/indraneel/logs/depart.csv")
