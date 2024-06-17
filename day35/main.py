import requests
from twilio.rest import Client




OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast" 
api_key = "53807585ce22ed4d8b4df550d1beed7d"
account_sid = 'ACb0efc8ed8dcf40654f4f67412a690fda'
auth_token = '49192f670fb8ed0600434bef81965e5b'


weather_params = {
    "lat":45.5579,
    "lon":94.1632,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['list'][0]['weather'][0]['id'])

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        from_='+12183062962',
        body='It going to rain today My Carlito, Remember to bring an umbrella ☂️.',
        to='+610480578314'
    )

    print(message.status)
 

