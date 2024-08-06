import os
import aiohttp
import asyncio
from dotenv import load_dotenv
from openweather_api_call import fetch_weather_data
from cloud_check import cloud_check

load_dotenv()


def weather_condition_check(settings, db, mac_id):
    if settings.weather_station:
        print(f"logic for weather station")
    else:
        #Have to get the openweather api key, latitude and longitude first
        api_key = db.get_api_key(mac_id)

        api_url = os.getenv('weather_api')

        current_weather_data = fetch_weather_data(api_url, api_key[0]['latitude'], api_key[0]['longitude'],
                                                  api_key[0]['api_key'])
        print('curent weather', current_weather_data)
        hoot_condition = cloud_check(current_weather_data)
        print(hoot_condition)
        if hoot_condition == 0:
            return hoot_condition
        else:
            forecast_weather_call=fetch_weather_data(api_url, api_key[0]['latitude'], api_key[0]['longitude'],
                                                  api_key[0]['api_key'],forecast_type='forecast')
            print(f"forecast check break if condition satisfied",forecast_weather_call)
            # print(f"check distance and return true or false")



