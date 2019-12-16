import requests
import re

one_string = input().strip()
two_string = input().strip()

try:
    def connect(url):
        res = requests.get(url)
        content = res.text
        pattern = r"href=[\'\"]?([^\'\" >]+)"
        return re.findall(pattern, content)

    check = "No"
    checklist = connect(one_string)

    if len(checklist) > 0:
        for url in checklist:
            urls = connect(url)
            if two_string in urls:
                check = "Yes"
                break
    print(check)

except Exception:
    print("No")




