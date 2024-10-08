import aiohttp
import asyncio
from fetch_weather import fetch_weather
from forecast_data_check import forecast_data_check

async def get_current_weather(apiurl, latitude, longitude, api_key):
    # this is for curretn weather call
    async with aiohttp.ClientSession() as session:
        weather_url = f"{apiurl}weather?lat={latitude}&lon={longitude}&appid={api_key}"
        data = await fetch_weather(session, weather_url)
        weather_condition_id = data['weather'][0]['id']
        return weather_condition_id

async def get_forecast_weather(apiurl,latitude,longitude,api_key):
    #forecast call
    async with aiohttp.ClientSession() as session:
        forecast_url=f"{apiurl}onecall?lat={latitude}&lon={longitude}&appid={api_key}"
        data= await fetch_weather(session,forecast_url)
        # here we need to do a forecast check and get the id for the next hour
        forecast_id=forecast_data_check(data)
        return forecast_id

def fetch_weather_data(apiurl,latitude,longitude,api_key,forecast_type='current'):
    if forecast_type == 'current':
        return asyncio.run(get_current_weather(apiurl,latitude,longitude,api_key))
    elif forecast_type == 'forecast':
        return asyncio.run(get_forecast_weather(apiurl,latitude,longitude,api_key))