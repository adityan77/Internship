import requests

longitude = 72.8777
latitude = 19.0760

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&current=temperature_2m"
)


goal = requests.get(url)
r = goal.json()


temp = r["current"]["temperature_2m"]
print(f"Current Temperature: {temp}°C")


if temp > 30:
    print("It’s Hot!!!")
elif temp < 15:
    print("It’s Cold!!!")
else:
    print("Weather is Moderate.")
