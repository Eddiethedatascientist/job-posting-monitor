import json
with open("JSON file", "r", encoding="UTF-8") as file:
    raw_data = json.load(file)
print(raw_data.keys())
print(raw_data["departments"])
print(len(raw_data["departments"]))
print(raw_data["departments"][0])
print()
print(raw_data["departments"][1])
print(raw_data["departments"][0].keys())
print()
print(raw_data["departments"][0]["positions"])
print(len(raw_data["departments"][0]["positions"]))
print(raw_data["departments"][0]["positions"][0])
#Extract the job innformation
extracted_dict = {}
for i, item in enumerate(raw_data["departments"]):
    new_key = raw_data["departments"][i]["label"]
    extracted_dict[new_key] = []
    for item in raw_data["departments"][i]["positions"]:
        if item not in extracted_dict[new_key]:
            extracted_dict[new_key].append(item)
print()
print()
print("The data structure after extraction")
print(extracted_dict)
with open("JSON extracted file", "w", encoding="UTF-8") as file:
    json.dump(extracted_dict, file)
