# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		import requests, json 
		api_key = "070f3c2952168202c7a321026dac81ce"
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		loc = str(tracker.get_slot('location'))
		complete_url = base_url + "appid=" + api_key + "&q=" + loc 
		response = requests.get(complete_url) 
		x = response.json()
		#print(x)
		if x["cod"] != "404":
			y = x["main"]
			temperature = y["temp"]
			current_pressure = y["pressure"]
			humidity = y["humidity"]
			z = x["weather"]
			condition = z[0]["description"]
			#city= x["name"]
			wind_mph = x["wind"]["speed"]
			response = """It is currently {} at the moment. The temperature is {} kelvin unit, the humidity is {}% and the wind speed is {} mph.""".format(condition,temperature,humidity,wind_mph)
			dispatcher.utter_message(response)
			return [SlotSet('location',loc)]
		else:
			print(" City Not Found ")
			response = """" City Not Found sorry """
			dispatcher.utter_message(response)
			return [SlotSet('location',loc)]