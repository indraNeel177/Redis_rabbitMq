from datetime import datetime


gps_data = {'status': {'code': 0, 'message': 'OK'}, 
'track': [{'date': 1637669132, 'direction': 171, 'latitude': 22.4612572, 'longitude': 88.3594911, 'speed': 0, 'satellitesCount': 19}]}

fuel_data = {'status': {'code': 0, 'message': ''}, 'tankData': [{'data': [{'rV': 0, 'aV': None, 'eD': 1637649082}], 
'tankCapacity': 4100, 'tankNumber': 1}, {'data': [{'rV': 1652.3, 'aV': None, 'eD': 1637649082}], 'tankCapacity': 4100, 'tankNumber': 2}]}


gps_data = {entry.get('date'): entry for entry in gps_data.get('track')}
fuel_data = {entry.get('tankNumber'): {'tank_number': entry.get('tankNumber'), 'tank_capacity': entry.get('tankCapacity'), 'data': {level_1_entry.get('eD'): level_1_entry for level_1_entry in entry.get('data')}} for entry in fuel_data.get('tankData')}

# print(fuel_data)
# print(sorted(gps_data))

# data = {}
# for tank_entry in fuel_data:
#     try:
#         data['tanks'][tank_entry] = fuel_data[tank_entry]['data'][entry]
#     except Exception as e_:
#         print("Exception in fetching fuel data during " + str(e_))
# print(data)

# gps_data = [1637313738, 1637313743]
# fuel_data  = {1: {'tank_number': 1, 'tank_capacity': 4100, 'data': {1637313443: {'rV': 15.6, 'aV': None, 'eD': 1637313443}}},
#  2: {'tank_number': 2, 'tank_capacity': 4100, 'data': {1637313733: {'rV': 1671.3, 'aV': None, 'eD': 1637313733}, 1637313738: {'rV': 1671.3, 'aV': None, 'eD': 1637313738}, 1637313743: {'rV': 1671.3, 'aV': None, 'eD': 1637313743}, 1637313748: {'rV': 1671.3, 'aV': None, 'eD': 1637313748}, 1637313753: {'rV': 1671.3, 'aV': None, 'eD': 1637313753}}}}

if len(gps_data) > 0:
    data_list = []
    for entry in sorted(gps_data):
        print( datetime.fromtimestamp(gps_data.get(entry).get('date')).minute == 30)
        data = {'device_id': "",
                                 'gps': gps_data.get(entry),
                                 'ignition': 0 if datetime.fromtimestamp(gps_data.get(entry).get('date')).minute == 30 and randint(1, 4) == 1 else 1,
                                'tanks': {}}
        #                # data['ignition'] = state_data.get('currentIgn')
        data['gps']['speed'] = 5
        for tank_entry in fuel_data:
            try:
                if tank_entry == 1 or tank_entry == 5: 
                    data['tanks']["1,5"] = fuel_data[tank_entry]['data'][entry] 
                else:
                    data['tanks'][tank_entry] = fuel_data[tank_entry]['data'][entry]
            except Exception as e_:
                pass
                # print(("Exception in fetching fuel data during " + e_.__str__()))
                        # data['gps']['date'] = data['gps']['date'] + difference
            print(data)
            # data_list.append(data)
        

data = {'DevId': "kk",
                            'type': 'tug_boat',
                            'data': data_list}

