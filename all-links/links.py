import requests
import re

link = input().strip()
result = ""

res = requests.get(link)
content = res.text

pattern = r'''<a (.*?)href=['"](.*?)['"]'''
urls = re.findall(pattern, content)

url_set = set()
url_list = []

for url in urls:
    url = url[1]
    params = url.split("/")
    if params[0] != "..":
        if params[0] == "http:" or params[0] == "https:" or params[0] == "ftp:":
            protocol = params[2].split(":")
            url_set.add(protocol[0])
        else:
            protocol = params[0].split(":")
            url_set.add(protocol[0])

for elem in url_set:
    url_list.append(elem)

url_list.sort()
result = "\n".join(url_list)

print(result)