import requests
from twilio.rest import Client

#OWM API parameters
api_key = "cfe93827fdb441ee3b08886450e207d6"
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

#Twilio API parameters
account_sid = 'AC3d2bfe5bec186da3891f19e8cb07e88f'
auth_token = '0fd76838276d997cf8fb49e62d75a1d6'

parameters = {
    'lat': -23.534625,   #Sao Paulo
    'lon': -46.699594,
    # 'lat': 22.626070,     #testes com loc da China (chove neste momento)
    # 'lon': 120.358757,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Its raining there')
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body='Vai chover, ao sair, leve um guarda-chuvas!',
        from_= '+14345954165',
        to= '+5511981704765'
    )
    print(message.status)

