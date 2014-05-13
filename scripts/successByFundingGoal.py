import json
import math

f = open("kickstarter.json")
d = json.load(f)
f.close()

fundingGoal = {}
def getAmount(amount):
    amount = amount.replace(",","")
    try:
        amount = int(amount.replace("$",""))
    except:
        return 0
    return amount

def findRangeLinear(amount):
    amount = amount.replace(",","")
    amount = int(amount.replace("$",""))
    floor = amount/100*100
    return (floor, floor+100)

def findRangeLog(amount):
    amount = amount.replace(",","")
    amount = float(amount.replace("$",""))
    floor = int(math.log(amount, 2))
    return 2**floor, 2**(floor+1)

for project in d:
    goal = project["goal"]
    pledged = project["totalPledged"]
    try:
        range = str(findRangeLog(goal))
    except:
        continue
    if range not in fundingGoal:
        item = {}
        item["numProjects"] = 0
        item["successful"] = 0
        fundingGoal[range] = item
    fundingGoal[range]["numProjects"] += 1
    fundingGoal[range]["successful"] += int(pledged >= goal)

f = open("successByGoal.json", 'w')
f.write(json.dumps(fundingGoal, indent=4))
f.close()
