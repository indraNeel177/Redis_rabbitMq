from numpy import dtype
import pandas as pd
from sqlalchemy import table
from math import isnan

arrival_merge_mapping_data = {'R_Key': 'R_Key', 'FlightStatus': 'FlightStatus_Arrival', 'STA': 'STA',
                                  'ATA': 'ATA', 'AircraftIATA': 'AircraftIATA_Arrival',
                                  'Belt': 'Belt', 'FromAirport_ICAOCode': 'FromAirport_ICAOCode', 'FlightNumber':
                                      'FlightNumber_Arrival', 'Bay': 'Bay',
                                  'FromAirport_IATACode': 'FromAirport_IATACode', 'ETA': 'ETA',
                                  'Belt_LastBag': 'Belt_LastBag',
                                  'Via1': 'Via1_Arrival', 'FlightType': 'FlightType', 'GMRPK': 'GMRPK_Arrival',
                                  'Belt_FirstBag': 'Belt_FirstBag', 'OperationUnit': 'OperationUnit',
                                  'FromAirport': 'FromAirport', 'TerminalArrival': 'TerminalArrival',
                                  'Airline': 'Airline', 'On_Block_Time': 'On_Block_Time',
                                  'AircraftRegistration': 'AircraftRegistration_Arrival', 'PassengerCount':
                                      'PassengerCount_Arrival', 'Runway': 'Runway_Arrival', 'AircraftIcao':
                                      'AircraftIcao_Arrival', 'AllocatedBay': 'AllocatedBay', 'FlightArrivalId':
                                      'FlightArrivalId', 'ServiceType': 'ServiceType_Arrival',
                                  'ParkingStandOpenTime':
                                      'ParkingStandOpenTime_Arrival', 'ParkingStandCloseTime':
                                      'ParkingStandCloseTime_Arrival',
                                  'OperationalStatus': 'OperationalStatus_Airrival',
                                  'GroundHandlers': 'GroundHandlers_Arrival', 'SharedInfo': 'SharedInfo_Arrival',
                                  'ActualBay': 'ActualBay', 'AircraftType': 'AircraftType_Arrival',
                                  'Category': 'Category'}
merge_departure_maping = {'ATD': 'ATD', 'ToAirport_ICAOCode': 'ToAirport_ICAOCode', 'FlightNumber':
        'FlightNumber_Departure', 'SecondGate': 'SecondGate', 'Via4':
                                  'Via4_Departure', 'Via2': 'Via2_Departure', 'Via3': 'Via3_Departure',
                              'FirstGateCloseTime': 'FirstGateCloseTime', 'SecondGateCloseTime':
                                  'SecondGateCloseTime', 'SecondGateOpenTime': 'SecondGateOpenTime',
                              'FirstGate': 'FirstGate', 'STD': 'STD', 'ETD': 'ETD', 'Bay': 'Bay_Departure',
                              'GMRPK': 'GMRPK_Departure', 'GateFinalCallTime': 'GateFinalCallTime',
                              'ToAirport': 'ToAirport', 'ToAirport_IATACode': 'ToAirport_IATACode',
                              'FirstGateOpenTime': 'FirstGateOpenTime', 'R_Key': 'R_Key', 'Off_Block_Time':
                                  'Off_Block_Time', 'TerminalDeparting': 'TerminalDeparting',
                              'AircraftRegistration': 'AircraftRegistration_Departure',
                              'ScheduleCheckInOpenTime': 'ScheduleCheckInOpenTime', 'FlightDepartureId':
                                  'FlightDepartureId', 'OperationalStatus': 'OperationalStatus_Departure',
                              'AircraftIcao': 'AircraftIcao_Departure', 'ActualCheckInOpenTime':
                                  'ActualCheckInOpenTime', 'CheckinCounterOrigin': 'CheckinCounterOrigin',
                              'FlightStatus': 'FlightStatus_Departure', 'CheckinCounterDestination':
                                  'CheckinCounterDestination', 'GroundHandlers': 'GroundHandlers_Departure',
                              'ParkingStandCloseTime': 'ParkingStandCloseTime', 'ScheduleCheckInCloseTime':
                                  'ScheduleCheckInCloseTime', 'SharedInfo': 'SharedInfo_Departure',
                              'DestinationTerminal': 'DestinationTerminal', 'PassengerCount':
                                  'PassengerCount_Departure', 'Via1': 'Via1_Departure',
                              'ActualCheckInCloseTime': 'ActualCheckInCloseTime', 'ParkingStandOpenTime':
                                  'ParkingStandOpenTime_Departure', 'Runway': 'Runway_Departure',
                              'FirstGateScheduleCloseTime': 'FirstGateScheduleCloseTime', 'ServiceType':
                                  'ServiceType_Departure', 'FirstGateScheduleOpenTime':
                                  'FirstGateScheduleOpenTime', 'OperationUnit': 'OperationUnit',
                              'Logid': 'FlightDepartureId', 'AircraftType': 'AircraftType_Departure',
                              'AircraftIATA': 'AircraftIATA_Departure'}

arrival_db_column_list = ['R_Key', 'ATA', 'FlightNumber', 'ETA', 'SharedInfo', 'Via1',
                              'ToAirport_IATACode', 'Belt_LastBag', 'ParkingStandCloseTime',
                              'OperationalStatus', 'AircraftIcao', 'ParkingStandOpenTime',
                              'STA', 'ToAirport_ICAOCode', 'AircraftRegistration', 'FlightType', 'Bay',
                              'Airline', 'GMRPK', 'Belt_FirstBag', 'TerminalArrival', 'OperationUnit',
                              'ToAirport', 'ServiceType', 'FlightStatus', 'On_Block_Time', 'GroundHandlers',
                              'PassengerCount', 'Belt', 'Runway', 'FromAirport_IATACode', 'schedule_date',
                              'FromAirport', 'FromAirport_ICAOCode', 'Via2', 'Via3', 'Via4', 'Via5', 'Remark',
                              'ActualBay', 'AircraftType', 'AircraftIATA']


departure_column_list = ['ATD', 'R_Key', 'FlightNumber', 'ETD', 'ScheduleCheckInCloseTime', 'Via1',
                             'FirstGateCloseTime', 'ScheduleCheckInOpenTime', 'FirstGateOpenTime', 'STD', 'Airline',
                             'CheckinCounterOrigin', 'GateFinalCallTime', 'Bay', 'GMRPK', 'ParkingStandOpenTime',
                             'AircraftIcao', 'FirstGate', 'FlightStatus', 'AircraftRegistration',
                             'DestinationTerminal', 'Off_Block_Time', 'GroundHandlers', 'ActualCheckInOpenTime',
                             'PassengerCount', 'OperationalStatus', 'FromAirport_IATACode', 'CheckinCounterDestination',
                             'FlightType', 'Runway', 'ToAirport_IATACode', 'TerminalDeparting', 'OperationUnit',
                             'SharedInfo', 'ActualCheckInCloseTime', 'ParkingStandCloseTime', 'ServiceType',
                             'FirstGateScheduleCloseTime', 'FirstGateScheduleOpenTime', 'FromAirport',
                             'ToAirport_ICAOCode', 'FromAirport_ICAOCode','schedule_date','ToAirport','Via3','Via2',
                             'AircraftType', 'AircraftIATA']



at= pd.read_csv("/home/indraneel/WORK/vsc/Redis_rabbitMq/query_master/Datetime/arrvil.csv")
dt = pd.read_csv("/home/indraneel/WORK/vsc/Redis_rabbitMq/query_master/Datetime/depart.csv")

at = at.dropna(axis='columns')
dt = dt.dropna(axis='columns')


at = at.to_dict(orient="index")
dt = dt.to_dict(orient="index")



def map_fields(init_dict, map_dict, res_dict=None):

    res_dict = res_dict or {}
    for k, v in init_dict.items():
        if k in map_dict:
            # print("Key: ", k)
            if isinstance(v, dict):
                # print("value is a dict - recursing")
                v = map_fields(v, map_dict[k])
            elif k in map_dict.keys():
                # print("Remapping:", k, str(map_dict[k]))
                k = str(map_dict[k])
            res_dict[k] = v
    return res_dict



def ins_query_maker(tablename, rowdict):
    keys = tuple(rowdict)
    dictsize = len(rowdict)
    keys_column = '('+','.join(rowdict.keys())+')'
    sql = ''
    for i in range(dictsize) :
        if(type(rowdict[keys[i]]).__name__ == "str"):
            sql += "\"" + str(rowdict[keys[i]]) + "\""
        else:
            sql += str(rowdict[keys[i]])
        if(i< dictsize-1):
            sql += ", "
    
    query = "insert into " + str(tablename) + " " + str(keys_column) + " values (" + sql + ")"
    # print(query) # for demo purposes we do this
    return(query) #in real code we do this

at  = map_fields(init_dict=at[0],map_dict=arrival_merge_mapping_data)
dt = map_fields(init_dict=dt[0],map_dict=merge_departure_maping)



mt = {**at, **dt}



print(ins_query_maker(tablename="DailyFlightSchedule_Merged", rowdict=mt))
