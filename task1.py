import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your API key
API_KEY = "84e566ae2d568c400b47882fb369b0d8"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching weather data
response = requests.get(URL)
data = response.json()

# Extracting date and temperature
dates = []
temps = []

for item in data["list"]:
    dt_txt = item["dt_txt"]
    temp = item["main"]["temp"]
    dates.append(datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S"))
    temps.append(temp)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(dates, temps, marker='o', linestyle='-', color='teal')
plt.title(f"5-Day Weather Forecast: {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("weather_forecast_chart.png")
plt.show()
