''''List All Users from JSONPlaceholder
API: https://jsonplaceholder.typicode.com/users
Goal: Display names, emails, and company names of all users.'''
import requests

api="https://jsonplaceholder.typicode.com/users"
goal=requests.get(api)
print(goal.status_code)
Response=goal.json()
for user in Response:
    print(f"Name:-{user["name"]}")
    print(f"Email:-{user["email"]}")
    print(f"Company Name:-{user["company"]["name"]}")
