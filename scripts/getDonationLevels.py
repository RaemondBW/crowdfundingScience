import json
import math
f = open("kickstarter.json")
d = json.load(f)
f.close()
getNumBackers = False

levels = {}
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
    amount = int(amount.replace("$",""))
    floor = int(math.log(amount, 2))
    return 2**floor, 2**(floor+1)

for project in d:
    for amount, value in project["levels"].items():
        try:
            range = str(findRangeLog(amount))
        except:
            continue
        if range not in levels:
            levels[range] = 0
        item = {}
        if getNumBackers:
            levels[range] += value["backers"]
        else:
            levels[range] += value["backers"]*getAmount(amount)

f = open("amountPerFundingLevelAmount.json", 'w')
f.write(json.dumps(levels, indent=4))
f.close()
