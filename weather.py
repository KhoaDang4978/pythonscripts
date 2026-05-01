# This is a Ho Chi minh weather forecast
import requests
def get_description(code):
    if code == 0:
        return "Clear sky"
    elif code <= 3:
        return "Partly cloudy"
    elif code <= 12:
        return "Mist/fog"
    elif code <= 29:
        return "Thunderstorm"
    elif code <= 59:
        return "Drizzle"
    elif code <= 65:
        return "Rain"
    elif code <= 67:
        return "Heavy rain"
    else:
        return f"Unknown (code {code})"
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=10.8231&longitude=106.6297&current=temperature_2m,wind_speed_10m,weather_code")
data = response.json()
print("⛅️ Ho Chi Minh City Weather")
print("---------------------------")
print(f"Temperature: {data['current']['temperature_2m']}°C")
print(f"Wind speed: {data['current']['wind_speed_10m']} km/h")
code = data['current']['weather_code']
print(f"Condition: {get_description(code)}")