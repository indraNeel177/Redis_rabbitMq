from datetime import datetime
import json
from random import randint

fuel_data = {'values': {'1': [[1640751985, 3120.3, 3120.3], [1640751985, 3120.3, 3120.3]], '2': [[1640751985, 1306, 1306], [1640751985, 1306, 1306]], '3': [[1640751985, 3327.7, 3327.7], [1640751985, 3327.7, 3327.7]], '4': [[1640751985, 4608, 4608], [1640751985, 4608, 4608]]}, 'tanks': [{'tankNumb': 3, 'tankName': ''}, {'tankNumb': 2, 'tankName': ''}, {'tankNumb': 1, 'tankName': ''}, {'tankNumb': 4, 'tankName': ''}]}
gps_data = {'status': {'code': 0, 'message': 'OK'}, 'track': [{'date': 1640751985, 'direction': 35, 'latitude': 22.0272138, 'longitude': 88.0834907, 'speed': 14.1, 'satellitesCount': 20}]}



if len(gps_data) > 0:
    # fuel_data = self.omnicomm_api.fuel_level(vehicle_id=self.vehicle_id, time_begin=time_begin,
    #                                          time_end=time_end)
    fuel_data = fuel_data
    # utility.loginfo(" ------------Fuel data------------- : " +
    #                 str(fuel_data) + ' time-begin' + str(datetime.fromtimestamp(time_begin).strftime('%c'))
    #                 + ' time_end' + str(datetime.fromtimestamp(time_end).strftime('%c')))
    data_list = []
    time_stamp = []
    for entry in sorted(gps_data):
        if entry == "track":
            for x in gps_data.get(entry):
                time_stamp.append(x.get('date'))
    print(time_stamp)
    for entry in sorted(gps_data):
        data = {'device_id': "HDK",
                'gps': gps_data.get(entry),
                'ignition':  1,
                'tanks': {}}
        # data['ignition'] = state_data.get('currentIgn')
        # data['gps']['speed'] = 5
        if fuel_data:
            for tank_entry in fuel_data["values"]:
                if tank_entry == "1" or tank_entry == "5":
                    for x in fuel_data["values"][tank_entry]:
                        print(x[0] in time_stamp)
                        if len(x) > 0 and x[0] in time_stamp:
                            time_dict = {'eD': x[0], 'rV': x[1], 'aV': x[2]}
                            data['tanks']["1,5"] = time_dict
                else:
                    for x in fuel_data["values"][tank_entry]:
                        if len(x) > 0 and x[0] in time_stamp:
                            time_dict = {'eD': x[0], 'rV': x[1], 'aV': x[2]}
                            data['tanks'][tank_entry] = time_dict
        # data['gps']['date'] = data['gps']['date'] + difference
    data_list.append(data)
data = {"DevId": "HDK_10",
        "type": "tug_boat",
        "data": data_list}

print(data)

