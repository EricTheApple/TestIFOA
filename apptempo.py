#from dotenv import load_dotenv
import requests
import streamlit as st
import pandas as pd

#load_dotenv()
#API_key = os.getenv('api_key_weathermap')
API_key = st.secrets["API_key_weather"]

st.title('Che tempo fa?')

city_name = st.text_input("Digita il nome della città che ti interessa",'Fusignano')

if st.button('Cerca', help='fai partire la ricerca'):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    result = requests.get(url)
    json = result.json()

    if json['weather'][0]['main'] == 'Clouds':
        st.header('Cielo nuvoloso :cloud:')
    elif json['weather'][0]['main'] == 'Clear':
        st.header('Cielo sereno :fire: ')
        #'broken clouds'

    kelvin = -273.15
    temperatura = str(int(json['main']['temp']+kelvin))+"°C"
    temperatura_min = str(int(json['main']['temp_min']+kelvin))+"°C"
    temperatura_max = str(int(json['main']['temp_max']+kelvin))+"°C"
    vento = str(json['wind']['speed'])+" km/h"
    umidità = json['main']['humidity']
    pressione = json['main']['pressure']


    a, b = st.columns(2)
    c, d = st.columns(2)

    a.metric("Temperatura", temperatura, border=True)
    b.metric("Vento", vento, border=True)

    c.metric("Umidità", umidità, border=True)
    d.metric("Pressione", pressione, border=True)

    latitudine = json['coord']['lat']
    longitudine = json['coord']['lon']
    coordinate = pd.DataFrame([[latitudine, longitudine]],columns = ['LAT','LON'])

    st.map(data=coordinate,color="#FFF200")

    
    

#st.markdown()

# {'coord': {'lon': 11.9571, 'lat': 44.4651}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]
#  , 'base': 'stations', 
#  'main': {'temp': 291.99, 'feels_like': 291.86, 'temp_min': 291.43, 'temp_max': 291.99, 'pressure': 1014, 'humidity': 74, 'sea_level': 1014, 'grnd_level': 1014},
#    'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 99, 'gust': 2.74}, 'clouds': {'all': 100}, 'dt': 1747139701, 'sys': {'type': 2, 'id': 2009678, 'country': 'IT', 'sunrise': 1747108023, 'sunset': 1747161007},
#      'timezone': 7200, 'id': 6536752, 'name': 'Fusignano', 'cod': 200}