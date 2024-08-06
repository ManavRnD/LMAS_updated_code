def cloud_check(weather_data):
    true=1
    false=0

    #thunderstorm
    if 232>=weather_data >=200:
        return true
    # rain
    elif 511>=weather_data >= 500:
        return true
    #drizzle
    elif 321 >= weather_data >=301:
        return true
    #shower rain
    elif 531>= weather_data>= 520:
        return true
    #tornado
    elif weather_data == 781:
        return true
    elif weather_data == 751:
        return true
    elif weather_data == 762:
        return true

    else:
        return false