import numpy

tank_mapping =  {'HDK_HDK_TUGB_0002': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 5, 'sensor_id': 14}, 
'2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 6, 'sensor_id': 6},
 '3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 8, 'sensor_id': 8},
  '4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 9, 'sensor_id': 9}}, 
  'HDK_HDK_TUGB_0010': {'1,5': {'tank_name': 'Reserve Tank 01', 'tank_capacity': 27700, 'tank_id': 14, 'sensor_id': 19}, 
  '2': {'tank_name': 'Reserve Tank 02', 'tank_capacity': 27700, 'tank_id': 15, 'sensor_id': 16}, 
  '3': {'tank_name': 'Service Tank 01', 'tank_capacity': 5000, 'tank_id': 16, 'sensor_id': 17},
   '4': {'tank_name': 'Service Tank 02', 'tank_capacity': 5000, 'tank_id': 17, 'sensor_id': 18}}}



device_id = "HDK_HDK_TUGB_0010"
entry =  {'device_id': 'HDK_HDK_TUGB_0010', 'gps': {'date': 1640160680, 'direction': 308, 'latitude': 22.0315556, 'longitude': 88.0876124, 'speed': 0, 'satellitesCount': 18}, 'ignition': 1, 'tanks': {'1,5': {'rV': 1255.4, 'aV': None, 'eD': 1640160680}, '2': {'rV': 10073.4, 'aV': None, 'eD': 1640160680}}}


fuel_json = {tank_mapping[device_id][str(tank)]['tank_name']: entry['tanks'][tank] for tank in
                         entry['tanks']}

# entry_data = np.array((entry['gps']['date'], entry['gps']['latitude'], entry['gps']['longitude'],
#                                            entry['gps']['speed']))

print(fuel_json)

for tank in entry['tanks']:
    entry_data = np.append(entry_data, [entry['tanks'][tank]])

print(e)