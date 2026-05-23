import requests


city_input = input("Enter a city: ")
city = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city_input}&count=1")
data  = city.json()
xy = (data["results"][0]["latitude"] ,data["results"][0]["longitude"] )
lat = data["results"][0]["latitude"]
long = data["results"][0]["longitude"] 
print(xy)
weather= requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true")
weatherdata = weather.json()
print(f"The temperature is {weatherdata["current_weather"]["temperature"]}")


