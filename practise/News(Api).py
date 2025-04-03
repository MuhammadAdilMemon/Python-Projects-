import requests
import json


query=input("What sort of news would you like?")

key="7eead7fe1a554b60841431a94d7c6796"

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey={key}"



r=requests.get(url)

news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------")