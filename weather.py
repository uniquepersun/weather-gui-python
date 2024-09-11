import tkinter as tk
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("YOUR_API_KEY")

def get_weather(city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

  response = requests.get(url)

  if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
    return data
  else:
    print("Error:", response.status_code)
    return None


def update_weather(city):
  weather_data = get_weather(city)

  if weather_data:
    city_name = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"] - 273.15
    feels_like = weather_data["main"]["feels_like"]
    pressure = weather_data["main"]["pressure"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    visibility = weather_data["visibility"] / 1000
    country_code = weather_data["sys"]["country"]
    sunrise_time = weather_data["sys"]["sunrise"]
    sunset_time = weather_data["sys"]["sunset"]
    
    city_label.config(text=city_name)
    weather_label.config(text=weather_description)
    temp_label.config(text=f"{temperature:.2f} °C (Feels like: {feels_like:.2f} °C)")
    pressure_label.config(text=f"Pressure: {pressure} hPa")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_label.config(text=f"Wind Speed: {wind_speed:.2f} m/s")
    visibility_label.config(text=f"Visibility: {visibility:.2f} km")
    sunrise_label.config(text=f"Sunrise: {sunrise_time}")
    sunset_label.config(text=f"Sunset: {sunset_time}")
    country_label.config(text=f"Country: {country_code}")
  else:
    city_label.config(text="City Not Found")
    weather_label.config(text="")
    temp_label.config(text="")
    pressure_label.config(text="")
    humidity_label.config(text="")
    wind_label.config(text="")
    visibility_label.config(text="")
    sunrise_label.config(text="")
    sunset_label.config(text="")
    country_label.config(text="")

def format_time(timestamp):
  from datetime import datetime, timezone, timedelta

  utc_time = datetime.fromtimestamp(timestamp, timezone.utc)
  local_time = utc_time + timedelta(seconds=root.tk.call('tk:seconds'))
  return local_time.strftime('%H:%M:%S')

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="City:")
city_label.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

temp_label = tk.Label(root, text="")
temp_label.pack()

pressure_label = tk.Label(root, text="")
pressure_label.pack()

humidity_label = tk.Label(root, text="")
humidity_label.pack()

wind_label = tk.Label(root, text="") 
wind_label.pack()

visibility_label = tk.Label(root, text="")
visibility_label.pack()

sunrise_label = tk.Label(root, text="") 
sunrise_label.pack()

sunset_label = tk.Label(root, text="")
sunset_label.pack()

country_label = tk.Label(root, text="") 
country_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()


update_button = tk.Button(root, text="Get Weather", command=lambda: update_weather(city_entry.get()))

update_button.pack()


root.mainloop()

