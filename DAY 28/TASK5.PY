# 1.	Try accessing a non-existent endpoint (e.g., https://jsonplaceholder.typicode.com/nonexistent).
# 2.	Handle the error (check status code, print an error message if request fails).
# Example Code:
# response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")

import requests
goal=requests.get("https://jsonplaceholder.typicode.com/nonexistent")
j=goal.json()
# print(x)
s=goal.status_code
if(s==200):
    print("Success!!!")
else:
    print("Fail!!!")