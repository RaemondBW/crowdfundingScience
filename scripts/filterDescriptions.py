import json
f = open("kickstarter.json")
d = json.load(f)
f.close()

#levels = {}
filteredData = []

#for i in range(100):

for project in d:
    #    for amount, value in project["levels"].items():
    #        value["backers"]
    item = {}
    for key, value in project.items():
        if key not in ["description", "levels"]:
            item[key] = value
    filteredData.append(item)


f = open("noDescriptions.json", 'w')
f.write(json.dumps(filteredData, indent=4))
f.close()