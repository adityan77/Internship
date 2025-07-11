import requests

# -------- CONFIG --------
CITY = "Mumbai"
OPENWEATHER_API_KEY = "your_api_key_here"  # Replace with your actual API key
TEMP_THRESHOLD = 30  # Celsius

# -------- STEP 1: Get Weather Data --------
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}"

response = requests.get(weather_url)

if response.status_code == 200:
    data = response.json()

    # Extract temperature in Kelvin and convert to Celsius
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Current temperature in {CITY}: {temp_celsius:.2f}°C")

    if temp_celsius > TEMP_THRESHOLD:
        message = f"🌡️ Alert! Current temperature in {CITY} is {temp_celsius:.2f}°C, which is above {TEMP_THRESHOLD}°C."
        print(message)
    else:
        print("✅ Temperature is normal. No alert needed.")
else:
    print("❌ Failed to get weather data. Error code:", response.status_code)
