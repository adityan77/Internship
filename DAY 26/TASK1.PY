import requests

joke="https://official-joke-api.appspot.com/random_joke"
goal=requests.get(joke)
print(goal.status_code)
print(goal.json())



