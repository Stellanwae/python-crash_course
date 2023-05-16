import json

username = input("What is your name?")
filename = 'name.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll rememeber you when you come, {username}")
    