import json
import requests
    
print("Name of Artist:")
Name = str(input())
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=30&term={Name}")
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])