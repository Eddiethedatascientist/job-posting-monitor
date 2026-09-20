import requests as r
import json
url = "https://acx.bamboohr.com/jobs/embed2.php?version=1.0.0&format=json"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = r.get(url, headers=headers)
print(response.status_code)
print(response.text[:1000])
print()
data = response.json()
with open("JSON file", "w", encoding="UTF-8") as file:
    json.dump(data, file)
with open("JSON file", "r", encoding="UTF-8") as file:
    data_selected = json.load(file)
print(data_selected)

