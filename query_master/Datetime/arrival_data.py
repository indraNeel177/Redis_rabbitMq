from numpy import dtype
import pandas as pd
from sqlalchemy import table
from math import isnan
from datetime import datetime, timedelta


at= pd.read_csv("/home/indraneel/Pictures/DailyFlightScheduleArrival_GMR (11).csv")
# 'schedule_date'  'Category'


l = ['STA', 'ETA', 'ATA', 'On_Block_Time', 'Sensor_On_Block_Time', 'Sensor_ATA', 'created_at', 'modified_at', 'schedule_date' ]



for j in l:
    at[j].str

print(at.info())
# at['STA'] = at['STA'].fillna('')
# at['STA'] = at['STA'].apply(lambda x : ((datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S")) if x != '' else x))

for name in l:
    try:
        at[name] = at[name].fillna('')
        at[name] = at[name].apply(lambda x : ((datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S")+ timedelta(days=365)) if x != '' else x))
    except Exception as e:
        # at[name] = at[name].fillna('')
        at[name] = at[name].apply(lambda x : ((datetime.strptime(str(x), "%Y-%m-%d") + timedelta(days=365))) if x != '' else x) 

at['Category'] = at['Category'].apply(lambda x : "platfrom")

print(at)

at.to_csv("/home/indraneel/logs/arrival.csv")
