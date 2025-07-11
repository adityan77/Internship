import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "New Post",
    "body": "This is a test post.",
    "userId": 1
}

response = requests.post(url, json=data)
print("New Post:", response.json())
