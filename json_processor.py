import json

data = {
    "users": [
        {"name": "Flor", "role": "Engineer"},
        {"name": "Moon", "role": "Designer"}
    ]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    content = json.load(f)

for user in content["users"]:
    print(f"{user['name']} - {user['role']}")
