import requests
import json

def url():
  url_linl = { "auth_url" :"https://omnindia.asymbix.net/auth/login?jwt=1",
  "event_url" : "https://omnindia.asymbix.net/ls/api/v1/reports/events/11098?timeBegin=1639630726&timeEnd=1639634206&Parameter=1"}
  return url_linl
 


def auth():
  url = "https://omnindia.asymbix.net/auth/login?jwt=1"
  payload = json.dumps({
  "login": "zestiot_new",
  "password": "9CzeZ0yIQL"
  })
  headers = {
  'Key': 'Content-Type',
  'Value': 'application/json',
  'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return json.loads(response.text)


def event(timeEnd, timeBegin):
  url = "http://omnindia.asymbix.net/ls/api/v1/reports/events/336029300?timeBegin={}&timeEnd={}&Parameter=1".format(timeBegin,timeEnd)
  payload={}
  headers = {
    'Authorization': "JWT " + auth().get("jwt")
  }
  response = requests.request("GET", url, headers=headers, data=payload)

  return json.loads(response.text)

# print(event(timeBegin=1644456651, timeEnd=1644479811))


a = [{'type': 33, 'latitude': 22.0262077, 'longitude': 88.0825808, 'parameters': ['60', '210'], 'timestamp': 1644456750, 'eventAddress': 'Haldia Dock Complex, Haldia, Purba Medinipur, West Bengal, 721604, India'}, {'type': 43, 'latitude': 22.0234679, 'longitude': 88.0809278, 'parameters': ['60', '870'], 'timestamp': 1644457810, 'eventAddress': 'Haldia Dock Complex, Haldia, Purba Medinipur, West Bengal, 721604, India'}, {'type': 98, 'latitude': 22.0234679, 'longitude': 88.0809278, 'parameters': ['300', '870'], 'timestamp': 1644457810, 'eventAddress': 'Haldia Dock Complex, Haldia, Purba Medinipur, West Bengal, 721604, India'}, {'type': 43, 'latitude': 22.0246534, 'longitude': 88.0805496, 'parameters': ['60', '100'], 'timestamp': 1644457950, 'eventAddress': 'Haldia Dock Complex, Haldia, Purba Medinipur, West Bengal, 721604, India'}, {'type': 43, 'latitude': 22.0267639, 'longitude': 88.0823506, 'parameters': ['60', '100'], 'timestamp': 1644458230, 'eventAddress': 'Haldia Dock Complex, Haldia, Purba Medinipur, West Bengal, 721604, India'}, {'type': 43, 'latitude': 22.0276585, 'longitude': 88.0833803, 'parameters': ['60', '120'], 'timestamp': 1644458360, 'eventAddress': 'Haldia Dock Complex, Haldia, Purba Medinipur, West Bengal, 721604, India'}]
a= [ dict_ for count, dict_ in enumerate(a) if a[count]['type']== 33]
print(a)

a = {'values': {'1': [0], '2': [7], '3': [9], '4': [8]}, 'tanks': [{'tankNumb': 2, 'tankName': ''}, {'tankNumb': 3, 'tankName': ''}, {'tankNumb': 1, 'tankName': ''}, {'tankNumb': 4, 'tankName': ''}]}
values =[*a['values'].values()]
values = [data for data in values if len (data)==0]
if len(values)>0:
    print("false")
print(values)