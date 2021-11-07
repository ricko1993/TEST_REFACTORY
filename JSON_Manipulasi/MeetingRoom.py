import json
file = "data.json"
with open(file, "r") as json_file:
    data = json.load(json_file)
    name_data = (data["data"])
    for i in name_data:
        if i["placement"]['room_id']==3:
            name = (i["placement"]['name'])
            print(name)