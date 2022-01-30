

final_fuel_json = {}
fuel_json_redis = {"fuel_data_100": {"1,5": [169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0, 169.0], "2": [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150], "3": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], "4": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]}}


tank_mapping  = {'HDK_HDK_TUGB_0002': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 5, 'sensor_id': 14}, 
'2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 6, 'sensor_id': 6}, 
'3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 8, 'sensor_id': 8}, 
'4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 9, 'sensor_id': 9}}, 
'HDK_HDK_TUGB_0010': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 14, 'sensor_id': 19},
 '2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 15, 'sensor_id': 16}, 
 '3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 16, 'sensor_id': 17}, 
 '4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 17, 'sensor_id': 18}}}

device_id = 'HDK_HDK_TUGB_0010'


for master_tank_data in tank_mapping[device_id]:
    if len(fuel_json_redis["fuel_data_100"][master_tank_data]) > 1:
        fuel_json_redis["fuel_data_100"][master_tank_data] = fuel_json_redis["fuel_data_100"][master_tank_data][:1]
        fuel_values = [fuel_value for fuel_value in fuel_json_redis["fuel_data_100"][master_tank_data] if fuel_value != '']
        if len(fuel_values) > 0:
            final_fuel_json[master_tank_data] = max(set(fuel_values), key=fuel_values.count) * 10
            print(final_fuel_json)