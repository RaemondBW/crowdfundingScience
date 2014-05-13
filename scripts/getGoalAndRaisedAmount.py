import json
import math
f = open("kickstarter.json")
d = json.load(f)
f.close()
getNumBackers = False

records = "["
templist = []

for project in d:
    try:
        #templist.append((float(project["totalPledged"]),str(project["name"]),str(project["goal"])))
        templist.append(
        	(
        		float(project["goal"]),
        		float(project["totalPledged"]),
        	)
        )

    except:
         continue

templist = sorted(templist)
for t in templist:
    records+="{\"Goal\": %s, \"Raised\":%s},\n"%(t[0],t[1])

records+="]"
e = open("data3.json", 'w')
e.write(records)
e.close()
