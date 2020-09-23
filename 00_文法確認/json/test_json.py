import json

json_file = open('settings.json', 'r')
json_data = json.load(json_file)

print(json_data["data1"])
print(json_data["data2"])
print(json_data["data3"])
