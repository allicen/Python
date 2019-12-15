import requests
import json

client_id = "***"
client_secret = "***"

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j["token"]

headers = {"X-Xapp-Token": token}

with open("index.txt") as pw:
    data = pw.read().splitlines()

people = []

for line in data:
    r = requests.get("https://api.artsy.net/api/artists/" + line, headers=headers)
    r.encoding = "utf-8"
    j = json.loads(r.text)
    people.append([int(j["birthday"]), j["sortable_name"]])

people.sort()

for person in people:
    print(person[1])