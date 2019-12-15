import requests

with open("index.txt") as pw:
    line = pw.read().splitlines()

api_url = "http://numbersapi.com/"
api_end = "/math?json=true"

for i in line:
    res = requests.get(api_url + i + api_end)
    data = res.json()
    if data["found"]:
        print("Interesting")
    else:
        print("Boring")
