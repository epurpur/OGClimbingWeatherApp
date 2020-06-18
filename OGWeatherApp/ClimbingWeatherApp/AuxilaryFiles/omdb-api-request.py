#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:28:58 2018

@author: ep9k
"""
import logbook
import sys
import json
import requests
from pprint import pprint

###################################

#request is for Boone and Charlottesville. Boone id = 4456703, Charlottesville id = 4752031
city_id = '31209681'

app_log = logbook.Logger('API')


def make_api_request(city_id):
    try:        
        r = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id={city_id}&units=imperial')
        
        data = json.loads(r.text)
        
        #names = data['list']
        for city in data['list']:
            if city['sys']['country'] != 'US':
                print(f"City: {city['name']}, {city['sys']['country']}")
                print(f"Temp today: {city['main']['temp']}")
                print(f"Humidity: {city['main']['humidity']}\n")
            else:
                print(f"City: {city['name']}")
                print(f"Temp today: {city['main']['temp']}")
                print(f"Humidity: {city['main']['humidity']}\n")
    except KeyError:
        msg = 'Something is wrong with the api request. Maybe a city_id is wrong or your API key is bad'
        print("Error! ", msg)
        app_log.warn(msg)
            
            
def init_logging(filename: str = None):
    level = logbook.TRACE            #hierarchy of levels in logging include trace, error, notices, etc. I'm using TRACE so that it is verbose in what it reports.
    
    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application() #uses date as part of logging
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
        
    msg = f"Logging Initialized. level: {level}, mode: {'stdout mode' if not filename else 'file mode: ' + filename}"
    
    logger = logbook.Logger('Startup')
    logger.notice(msg)
            
    
init_logging()
make_api_request(city_id)
