import json
file = "data.json"
with open(file, "r") as json_file:

    data = json.load(json_file)
    name_data = (data["data"])
    for i in name_data:
        if i["purchased_at"]=="16 Januari 2020":
            name = (i['name'])
            print(name)