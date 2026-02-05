import json

# data = '{"name": "Kavya", "active": true}'
# parsed = json.loads(data)

# print(parsed)



data = {"id": 1, "active": True}
json_str = json.dumps(data)

print(type(json_str))