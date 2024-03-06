import requests
import json
import pyttsx3

city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=057aa2d0f8894e5386073510240503&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

audio = pyttsx3.init()
audio.say(f" 'The Current Weather in the {city} is {w} degrees' " )
audio.runAndWait()