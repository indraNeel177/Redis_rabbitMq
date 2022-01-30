# import pymysql
 
# class FlightActivity():
#     def __init__(self,host='db-avileap-staging.ckfsniqh1gly.us-west-2.rds.amazonaws.com',user='avileap_curd', password = "avileap^7t*ALP",db='AviLeap'):
#         self.user = user
#         self.host = host
#         self.db = db
#         self.password = password
 
#     def getConn(self):
#         self.connection = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
#         self.cursor = self.connection.cursor()
    
#     def FlightQuery(self):
#         #query="select * from DailyFlightSchedule_Merged WHERE OperationUnit = 13 and Off_Block_Time is not NULL and FlightNumber_Arrival regexp 'KA|KU|KE|MI|UK|TG|9I|2T|SQ|AI|MK|TR|IX|CX|MH|EY|AK|CV|CQ' ORDER by LogId desc limit 10"
#         query="select * from EquipActivityLogs order by LogId desc limit 10"
#         self.getConn()
#         self.cursor.execute(query)
#         output = self.cursor.fetchall()
#         print(output)
 
# ob1=FlightActivity()
# ob1.FlightQuery()

gps_data = {'status': {'code': 0, 'message': 'OK'}, 'track': [{'date': 1640748385, 'direction': 160, 'latitude': 22.0262671, 'longitude': 88.0829291, 'speed': 0, 'satellitesCount': 19}, 
{'date': 1640748395, 'direction': 160, 'latitude': 22.0262671, 'longitude': 88.0829291, 'speed': 0, 'satellitesCount': 19}, {'date': 1640748375, 'direction': 160, 'latitude': 22.0262671, 'longitude': 88.0829291, 'speed': 0, 'satellitesCount': 19}]}


fuel_data = {'values': {'1': [], '2': [], '3': [], '4': []}, 'tanks': [{'tankNumb': 2, 'tankName': ''}, {'tankNumb': 4, 'tankName': ''}, {'tankNumb': 1, 'tankName': ''}, {'tankNumb': 3, 'tankName': ''}]}


time_stamp = []
data_list = []
fuel_data_list = []

track = 

for entry in gps_data:
    if entry == "track":
        for x in gps_data.get(entry):
            time_stamp.append(x.get('date'))

for fuel in fuel_data['values']:
    for data in fuel_data["values"][fuel]:
        if fuel == '1':
            fuel = "1,5"
        else:
            fuel = str(fuel)
        data.append(fuel)
        fuel_data_list.append({data[0]:data})


# {"DevId": "HDK_HDK_TUGB_0010", "type": "tug_boat", "data":
#  [{"device_id": "HDK_HDK_TUGB_0010", "gps": {"date": 1640228791, "direction": 172, "latitude": 22.0263589, "longitude": 88.0829597, "speed": 0, "satellitesCount": 20},
#   "ignition": 1, "tanks": {"1,5": {"rV": 1044.5, "aV": null, "eD": 1640228791}, "2": {"rV": 9999.3, "aV": null, "eD": 1640228791}}}]}

# [{'device_id': 'HDK', 'gps': {'date': 1640748385, 'direction': 160, 'latitude': 22.0262671, 'longitude': 88.0829291, 'speed': 0, 'satellitesCount': 19},
#  'ignition': 1, 'tanks': {'1,5': {'eD': 1640748385, 'rV': 3050.3, 'aV': 3051.5}, '2': {'eD': 1640748385, 'rV': 1306, 'aV': 1305}, 
#  '3': {'eD': 1640748385, 'rV': 3353.6, 'aV': 3354.3}, '4': {'eD': 1640748385, 'rV': 4608, 'aV': 4608}}}]

for gps_entry in gps_data['track']:
    gps_date = gps_entry.get("date")
    tanks_data_entry = {}
    for fuel_entry in fuel_data_list:
        if fuel_entry.get(gps_date):
            data = fuel_entry.get(gps_date)
            tanks_data = {data[-1]:{'eD': data[0], 'rV': data[1], 'aV': data[2]}}
            tanks_data_entry.update(tanks_data)
    data = {'device_id': "HDK",
            'gps': gps_entry,
            'ignition': 1,
            'tanks': tanks_data_entry if tanks_data_entry else {}}
    data_list.append(data)


print(data_list)



# for entry in sorted(gps_data):
#     if entry == "track":
#         data = {'device_id': "HDK_10",
#                 'gps': gps_data.get(entry),
#                 'ignition':  1,
#                 'tanks': {}}
#         if fuel_data:
#             for tank_entry in fuel_data["values"]:
#                 # print(tank_entry)
#                 if tank_entry == "1" or tank_entry == "5":
#                     for x in fuel_data["values"][tank_entry]:
#                         if x[0] in time_stamp:
#                             time_dict = {'eD': x[0], 'rV':x[1], 'aV':x[2]}
#                             data['tanks']["1,5"] = time_dict
#                 else:
#                     for x in fuel_data["values"][tank_entry]:
#                         if x[0] in time_stamp:
#                             time_dict = {'eD': x[0], 'rV':x[1], 'aV':x[2]}
#                             data['tanks'][tank_entry] = time_dict
#                     # data['tanks'][tank_entry] = fuel_data[tank_entry]['data'][entry]
#         data_list.append(data)
data_list = []

# for entry in sorted(gps_data):
#     if entry == "track":
#         for x in gps_data[entry]:
#             data = {'device_id': "HDK_10",
#                 'gps': x,
#                 'ignition':  1,
#                 'tanks': {}}
#             date = x
#             if fuel_data:
#                 for tank_entry in fuel_data["values"]:
#                     # print(tank_entry)
#                     if tank_entry == "1" or tank_entry == "5":
#                         for x in fuel_data["values"][tank_entry]:
#                             if x[0] in time_stamp:
#                                 time_dict = {'eD': x[0], 'rV':x[1], 'aV':x[2]}
#                                 data['tanks']["1,5"] = time_dict
#                     else:
#                         for x in fuel_data["values"][tank_entry]:
#                             if x[0] in time_stamp:
#                                 time_dict = {'eD': x[0], 'rV':x[1], 'aV':x[2]}
#                                 data['tanks'][tank_entry] = time_dict

            
#             data_list.append(data)
        

# print(data_list)