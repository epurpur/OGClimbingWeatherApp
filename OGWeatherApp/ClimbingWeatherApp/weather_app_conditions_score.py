#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:32:49 2020

@author: ep9k
"""

#this computes the conditions scores for each city in the selected state

def define_best_daily_conditions(json_data):
    """Defines best daily conditions for the one day forecast"""    
    
    conditions_dict = {}        #Making a dict to store 'Name': 'Conditions_score' as key,value pair
     
    #weather_app_conditions_score.py
    for city in json_data:
        temperature = city['main']['temp'] 
        humidity = city['main']['humidity']
            
        #first convert temperature to celcius (makes math easier)
        temperature = ((temperature - 32) * (5/9))
            
        #conditions receive a penalty of 2x score if below freezing level
        if temperature < 0:
            conditions_dict[city['name']] = (abs(temperature) * humidity * 2)
                
        else:
            conditions_dict[city['name']] = (temperature * humidity)
             
    print(f"Currently, the best conditions are in {min(conditions_dict, key=conditions_dict.get)}.")  
        


def define_best_extended_forecast_conditions(daily_measurement):
    """defines best daily conditions for the 5 day forecast"""
    
    temperature = daily_measurement['main']['temp']
    humidity = daily_measurement['main']['humidity']
    
    #first convert temperature to celsius (makes math easier)
    temperature = ((temperature - 32) * (5/9))
            
    #conditions receive a penalty of 2x score if below freezing level
    if temperature < 0:
        conditions_score = (abs(temperature) * humidity * 2)

    else:
        conditions_score = (temperature * humidity)
        
    return conditions_score
        
