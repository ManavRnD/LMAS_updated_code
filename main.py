## main file to do API CAll:

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ds_condition_check import ds_condition_check
from as_condition_check import as_condition_check
from weather_condition_check import weather_condition_check
from lmas_data_table import MySQLDatabase


#Settings Class ( change to database for production)
class Settings:
    def __init__(self):
        self.check_previous_AS = False  #check if previous AS has triggerd for DS
        self.AS_trigger = 2  # Minutes: sets time in minutes for which AS trigger needs to be checked
        self.DS_AS_trigger_count = 1  # AS trigger count limit/ threshold
        self.multiple_as = True  # default set to only single AS
        self.as_trigger_time = 5  # minutes of as data that will be checked
        self.as_trigger_count = 3  # default 3 triggers in 5 minutes
        self.as_redundant = False  # default treating as3935 as not redundant
        self.as_trigger_short_time = 1  # this is for non-redundat as, here we define time for which
        # we will check if the other as triggerd in that short amount of time ,
        # note that this time should be less than the as_trigger_time
        self.weather_station = True # weather station connected
        # distance for openweather should be set in front end so that the calculations are not to be repeated

    def __repr__(self):
        return f"Settings check_previous_AS={self.check_previous_AS},AS_trigger={self.AS_trigger}"


#Initate the settings
settings = Settings()
#Initiate MYSQL database
db=MySQLDatabase(host='localhost',user="Mepl",password="Mepl@123",database="manav_admin")

#API Call /weatherapi
mac_id = "1234"
daigsat = '1'
as3935 = '0'
battery = '1234'

diagsat = int(daigsat)
as3935 = int(as3935)

#DS settings, set if to check if AS has triggered before:
settings.check_previous_AS = False
settings.AS_trigger = 5
settings.DS_AS_trigger_count = 5

#AS settings:
settings.multiple_as = True
settings.as_trigger_count = 10
settings.as_redundant=False

#WS settings:
settings.weather_station= False

# Based on the settings logic for checking if hoot or not based on DS
if diagsat == 1:
    # ds_return = ds_condition_check(settings, diagsat, as3935,mac_id,db)
    # print(ds_return)
    # as_return = as_condition_check(settings, as3935)
    ws_return = weather_condition_check(settings,db,mac_id)
    print('Ws return',ws_return)
else:
    as_return = as_condition_check(settings, as3935)
    ws_return = weather_condition_check(settings)

##Check the truth table to decide
print('Depending on each resturn we will decide to hoot or not')

print(f"This hoot or not then we need to add a snippet of code to check if thsi should be updated to user via "
      f"notification or not")