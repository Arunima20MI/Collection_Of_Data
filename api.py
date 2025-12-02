import requests
import pandas as pd

API_KEY = "267f4f1f49933418a86dfe3b3bfa1eaa"   # Replace with your OpenWeatherMap API key
city = "Bhubaneshwar"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
weather = response.json()

data = {
    "City": [city],
    "Temperature": [weather["main"]["temp"]],
    "Humidity": [weather["main"]["humidity"]],
    "Condition": [weather["weather"][0]["description"]]
}

df_api = pd.DataFrame(data)
df_api.to_csv("api_data.csv", index=False)
print("api_data.csv created")