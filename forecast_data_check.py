from datetime import datetime


def forecast_data_check(forecast_response_data):
    try:

        unix_time = forecast_response_data['hourly'][1]['dt']
        time = datetime.fromtimestamp(unix_time)
        time_now = datetime.now()
        time_diffrence = time - time_now
        minutes = time_diffrence.total_seconds() // 60

        # if the time is less than 15 minutes that means the forecast is for like next 15 minutes which wont be an
        # updated one ,so we choose the next hour

        if minutes <= 15:
            forcast_condition_id = forecast_response_data['hourly'][2]['weather'][0]['id']


        else:
            forcast_condition_id = forecast_response_data['hourly'][1]['weather'][0]['id']

        return forcast_condition_id




    except Exception as e:
        return "Error", e
