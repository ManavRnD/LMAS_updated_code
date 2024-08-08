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

        #in env file we have the openweatehr url
        api_url = os.getenv('weather_api')

        #fetch weather data is used to do call for both current and forecast, and only the id will be returned
        current_weather_data = fetch_weather_data(api_url, api_key[0]['latitude'], api_key[0]['longitude'],
                                                  api_key[0]['api_key'])
        # print('curent weather', current_weather_data)

        #cloud check to see if holds true for LMAS
        hoot_condition = cloud_check(current_weather_data)

        if hoot_condition == 0:  # remember to change it to 1
            return hoot_condition
        else:
            #forecast call
            forecast_weather_call = fetch_weather_data(api_url, api_key[0]['latitude'], api_key[0]['longitude'],
                                                       api_key[0]['api_key'], forecast_type='forecast')

            hoot_condition = cloud_check(forecast_weather_call)

            if hoot_condition == 0:  # remember to change it to 1
                return hoot_condition
            else:
                print('have to do direction call')

            return 0
