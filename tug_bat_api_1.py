final_fuel_json = {}
fuel_json_redis = {"1,5": [], "2": [], "3": [], "4": []}
fuel_json = {"1,5": {"eD": 1640806767, "rV": 3059.4, "aV": 3059.1},
          "2": {"eD": 1640806767, "rV": 1295, "aV": 1295},
          "3": {"eD": 1640806767, "rV": 3036.3, "aV": 3036.3},
          "4": {"eD": 1640806767, "rV": 4608, "aV": 4608}}
tank_mapping  = {'HDK_HDK_TUGB_0002': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 5, 'sensor_id': 14}, 
'2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 6, 'sensor_id': 6}, 
'3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 8, 'sensor_id': 8}, 
'4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 9, 'sensor_id': 9}}, 
'HDK_HDK_TUGB_0010': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 14, 'sensor_id': 19},
 '2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 15, 'sensor_id': 16}, 
 '3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 16, 'sensor_id': 17}, 
 '4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 17, 'sensor_id': 18}}}
for fuel_data in fuel_json:
    try:
        fuel_data_entry = float(fuel_json.get(fuel_data).get("aV", fuel_json.get(fuel_data).get("rV")))
        fuel_json_redis.get(fuel_data).append(fuel_data_entry)
    except Exception:
        pass
for fuel_data in fuel_json:
    try:
        fuel_data_entry = float(fuel_json.get(fuel_data).get("aV", fuel_json.get(fuel_data).get("rV")))
        fuel_json_redis.get(fuel_data).append(fuel_data_entry)
        if len(fuel_json_redis[fuel_data]) > 1:
            fuel_json_redis[fuel_data] = fuel_json_redis[fuel_data][:-1]
            fuel_values = [fuel_value for fuel_value in fuel_json_redis[fuel_data] if fuel_value]
            if len(fuel_values) > 0:
                 final_fuel_json.update({tank_mapping["HDK_HDK_TUGB_0010"][fuel_data]["tank_name"]:max(set(fuel_values), key=fuel_values.count)})
    except Exception:
        pass


print(fuel_json_redis)
print(final_fuel_json)

# for master_tank_data in tank_mapping["HDK_HDK_TUGB_0010"]:
#     if len(fuel_json_redis[master_tank_data]) > 1:
#         fuel_json_redis[master_tank_data] = fuel_json_redis[master_tank_data][:1]
#         fuel_values = [fuel_value for fuel_value in fuel_json_redis[master_tank_data] if fuel_value]
#     if len(fuel_values) > 0:
#          print(fuel_values)
#          final_fuel_json.update({tank_mapping["HDK_HDK_TUGB_0010"][master_tank_data]["tank_name"]:max(set(fuel_values), key=fuel_values.count)})
         



# print(final_fuel_json)
        