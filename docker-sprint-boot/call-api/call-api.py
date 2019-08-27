#Import the modules
import requests
import json

# Get the feed
r = requests.get("http://calculator/hello")
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)

print(data)