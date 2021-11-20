import json
import requests

def temperature(t,location):
    response=requests.get('https://api.weatherapi.com/v1/forecast.json?key=6e5c16bd95814a9aa1a60221210710&q='+str(location)+'&days=1&aqi=yes&alerts=no')
    json_data = json.loads(response.text)
    try:
        temp = str(json_data['current'][t])
        x = "It is {}°C in {}".format(temp, location)
    except:
        x="Error"
    finally:
        return x

def air_q(x,location):
    response = requests.get('https://api.weatherapi.com/v1/forecast.json?key=6e5c16bd95814a9aa1a60221210710&q='+str(location)+'&days=1&aqi=yes&alerts=no')
    json_data = json.loads(response.text)
    try:
        bolna=str(int(json_data["current"]['air_quality'][x]))
        bolna="Currently there are {}μg/m3 {} in {}'s Air.".format(bolna,x,(location.upper()))
    except:
        bolna="Error"
    finally:
        return bolna
