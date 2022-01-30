tank_mapping  = {'HDK_HDK_TUGB_0002': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 5, 'sensor_id': 14}, 
'2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 6, 'sensor_id': 6}, 
'3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 8, 'sensor_id': 8}, 
'4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 9, 'sensor_id': 9}}, 
'HDK_HDK_TUGB_0010': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 14, 'sensor_id': 19},
 '2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 15, 'sensor_id': 16}, 
 '3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 16, 'sensor_id': 17}, 
 '4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 17, 'sensor_id': 18}}}
def redis_fuel_monitor(fuel_json):
    try:
        device_id = "HDK_HDK_TUGB_0010"
        final_fuel_json = {}
        fuel_json_redis = {}
        if fuel_json_redis:
            fuel_json_redis = json.loads(fuel_json_redis)
            for master_tank_data in tank_mapping[device_id]:
                fuel_data = 'aV' if master_tank_data in fuel_json and fuel_json[master_tank_data]["aV"] else 'rV'
                if ',' in master_tank_data:
                    # master_tank_data_list = master_tank_data.split(',')
                    master_tank_data_list = master_tank_data
                    if master_tank_data_list in fuel_json and master_tank_data_list in fuel_json:
                        fuel_json_redis["fuel_data_100"][master_tank_data].append(((fuel_json[master_tank_data_list][fuel_data] + fuel_json[master_tank_data_list]["fuel_data"]) / 2) // 10)
                    elif master_tank_data_list in fuel_json:
                        fuel_json_redis["fuel_data_100"][master_tank_data].append(fuel_json[master_tank_data_list][fuel_data] // 10)
                    # elif master_tank_data_list[1] in fuel_json:
                    #     fuel_json_redis["fuel_data_100"][master_tank_data].append(fuel_json[master_tank_data_list[1]][fuel_data] // 10)
                    else:
                        fuel_json_redis["fuel_data_100"][master_tank_data].append('')
                    fuel_json.pop(master_tank_data_list[0], None)
                    fuel_json.pop(master_tank_data_list[1], None)
                else:
                    if master_tank_data not in fuel_json:
                        fuel_json_redis["fuel_data_100"][master_tank_data].append('')
                    else:
                        fuel_json_redis["fuel_data_100"][master_tank_data].append(fuel_json[master_tank_data][fuel_data] // 10)
        else:
            fuel_json_redis = {"fuel_data_100": {}}
            for master_tank_data in tank_mapping[device_id]:
                fuel_data = 'aV' if  master_tank_data in fuel_json and fuel_json[master_tank_data]["aV"] else 'rV'
                if ',' in master_tank_data:
                    # master_tank_data_list = master_tank_data.split(',')
                    master_tank_data_list = master_tank_data
                    if master_tank_data_list in fuel_json and master_tank_data_list in fuel_json:
                       fuel_json_redis["fuel_data_100"][master_tank_data] = [((fuel_json[master_tank_data_list][fuel_data] + fuel_json[master_tank_data_list][fuel_data]) / 2) // 10]
                    elif master_tank_data_list in fuel_json:
                        fuel_json_redis["fuel_data_100"][master_tank_data] = [fuel_json[master_tank_data_list][fuel_data] // 10]
                    # elif master_tank_data_list[1] in fuel_json:
                    #     fuel_json_redis["fuel_data_100"][master_tank_data] = [fuel_json[master_tank_data_list[1]][fuel_data] // 10]
                    else:
                        fuel_json_redis["fuel_data_100"][master_tank_data] = ['']
                    fuel_json.pop(master_tank_data_list[0], None)
                    fuel_json.pop(master_tank_data_list[1], None)
                else:
                    if master_tank_data not in fuel_json:
                        fuel_json_redis["fuel_data_100"][master_tank_data] = ['']
                    else:
                        fuel_json_redis["fuel_data_100"][master_tank_data] = [fuel_json[master_tank_data_list][fuel_data] // 10]
        for master_tank_data in tank_mapping[device_id]:
            if len(fuel_json_redis["fuel_data_100"][master_tank_data]) > 1:
                fuel_json_redis["fuel_data_100"][master_tank_data] = fuel_json_redis["fuel_data_100"][master_tank_data][:1]
                fuel_values = [fuel_value for fuel_value in fuel_json_redis["fuel_data_100"][master_tank_data] if fuel_value != '']
                if len(fuel_values) > 0:
                    final_fuel_json[master_tank_data] = max(set(fuel_values), key=fuel_values.count) * 10
                    print(final_fuel_json)
        # self.redis.set_val(key=Constants.live_tracking_fuel_data_key.format(self.device_id), val=json.dumps(fuel_json_redis))
        return final_fuel_json
    except Exception as e_:
        # exc_type, exc_obj, exc_tb = sys.exc_info()
        print(e_)


import json
# f = open("", "r")
with open('query_master/Datetime/work_fuel.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

l = []

for x in mylist:
    if x not in '          EXCEPTION             ':
        m = x.split("  PUBLISH SUCCESS           : ")
        l.append(m[-1])
        

g = []
for y in l:
    y = json.loads(y)
    for z in y["data"]:
        redis_fuel_monitor(z["tanks"])