import json
import requests

title = 'ESPN: The Worldwide Leader in Sports'

title = "{\"texts\": [\"" + title + "\"]}"

response = requests.post('https://api.uclassify.com/v1/uclassify/iab-taxonomy/classify', data=title, headers = {'Authorization': 'Token ' + "TgKtVaTl6qFL"})

data = response.json()

obj = json.dumps(data[0])
loaded = json.loads(obj)

list_json = loaded['classification']

category = {}
greater_prob = 0
for p in list_json:
    if p['p'] >= greater_prob:
        greater_prob = p['p']
        category.update(p)

print(category)

top_tier_cat = category['className'].split("_")[0]