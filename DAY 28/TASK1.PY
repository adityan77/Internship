import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print("Status Code:", response.status_code)

posts = response.json()
print("First Post:", posts[0])
