import json
with open("JSON extracted file", "r", encoding="UTF-8") as file:
    data = json.load(file)
print(data.keys())
normalized_list = []
for item in data.keys():
    key = item
    for num in data[key]:
        structure_dict = {}
        structure_dict["job_id"] = num["id"]
        structure_dict["title"] = num["name"]
        structure_dict["url"] = num["url"]
        structure_dict["location"] = num["location"]
        if key == "":
            key = "Open application"
        structure_dict["department"] = key
        normalized_list.append(structure_dict)
print(normalized_list)
print()
for item in normalized_list:
    print(item)
print()
print(len(normalized_list))
with open("JSON normalised data", "w", encoding="UTF-8") as file:
    json.dump(normalized_list, file)
