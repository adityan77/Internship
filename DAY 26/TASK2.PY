import requests
import webbrowser

ga="https://dog.ceo/api/breeds/image/random"
goal=requests.get(ga)
j=goal.json()
print(goal.status_code)

webbrowser.open(j["message"])
