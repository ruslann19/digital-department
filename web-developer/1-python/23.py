import requests
import pickle

from pprint import pprint

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
users = {u["id"]: {
    "id": u["id"],
    "username": u["username"],
    "email": u["email"],
    "posts": 0,
    "comments": 0
} for u in users}

posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()

for post in posts:
    users[post["userId"]]["posts"] += 1

users = {u["email"]: u for u in users.values()}

for comment in comments:
    if comment["email"] in users:
        users[comment["email"]]["comments"] += 1

users = list(users.values())

response = requests.post("https://webhook.site/018ee168-4f1f-48c3-8859-63365975980f", json={"statistics": users})

with open("solution.pickle", 'wb') as f:
    pickle.dump(response, f)
