import requests
import pandas as pd
import json

url = 'https://api-web.nhle.com/v1/roster/TOR/current'
raw = requests.get(url).content
parsed = json.loads(raw)
print(json.dumps(parsed, indent=4))

f = open("output.txt", 'w')
f.write(str(json.dumps(parsed, indent=4)))


