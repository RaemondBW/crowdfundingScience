import json

f = open("kickstarter.json")
d = json.load(f)
f.close()

categories = {}

def getAmount(amount):
    amount = amount.replace(",","")
    try:
        amount = int(amount.replace("$",""))
    except:
        return 0
    return amount

for project in d:
    category = project["category"]
    category = category.replace("\n","")
    if project["currency"] == "USD":
        if category not in categories:
            item = {}
            item["raised"] = 0
            item["backers"] = 0
            item["numProjects"] = 0
            item["successful"] = 0
            categories[category] = item
        categories[category]["backers"] += int(project["backers"].replace(",",""))
        categories[category]["raised"] += float(project["totalPledged"])
        categories[category]["numProjects"] += 1
        categories[category]["successful"] += int (float(project["totalPledged"]) >= float(project["goal"]))
    #categories[category]["successful"]
    #it might be interesting to add the percentage of successful projects for each category here

f = open("valuesByCategoryUSD2.json", 'w')
f.write(json.dumps(categories, indent=4))
f.close()
