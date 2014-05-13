import json

# f = open("valuesByCategoryUSD2.json")
# d = json.load(f)
# f.close()

projects = {}

def getAmount(amount):
    amount = amount.replace(",","")
    try:
        amount = int(amount.replace("$",""))
    except:
        return 0
    return amount

# for category in d["data"]:
#     categories.append(category["category"])

f = open("kickstarter.json")
d = json.load(f)
f.close()

for project in d:
    category = project["category"]
    category = category.replace("\n","")
    if category not in projects:
        projects[category] = []
    item = {}

    if project["currency"] != "USD":
        continue

    for key, value in project.items():
        if key == "levels":
            continue

        if key == "title":
            value = value.replace(" \u2014 Kickstarter", "")
        value = value.replace("\n","")
        item[key] = value

    projects[category].append(item)

for category, projectList in projects.items():
    projectData = {}
    projectData["data"] = projectList
    f = open("categoryData/" + category + ".json", 'w')
    f.write(json.dumps(projectData, indent=4))
    f.close()
