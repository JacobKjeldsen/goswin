import requests
import json
import os
import time

class BeachAPI:
    def __init__(self):
        self.url = "http://api.vandudsigten.dk/beaches"
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def get_beach_status(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()
    

    '''
    Example of the JSON input:
    {
        "id": 85,
        "municipality": "Aarhus",
        "municipality_url": "<a target='_blank' href=\"https://www.aarhus.dk\">Hjemmeside</a>",
        "name": "150 Egå S",
        "description": "",
        "latitude": 56.2058,
        "longitude": 10.2859,
        "comments": "Permanent badeforbud - Risiko for sundhedsfare ",
        "facilities": "",
        "links": [
            "<a target='_blank' href=\"https://www.aarhus.dk/borger/kultur-natur-og-idraet/ud-i-naturen/vil-du-paa-stranden\">Badevandsside</a>"
        ],
        "data": [
            {
                "date": "2024-02-18",
                "water_quality": "1",
                "water_temperature": "2",
                "current_speed": "0,2",
                "current_direction": "18",
                "air_temperature": "3",
                "wind_speed": "9",
                "wind_direction": "171",
                "wind_direction_display": "351",
                "weather_type": "12",
                "precipitation": "11"
            },
            {
                "date": "2024-02-19",
                "water_quality": "1",
                "water_temperature": "2",
                "current_speed": "0,0",
                "current_direction": "21",
                "air_temperature": "5",
                "wind_speed": "7",
                "wind_direction": "283",
                "wind_direction_display": "463",
                "weather_type": "3",
                "precipitation": "0"
            },
            {
                "date": "2024-02-20",
                "water_quality": "1",
                "water_temperature": "3",
                "current_speed": "0,0",
                "current_direction": "21",
                "air_temperature": "6",
                "wind_speed": "5",
                "wind_direction": "257",
                "wind_direction_display": "437",
                "weather_type": "3",
                "precipitation": "0"
            },
            {
                "date": "2024-02-21",
                "water_quality": "1",
                "water_temperature": "3",
                "current_speed": "0,0",
                "current_direction": "21",
                "air_temperature": "4",
                "wind_speed": "6",
                "wind_direction": "251",
                "wind_direction_display": "431",
                "weather_type": "3",
                "precipitation": "0"
            }
        ]
    }
    extract the water temperature, date and quality status from the JSON input and return it. Should be the date from today.
    eg.:
    "date": "2024-02-18",
                "water_quality": "1",
                "water_temperature": "2",
    
    return 2, 1
    '''
    # Given a beach name, return the current status of the beach
    def get_status(self, json_input, beach_name):
        for beach in json_input:
            if beach.get('name') == beach_name:
                for data in beach["data"]:
                    if data.get('date') == time.strftime("%Y-%m-%d"):
                        return data["water_temperature"], data["water_quality"]
        return None, None
    
    def get_location(self, json_input, beach_name):
        for beach in json_input:
            if beach.get('name') == beach_name:
                return beach["latitude"], beach["longitude"]
        return None, None