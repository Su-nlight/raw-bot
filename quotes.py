import requests
import json

def quote():
    response= requests.get('https://zenquotes.io/api/random')
    json_data= json.loads(response.text)
    quote = json_data[0]['q'] + "  - " +json_data[0]['a']
    return(quote)
def daily_quote():
    response= requests.get('https://zenquotes.io/api/today')
    json_data = json.loads(response.text)
    daily_quote = json_data[0]['q']  + "  - " + json_data[0]['a']
    return(daily_quote)
    
