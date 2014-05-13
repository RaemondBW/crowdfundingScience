import json

f = open("indiegogo.json")
d = json.load(f)
f.close()

projects = {}
projects["data"] = []

for project in d:
    item = {}
    for key,value in project.items():
        if key == "totalPledged":
            item["goal"] = value
        elif key == "goal":
            item["totalPledged"] = value
        else:
            item[key] = value
    projects["data"].append(item)

f = open("fixedIndiegogo.json", "w")
f.write(json.dumps(projects, indent = 4))
f.close()
