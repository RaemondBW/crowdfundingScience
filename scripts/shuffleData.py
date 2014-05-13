import json
import random

f = open('fixedIndiegogo.json')
d = json.load(f)
f.close()

projects = {}
data = d["data"]

random.shuffle(data)
projects["data"] = data

f = open('randomizedIndiegogo.json', 'w')
f.write(json.dumps(projects, indent = 4))
f.close()
